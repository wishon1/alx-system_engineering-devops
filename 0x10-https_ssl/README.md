## Project: HTTPS SSL

### Overview
This project aims to enhance security for web traffic by implementing HTTPS SSL encryption and configuring HAProxy SSL termination. It includes tasks related to configuring domain zones, managing subdomains, and setting up SSL termination for HAProxy.

### Concepts
This project covers the following concepts:
- DNS
- Web stack debugging

### Background Context
Securing website traffic is crucial to protect sensitive information exchanged between users and web servers. HTTPS SSL encryption ensures data confidentiality, integrity, and authenticity by encrypting traffic between the client and server.

### Learning Objectives
By completing this project, you will be able to:
- Explain the roles of HTTPS SSL and its main elements
- Understand the purpose of encrypting traffic and the concept of SSL termination
- Configure DNS settings for subdomains and troubleshoot web stack issues

### Resources
- Read or watch:
  - [What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)
  - [What are the 2 main elements that SSL is providing](https://www.linkedin.com/pulse/what-two-main-roles-ssl-tls-digital-certificates-pem-keystore/)
  - [HAProxy SSL termination on Ubuntu 16.04](https://serversforhackers.com/c/letsencrypt-with-haproxy)
  - [SSL termination](https://www.nginx.com/resources/glossary/ssl-termination/)
- Refer to:
  - `man` pages or online documentation for `awk` and `dig`

### Requirements
- Allowed editors: vi, vim, emacs
- All files should be interpreted on Ubuntu 16.04 LTS
- Bash scripts must be executable and pass Shellcheck without errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`, followed by a comment explaining the script's purpose
- Include a README.md file with detailed instructions and explanations
- Ensure all Bash scripts end with a new line
- Implement functions and command-line arguments as specified in each task
- Use appropriate tools and techniques to achieve project goals

### Tasks
#### 0. World wide web
- Configure domain zone and subdomains
- Write a Bash script to display information about subdomains

#### 1. HAProxy SSL termination
- Configure HAProxy for SSL termination
- Serve encrypted traffic and verify setup
