#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include<sys/types.h>

/**
 *  infinite_while - Infinite while loop
 *
 *  Return: Integer
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
 *  main - Main driver function
 *
 *  Return: Void
 */

int main(void)
{

	pid_t zombie;
	int index;

	for (index = 0; index < 5; index++)
	{
		zombie = fork();
		if (zombie > 0)
		{
			printf("Zombie process created, PID: %d\n", zombie);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}
