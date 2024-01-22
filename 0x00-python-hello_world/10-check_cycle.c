#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
listint_t *fst, *nxt;

	if (!list)
	{
		return (0);
	}
	fst = list;
	nxt = list->next;
	while (nxt && fst && nxt->next)
	{
		if (fst == nxt)
		{
			return (1);
		}
		fst = fst->next;
		nxt = nxt->next->next;
	}
    return (0);
}