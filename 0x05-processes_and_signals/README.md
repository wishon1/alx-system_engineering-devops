* Project: 0x05. Processes and signals.

* Resources
Read or watch:
- [Linux PID](https://www.linfo.org/pid.html)
- [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
- [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
- [Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)

* man or help:
- ps
- pgrep
- pkill
- kill
- exit
- trap

* Requirements
* General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

More Info
- For those who want to know more and learn about all signals, check out this [article](https://www.computerhope.com/unix/signals.htm)

* Tasks
0. What is my PID
mandatory
- Write a Bash script that displays its own PID.
- File: 0-what-is-my-pid

1. List your processes
mandatory
- Write a Bash script that displays a list of currently running processes.
- Requirements:
	- Must show all processes, for all users, including those which might not have a TTY
	- Display in a user-oriented format
	- Show process hierarchy
- File: 1-list_your_processes

2. Show your Bash PID
mandatory
- Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the   PID of your Bash process.
- Requirements:
	- You cannot use pgrep
	- The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
- File: 2-show_your_bash_pid

3. Show your Bash PID made easy
mandatory
- Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
- Requirements:
	- You cannot use ps
- File: 3-show_your_bash_pid_made_easy

4. To infinity and beyond
mandatory
- Write a Bash script that displays To infinity and beyond indefinitely.
- Requirements:
	- In between each iteration of the loop, add a sleep 2
- File: 4-to_infinity_and_beyond

5. Don't stop me now!
mandatory
- We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
- Write a Bash script that stops 4-to_infinity_and_beyond process.
- Requirements:
	- You must use kill
	- Terminal #0
- File: 5-dont_stop_me_now

6. Stop me if you can
mandatory
- Write a Bash script that stops 4-to_infinity_and_beyond process.
- Requirements:
	- You cannot use kill or killall
	- Terminal #0
- File: 6-stop_me_if_you_can

7. Highlander
mandatory
- Write a Bash script that displays:
- To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
- I am invincible!!! when receiving a SIGTERM signal
- Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infi  nity_and_beyond one.
- Terminal #0
- File: 7-highlander.

8. Beheaded process
mandatory
- Write a Bash script that kills the process 7-highlander.
- Terminal #0
- File: 8-beheaded_process.

9. Process and PID file
#advanced
- Score: 0.0% (Checks completed: 0.0%)
- Write a Bash script that:
- Creates the file /var/run/myscript.pid containing its PID
- Displays To infinity and beyond indefinitely
- Displays I hate the kill command when receiving a SIGTERM signal
- Displays Y U no love me?! when receiving a SIGINT signal
- Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
- File: 100-process_and_pid_file

10. Manage my process
Read:
[&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
[init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
[Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
[Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

- Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: start, restart and stop. The most popular way of doing so on Unix system is to use the init scripts.
- Write a manage_my_process Bash script that:
- Indefinitely writes I am alive! to the file /tmp/my_process
- In between every I am alive! message, the program should pause for 2 seconds
- Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)
