#!/usr/bin/env python3

"""
Minimal example of a file receiving service in python 2.7 using only built-ins intended for use in the
IntelliJ Code Exfiltration demonstration plugin. There is no error check or security, this is simply meant
to be abase/reference to quickly demonstrate the plugin.

Usage:
    $ python minimal_upload_server.py
    $ curl --form "path=/path/to/file.png" --form file=@/path/to/file.png http://localhost:8080/upload
    {
        "status": 200,
        "data": {"url": "http://localhost:8080/f/uploads/path/to/file.png"},
        "success": true
    }
    $ curl --head --location http://localhost:8080/f/uploads/path/to/file.png
    HTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.7.10
    Date: Wed, 28 Jun 2017 00:43:39 GMT
    Content-Type: image/png
    Content-Encoding: None
    Content-Length: 25182
ShareX / ShareNix settings:
    {
        "Name": "localhost",
        "RequestType": "POST",
        "RequestURL": "http://localhost:8080/upload",
        "FileFormName": "file",
        "ResponseType": "Text",
        "URL": "$json:data.url$"
    }

While not intended to be public, one can change the SV_HOST parameter to an empty string, and port forward
port 80 to 8080 on your firewall.
"""

import cgi
import json
import mimetypes as memetypes
import os
import shutil
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import List

SV_HOST = "localhost"
SV_PORT = 8080
BASE_FILE_PATH = Path.cwd() / "uploads"
SITE_ROOT = f"https://{SV_HOST}:{SV_PORT}"


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_headers()

    def send_headers(self):
        npath = os.path.normpath(self.path)[1:]
        path_elements = npath.split('/')

        if path_elements[0] == "f":
            reqfile = self.to_full_local_path(path_elements)

            if not reqfile.is_file() or not os.access(reqfile, os.R_OK):
                self.send_error(404, "File not found")
                return None

            content, encoding = memetypes.MimeTypes().guess_type(reqfile)
            if content is None:
                content = "application/octet-stream"

            info = reqfile.stat()

            self.send_response(200)
            self.send_header("Content-Type", content)
            self.send_header("Content-Encoding", encoding)
            self.send_header("Content-Length", str(info.st_size))
            self.end_headers()

        elif path_elements[0] == "upload":
            self.send_response(200)
            self.send_header("Content-Type", "text/json; charset=utf-8")
            self.end_headers()

        else:
            self.send_error(404, "Uh oh. Not sure what to do!")
            return None

        return path_elements

    def to_full_local_path(self, path_elements: List[str]) -> Path:
        return BASE_FILE_PATH / Path('/'.join(path_elements[1:]))

    def do_GET(self):
        path_elements = self.send_headers()
        if path_elements is None or path_elements[0] != "f":
            return

        with open(self.to_full_local_path(path_elements), 'rb') as f:
            shutil.copyfileobj(f, self.wfile)

    def do_POST(self):
        path_elements = self.send_headers()
        if path_elements is None or path_elements[0] != "upload":
            return

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": self.headers['Content-Type']
            })
        filename = form['file'].filename
        path = form['path'].value
        form_file = form["file"].file

        print(f"Receiving file: {filename}")
        print(f"Orig path: {path}")

        # Strip leading slash if one exists
        local_path = path[1:] if path[0] == '/' else path

        print(f"To path: {local_path}")

        full_local_path = BASE_FILE_PATH / local_path

        # Ensure the directories exist
        full_local_path.parent.mkdir(exist_ok=True)

        # Open file and copy uploaded file into destination
        with open(full_local_path, "wb") as fdst:
            shutil.copyfileobj(form_file, fdst)

        # Create result object to send to user
        result = {
            "data": {"url": f'{SITE_ROOT}/f/{local_path}'},
            "success": True,
            "status": 200,
        }

        print(f"File received : {filename} : Stored to: {local_path}")

        self.wfile.write(bytes(json.dumps(result), 'UTF-8'))


BASE_FILE_PATH.mkdir(exist_ok=True)

httpd = HTTPServer((SV_HOST, SV_PORT), Handler)
print('Prompting for SSL PEM pass phrase. Enter "asdasd" when prompted.')
httpd.socket = ssl.wrap_socket(
    sock=httpd.socket,
    keyfile='key.pem',
    certfile='cert.pem',
    server_side=True,
)
httpd.serve_forever()
