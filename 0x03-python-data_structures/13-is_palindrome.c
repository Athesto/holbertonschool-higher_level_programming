#include "lists.h"
/**
 * compare_nodes - run thro
 * @forward: a forward runner of the list
 * @backward: the same runner bit this will run backward
 * Return: 0, is not palindrome or 1 if is palindrome
 */
static int compare_nodes(listint_t **forward, listint_t *backward)
{
	int is_pal = 0;

	if (backward == NULL)
		return (1);

	is_pal = compare_nodes(forward, backward->next);
	is_pal = is_pal && ((*forward)->n == backward->n);
	*forward = (*forward)->next;
	return (is_pal);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: reference of a list
 * Return: 1 if is a linked, 0 Otherwise
 */
int is_palindrome(listint_t **head)
{
	int i;
	listint_t *runner = *head;

	i = compare_nodes(&runner, runner);
	print_listint(runner);

	return (i);
}
