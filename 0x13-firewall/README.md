## Background Context
## concept:
	[Web stack debugging]()

This project dives deeper into working on servers work without a firewall, understanding how to debug web stack issues related to firewall configurations.

## Resources

- [What is a firewall](https://en.wikipedia.orgawiki/Firewall_%28computing%29)
- [Webstack debugging](https://github.com/wishon1/alx-system_engineering-devops/blob/master/0x13-firewall/webstackdebugiing.md)
- **More Info:**
  As explained in the web stack debugging guide, telnet is a valuable tool to check if sockets are open. For example, to check if port 22 is open on web-02:

  ```bash
  sylvain@ubuntu$ telnet web-02.holberton.online 22
  Trying 54.89.38.100...
  Connected to web-02.holberton.online.
  Escape character is '^]'.
  SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

  Protocol mismatch.
  Connection closed by foreign host.
  sylvain@ubuntu$
  ```

  We can see that the connection is successful. Now let’s try connecting to port 2222:

  ```bash
  sylvain@ubuntu$ telnet web-02.holberton.online 2222
  Trying 54.89.38.100...
  ^C
  sylvain@ubuntu$
  ```

  We can see that the connection never succeeds. This method can be used not only for this exercise but also for any debugging situation where two pieces of software need to communicate over sockets.

  Note that the school network filters outgoing connections via a network-based firewall, limiting interaction with certain ports on servers outside of the school network. To test your work on web-01, perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will originate from web-02, bypassing the firewall.

## Warning!

- Containers on demand cannot be used for this project due to Docker container limitations.
- Be cautious with firewall rules! For instance, denying port 22/TCP and logging out of your server will prevent SSH reconnection, and recovery may not be possible. When installing UFW, port 22 is blocked by default, so unblock it immediately before logging out of your server.

## Tasks

### 0. Block all incoming traffic but (mandatory)

Install the ufw firewall on **web-01** and set up rules to block all incoming traffic except for ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).

### 1. Port forwarding (advanced)

Configure **web-01** to forward port 8080/TCP to port 80/TCP.
