#!/usr/bin/env python

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
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

SV_HOST = "localhost"
SV_PORT = 8080
BASE_FILE_PATH = "./uploads"
SITE_ROOT = "http://{}:{}".format(SV_HOST, SV_PORT)


def ensure_directory_exists(path_dirname):
    if not os.path.exists(path_dirname):
        os.makedirs(path_dirname)


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_headers()

    def send_headers(self):
        npath = os.path.normpath(self.path)
        npath = npath[1:]
        path_elements = npath.split('/')

        if path_elements[0] == "f":
            reqfile = path_elements[1]

            if not os.path.isfile(reqfile) or not os.access(reqfile, os.R_OK):
                self.send_error(404, "File not found")
                return None

            content, encoding = memetypes.MimeTypes().guess_type(reqfile)
            if content is None:
                content = "application/octet-stream"

            info = os.stat(reqfile)

            self.send_response(200)
            self.send_header("Content-Type", content)
            self.send_header("Content-Encoding", encoding)
            self.send_header("Content-Length", info.st_size)
            self.end_headers()

        elif path_elements[0] == "upload":
            self.send_response(200)
            self.send_header("Content-Type", "text/json; charset=utf-8")
            self.end_headers()

        else:
            self.send_error(404, "Uh oh. Not sure what to do!")
            return None

        return path_elements

    def do_GET(self):
        elements = self.send_headers()
        if elements is None:
            return

        reqfile = elements[1]
        f = open(BASE_FILE_PATH + reqfile, 'rb')
        shutil.copyfileobj(f, self.wfile)
        f.close()

    def do_POST(self):
        elements = self.send_headers()
        if elements is None or elements[0] != "upload":
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

        print "Receiving file: {}".format(filename)
        print "Orig path: {}".format(path)

        # Ensure orig path contains a leading slash and add to base file path
        path = BASE_FILE_PATH + os.path.join("/", path)

        print "To path: {}".format(path)

        # Ensure the directories exist
        path_dirname = os.path.dirname(path)
        ensure_directory_exists(path_dirname)

        # Open file and copy uploaded file into destination
        fdst = open(path, "wb")
        shutil.copyfileobj(form_file, fdst)
        fdst.close()

        # Create result object to send to user
        result = {
            "data": {"url": SITE_ROOT + "/f/" + path},
            "success": True,
            "status": 200,
        }

        print "File received : {} : Stored to: {}".format(filename, path)

        self.wfile.write(json.dumps(result))


ensure_directory_exists(BASE_FILE_PATH)

HTTPServer((SV_HOST, SV_PORT), Handler).serve_forever()
