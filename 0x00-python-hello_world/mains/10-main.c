#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "../lists.h"

int test_3(void);
int test_2(void);
int test_1(void);
/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	test_3();
	test_2();
	test_1();
	return (0);
}

#include <time.h>

/**
 * test_3 - check the code for Holberton School students.
 * Return: Always 0.
 */
int test_3(void)
{
	listint_t *head;
	clock_t start;
	clock_t end;
	clock_t diff;
	int i;

	head = NULL;
	for (i = 0; i < 1001; i++)
		add_nodeint(&head, i);

	start = clock();

	for (i = 0; i < 10; i++)
		check_cycle(head);

	end = clock();

	diff = (double)(end - start) / 10;

	if (diff > 40)
		printf("Runtime too long\n");
	else
		printf("OK\n");

	free_listint(head);

	return (0);
}


/**
 * test_2 - rabbit and turtle
 * Return: (0)
 */
int test_2(void)
{
	listint_t *head;
	listint_t *current, *temp, *reset;
	int i;

	head = NULL;
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 972);
	add_nodeint(&head, 1024);
	add_nodeint(&head, 2048);
	print_listint(head);

	current = head;
	for (i = 0; i < 6; i++)
	{
		if (i == 4)
			temp = current;
		current = current->next;
	}
	reset = current->next;
	current->next = temp;

	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 6; i++)
		current = current->next;
	current->next = reset;

	free_listint(head);

	return (0);
}

/**
 * test_1 - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int test_1(void)
{
	listint_t *head;
	listint_t *current;
	listint_t *temp;
	int i;

	head = NULL;
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 1024);
	print_listint(head);

	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	temp = current->next;
	current->next = head;

	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	current->next = temp;

	free_listint(head);

	return (0);
}
