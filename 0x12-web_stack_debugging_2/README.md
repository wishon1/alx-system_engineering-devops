```markdown
# Web Stack Debugging #2

## Overview

Web Stack Debugging #2 project! This project focuses on advanced web stack debugging tasks, designed to enhance your skills in DevOps, SysAdmin, Scripting, and Debugging.

## Concepts

**Web stack debugging**.

## RESOURCES:
- [webstackdebugging](https://github.com/wishon1/alx-system_engineering-devops/blob/master/0x13-firewall/webstackdebugiing.md)

# TASk
### 0. Run software as another user (mandatory)

Write a Bash script that accepts one argument. The script should run the `whoami` command under the user passed as an argument. Test your script by passing different users.

Example:

```bash
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```

### 1. Run Nginx as Nginx (mandatory)

Fix the container so that Nginx is running as the `nginx` user. Nginx must be listening on all active IPs on port 8080. You cannot use `apt-get remove`. Write a Bash script that configures the container to fit the above requirements.

After debugging:

```bash
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

### 2. 7 lines or less (advanced)

Using what i did for task #1, i made my fix short.

Requirements:

- Your Bash script must be 7 lines long or less
- There must be a new line at the end of the file
- You respect Bash script requirements
- You cannot use `;`
- You cannot use `&&`
- You cannot use `wget`
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)

```
This README.md file provides a detailed overview of the Web Stack Debugging #2 project. It is designed to showcase my technical skills and expertise in web stack debugging.
```
