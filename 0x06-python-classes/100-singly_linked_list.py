#!/usr/bin/python3

"""Define a class Node."""
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.data = value

    @property
    def next_node(self):
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = 0

    def sorted_insert(self, value):
        """
                Inserts a new node into the linked list in increasing order.

                Args:
                    new_node: The new node to be inserted.

                Returns:
                    None
                """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new