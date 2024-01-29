# 0x0F. Load balancer

## Description
This project aims to enhance the web stack by introducing redundancy for web servers, improving reliability, and increasing traffic handling capacity. It involves configuring web servers behind a load balancer and adding custom Nginx response headers to track server responses.

## Concepts
For this project, understanding of the following concepts is required:
- Load balancer
- Web stack debugging

## Background Context
Two additional servers have been provided:
- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

The goal is to automate the configuration of a new Ubuntu server to match the project requirements using Bash scripts.

## Tasks
### 0. Double the number of webservers
Configure web-02 to be identical to web-01 and add a custom Nginx response header "X-Served-By" to identify the serving web server.

### 1. Install your load balancer
Install and configure HAproxy on lb-01 server to distribute traffic between web-01 and web-02 using a round-robin algorithm.

## Requirements
- All files will be interpreted on Ubuntu 16.04 LTS.
- Bash scripts must pass Shellcheck (version 0.3.7) without any error.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- Servers should be configured with the correct hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.

## Repo Structure
- Directory: 0x0F-load_balancer
    - `0-custom_http_response_header`: Bash script to configure Nginx and add custom response headers.
    - `1-install_load_balancer`: Bash script to install and configure HAproxy as a load balancer.

## Resources
- Introduction to load-balancing and HAproxy
- HTTP header
- Debian/Ubuntu HAProxy packages

## Usage
To execute the scripts, ensure they are executable and run them in the respective server environments.
