# Name: Corey McFarland
# Description: To implement a Stack ADT using a linked list.

from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def is_empty(self) -> bool:
        """
        Return True is Maxstack is empty, False otherwise
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the MaxStack
        """
        return self.sll_val.length()


    def push(self, value: object) -> None:
        """
        Method to add value to front of the linked list.
        """

        # Add to front of linked list.
        self.sll_val.add_front(value)

        # If list was empty, also add value to max stack.
        if self.sll_max.length() == 0:
            self.sll_max.add_front(value)

        # Else check if value is greater than or equal to top of max stack and add is so.
        else:
            max = self.sll_max.get_front()
            if value >= max:
                self.sll_max.add_front(value)

    def pop(self) -> object:
        """
        Method to return value of top of stack and remove from list.
        """

        # Check if list is empty
        if self.is_empty():
            raise StackException

        # Store value and remove from stack
        value = self.sll_val.get_front()
        self.sll_val.remove_front()

        # If value was in the max stack, remove from max stack.
        self.sll_max.remove(value)

        return value

    def top(self) -> object:
        """
        Method to get value of top of stack without removing.
        """

        # Check is list is empty.
        if self.is_empty():
            raise StackException

        return self.sll_val.get_front()

    def get_max(self) -> object:
        """
        Method to return top value from max stack.
        """

        # Check if list is empty
        if self.is_empty():
            raise StackException

        return self.sll_max.get_front()


# BASIC TESTING
if __name__ == "__main__":
    pass

    print('\n# push example 1')
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print('\n# pop example 1')
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print('\n# top example 1')
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)

    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))

