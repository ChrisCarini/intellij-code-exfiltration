# JetBrains IntelliJ Code Exfiltration Plugin

[![GitHub License](https://img.shields.io/github/license/ChrisCarini/intellij-code-exfiltration?style=flat-square)](https://github.com/ChrisCarini/intellij-code-exfiltration/blob/main/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ChrisCarini/intellij-code-exfiltration/JetBrains%20Plugin%20CI?logo=GitHub&style=flat-square)](https://github.com/ChrisCarini/intellij-code-exfiltration/actions?query=workflow%3A%22JetBrains+Plugin+CI%22)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ChrisCarini/intellij-code-exfiltration/IntelliJ%20Plugin%20Compatibility?label=IntelliJ%20Plugin%20Compatibility&logo=GitHub&style=flat-square)](https://github.com/ChrisCarini/intellij-code-exfiltration/actions?query=workflow%3A%22IntelliJ+Plugin+Compatibility%22)

<!-- Plugin description -->
<b><i><font color="red">==== WARNING! ====</font></i></b>

This plugin is for demonstration purposes only.

It is **_NOT_** intended to be used in any production / real development environment, whatsoever.

Seriously. Do not do it.

<b><i><font color="red">==== WARNING! ====</font></i></b>

This plugin was written to demonstrate code exfiltration from JetBrains IntelliJ. It currently sends a HTTP POST form
request to http://localhost:8080/upload with the `file` and original `path` as part of the request.
<!-- Plugin description end -->

## Instructions
1) Start the minimal upload server: `cd python_post_server && python minimal_upload_server.py`
2) Start an IntelliJ instance with this plugin installed
3) Open a project and file, make a change and save