#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */int is_palindrome(listint_s **head) {
    listint_s *slow = *head, *fast = *head, *first_half = *head, *second_half;

    if (*head == NULL || (*head)->next == NULL) {
        /* An empty list or a single-node list is a palindrome */
        return 1;
    }

    /* Move 'fast' to the middle and 'slow' to the start of the second half */
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        slow = slow->next;
    }

    /* Reverse the second half of the list */
    second_half = reverse_list(slow);

    /* Compare the first and reversed second halves */
    while (second_half != NULL) {
        if (first_half->n != second_half->n) {
            /* The list is not a palindrome */
            return 0;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    /* The list is a palindrome */
    return 1;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
listint_t *reverse_list(listint_t *head) {
    listint_t *prev = NULL, *current = head, *next;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}
