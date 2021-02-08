#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of list
 * @number: input number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner = *head;
	listint_t *pre;
	listint_t *node;
	while(runner)
	{
		if  (runner->n < number)
		{
			pre = runner;
			runner = runner->next;
		}
		else
		{
			node = malloc(sizeof(*node));
			if (node == NULL)
				return (NULL);
			node->next = runner;
			pre->next = node;
			node->n = number;
			return node;
		}
	}
	return (NULL);
}
