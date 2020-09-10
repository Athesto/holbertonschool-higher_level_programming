#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false !true
#define BUFSIZE 102400

/**
 * is_palindrome - check if it's a palindrome list
 * @head: head list
 * Return: 1 is true or 0 is false
 */
int is_palindrome(listint_t **head)
{
	unsigned int l_len;		/* list len */
	listint_t *runner = *head;	/* runner pointer */
	int array[BUFSIZE];				/* array of numbers */
	unsigned int a_idx;		/* array index */

	/* check if it's a valid list */
	if (!head || !*head || !(*head)->next)
		return (true);

	/* fill the array */
	runner = *head;
	for (a_idx = 0; runner; a_idx++)
	{
		l_len = a_idx;
		array[a_idx] = runner->n;
		runner = runner->next;
	}
	l_len++;

	/* check array */
	for (a_idx = 0; a_idx < l_len / 2; a_idx++)
	{
		if ((array[a_idx] - array[l_len - a_idx - 1]) != 0)
		{
			return (false);
		}
	}
	return (true);
}
