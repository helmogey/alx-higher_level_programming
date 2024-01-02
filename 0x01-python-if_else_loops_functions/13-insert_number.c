#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_lst;

	new_lst = malloc(sizeof(listint_t));
	if (new_lst == NULL)
		return (NULL);
	new_lst->n = number;

	if (node == NULL || node->n >= number)
	{
		new_lst->next = node;
		*head = new_lst;
		return (new_lst);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new_lst->next = node->next;
	node->next = new_lst;

	return (new_lst);
}
