# 0x0D. Web Stack Debugging #0

## Description

- Debugging project focusing on Docker, web stack, and network basics.

## Background Context

- Example fixing Docker container: copy /etc/passwd to /tmp, create /tmp/isworking.

```bash
docker run -d -ti ubuntu:14.04
docker exec -ti CONTAINER_ID /bin/bash
cp /etc/passwd /tmp/
echo OK > /tmp/isworking

+ Answer file:
#!/usr/bin/env bash
# Fix server with these 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking

### Tasks
#### 0. Give me a page! (mandatory)
Get Apache running in Docker, return "Hello Holberton" on querying root.

	Example:
	docker run -p 8080:80 -d -it holbertonschool/265-0
	docker ps
	curl 0:8080  # Expects "Hello Holberton"

## Installing Docker

- Provided container for the task. Install on Mac, Windows, or Ubuntu 16.04 locally if needed.


