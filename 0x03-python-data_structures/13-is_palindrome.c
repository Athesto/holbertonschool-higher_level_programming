#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false !true

/**
 * is_palindrome - check if it's a palindrome list
 * @head: head list
 * Return: 1 is true or 0 is false
 */
int is_palindrome(listint_t **head)
{
	unsigned int l_len;		/* list len */
	listint_t *runner = *head;	/* runner pointer */
	int *array;				/* array of numbers */
	unsigned int a_idx;		/* array index */

	/* check if it's a valid list */
	if (!head || !(*head)->next)
		return (true);

	for (l_len = 0; runner; l_len++)
		runner = runner->next;

	array = malloc(l_len * sizeof(*array));

	/* fill the array */
	runner = *head;
	for (a_idx = 0; a_idx < l_len; a_idx++)
	{
		array[a_idx] = runner->n;
		runner = runner->next;
	}

	/* check array */
	for (a_idx = 0; a_idx < l_len / 2; a_idx++)
	{
		if ((array[a_idx] - array[l_len - a_idx - 1]) != 0)
		{
			free(array);
			return (false);
		}
	}
	free(array);
	return (true);
}
