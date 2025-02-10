* PROJECT: 0x08. Networking basics #1

* Resources
+ Read or watch:

+ [What is localhost](https://en.wikipedia.org/wiki/Localhost)
+ [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
+ [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
+ [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)

* man or help:
+ ifconfig
+ telnet
+ nc
+ cut

* Tasks

0. Change your home IP
+ mandatory
+ Write a Bash script that configures an Ubuntu server with the below requirements.
+ Requirements:
	- localhost resolves to 127.0.0.2
	- facebook.com resolves to 8.8.8.8.
	- The checker is running on Docker, so make sure to read this
	- File: 0-change_your_home_IP

1. Show attached IPs
+ mandatory
+ Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
	- File: 1-show_attached_IPs
