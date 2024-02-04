# ALX System Engineering & DevOps - Web Stack Debugging #1

## Concepts(resoureces)
- [Network basics]Networking is a big part of what made computers so powerful and why the Internet exists. It allows machines to communicate with each other.

[What is a protocol](https://www.techtarget.com/searchnetworking/definition/protocol)
[hat is an IP address](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)
[hat is TCP/IP](https://www.avast.com/c-what-is-tcp-ip#)
[hat is an Internet Protocol (IP) port?)](https://www.lifewire.com/port-numbers-on-computer-networks-817939)
- [Web stack debugging]()
Certainly! Here's the updated README.md file including the provided commands and outputs:

---
overview

This project is part of the SE Foundations curriculum by Sylvain Kalache. It focuses on debugging web stack issues, specifically related to Nginx configuration. The tasks involve identifying and resolving issues that prevent Nginx from listening on port 80.

## Requirements
- **Allowed Editors**: vi, vim, emacs
- **Interpreted On**: Ubuntu 20.04 LTS
- **File Endings**: All files should end with a new line
- **Mandatory Files**: A README.md file at the root of the project folder is mandatory
- **Executable Scripts**: All Bash script files must be executable
- **Shellcheck**: Bash scripts must pass Shellcheck without any error
- **No Error**: Bash scripts must run without error
- **Script Header**: The first line of all Bash scripts should be `#!/usr/bin/env bash`
- **Comments**: The second line of all Bash scripts should explain what the script is doing
- **wget**: You are not allowed to use `wget`

### Tasks

#### Task 0: Nginx likes port 80 (mandatory)

- **Description**: Debug Nginx configuration to ensure it listens on port 80 of all active IPv4 IPs.
- **Requirements**: Write a Bash script to configure the server accordingly.

#### Task 1: Make it sweet and short (advanced)

- **Description**: Refactor the solution from Task 0 to be concise within 5 lines.
- **Additional Requirements**: Must use standard Bash scripting conventions, and `service nginx status` should confirm Nginx is not running.

## Test Outputs

```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#

root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#

root@966c5664b21f:/# service nginx status
 * nginx is not running
root@966c5664b21f:/#
```
