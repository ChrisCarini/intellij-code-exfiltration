# JetBrains IntelliJ Code Exfiltration Plugin

[![GitHub License](https://img.shields.io/github/license/ChrisCarini/intellij-code-exfiltration?style=flat-square)](https://github.com/ChrisCarini/intellij-code-exfiltration/blob/main/LICENSE)
[![All Contributors](https://img.shields.io/github/all-contributors/ChrisCarini/intellij-code-exfiltration?color=ee8449&style=flat-square)](#contributors)
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

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ChrisCarini"><img src="https://avatars.githubusercontent.com/u/6374067?v=4?s=100" width="100px;" alt="Chris Carini"/><br /><sub><b>Chris Carini</b></sub></a><br /><a href="#bug-ChrisCarini" title="Bug reports">🐛</a> <a href="#code-ChrisCarini" title="Code">💻</a> <a href="#doc-ChrisCarini" title="Documentation">📖</a> <a href="#example-ChrisCarini" title="Examples">💡</a> <a href="#ideas-ChrisCarini" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-ChrisCarini" title="Maintenance">🚧</a> <a href="#question-ChrisCarini" title="Answering Questions">💬</a> <a href="#review-ChrisCarini" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->