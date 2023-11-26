#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - infinite while loop
 * @void: accepts nothing
 * Return a status of 0 (succesful program terminationation)
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
/**
 * main - create 5 zombie processes
 * @void: accepts nothing
 * Return: return a status of 0 (success)
 */
int main(void)
{
	int i = 0;
	pid_t process_id, child_status, wait_pid;

	while ( i < 5)
	{
		process_id = fork();
		if (process_id == -1)
			exit(EXIT_FAILURE);
		else if (process_id == 0)
		{
			printf("Zombie process created, PID: %d\n", process_id);
			sleep(1);
			i++;
		}
		else if (process_id > 0)
		{
			wait_pid = waitpid( process_id, &child_status, 0);
			if (wait_pid == -1)
				exit(EXIT_FAILURE);
		}
	}
	infinite_while();
	return (0);
}
