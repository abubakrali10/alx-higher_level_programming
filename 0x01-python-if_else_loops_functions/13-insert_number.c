#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserting a node inside a sorted linked list
 * @head: head node of the linked list
 * @number: value to store in the new node
 * Return: pointer to the new node or NULL if it fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	int i = 0, j = 0;
	listint_t *traverse = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;

		return (new_node);
	}

	while (number >= traverse->n)
	{
		i++;
		traverse = traverse->next;

		if (!traverse)
			break;
	}

	j = i, i = 0;
	traverse = *head;

	while (i != j - 1)
	{
		i++;
		traverse = traverse->next;
	}
	new_node->next = traverse->next;
	traverse->next = new_node;

	return (new_node);
}
