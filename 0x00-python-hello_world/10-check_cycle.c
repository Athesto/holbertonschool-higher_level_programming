#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: input list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;

	while (turtle && turtle->next && turtle->next->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
	}
	return (0);

}
