# JetBrains IntelliJ Code Exfiltration Plugin

[![GitHub License](https://img.shields.io/github/license/ChrisCarini/intellij-code-exfiltration?style=flat-square)](https://github.com/ChrisCarini/intellij-code-exfiltration/blob/main/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ChrisCarini/intellij-code-exfiltration/build.yml?branch=main&logo=GitHub&style=flat-square)](https://github.com/ChrisCarini/intellij-code-exfiltration/actions/workflows/build.yml)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ChrisCarini/intellij-code-exfiltration/compatibility.yml?branch=main&label=IntelliJ%20Plugin%20Compatibility&logo=GitHub&style=flat-square)](https://github.com/ChrisCarini/intellij-code-exfiltration/actions/workflows/compatibility.yml)

<!-- Plugin description -->
<b><i><font color="red">==== WARNING! ====</font></i></b>

This plugin is for demonstration purposes only.

It is **_NOT_** intended to be used in any production / real development environment, whatsoever.

Seriously. Do not do it.

<b><i><font color="red">==== WARNING! ====</font></i></b>

This plugin was written to demonstrate code exfiltration from JetBrains IntelliJ. The plugin sends an HTTP POST form
request to https://localhost:8080/upload with the `file` and original `path` as part of the request.
<!-- Plugin description end -->

## Instructions

1) Start the minimal upload server: `cd python_post_server && python3 minimal_upload_server.py`
2) Start an IntelliJ instance with this plugin installed
3) Open a project and file, make a change and save