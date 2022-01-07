#include "lists.h"
/**
 * _compare_extreme_nodes - uses recursion to verify palindrome
 * @head: head of linked list
 * @tail: tail of linked list
 * Return: 0 if is not palindrome, 1 if it is
 */
int _compare_extreme_nodes(listint_t **head, listint_t *tail)
{
	int res;

	if (tail == NULL)
		return (1);

	res = _compare_extreme_nodes(head, tail->next);
	if (res == 0)
		return (0);

	res = ((*head)->n == tail->n);
	*head = (*head)->next;

	return (res);
}
/**
 * is_palindrome - calls for _compare_extreme_nodes
 * @head: head of linked list
 * Return: if null 0 if not 1
 */

int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (_compare_extreme_nodes(head, *head));
}
