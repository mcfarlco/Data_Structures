# Name: Corey McFarland
# Description: To implement a Stack ADT utilizing DynamicArray
# Last revised: 10/27/20

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = "STACK: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        """
        return self.da.length()

    def push(self, value: object) -> None:
        """
        Function to add provided object to top of stack using DynamicArray append().
        """
        self.da.append(value)

    def pop(self) -> object:
        """
        Function to return value from top of the stack and remove from array using DynamicArray get_at_index()
        and remove_at_index().
        """

        # Check if stack is empty
        if self.size() == 0:
            raise StackException

        output = self.da.get_at_index(self.size() - 1)
        self.da.remove_at_index(self.size() - 1)
        return output

    def top(self) -> object:
        """
        Function to return value from top of the stack using DynamicArray get_at_index() and remove_at_index().
        """

        # Check if stack is empty
        if self.size() == 0:
            raise StackException

        output = self.da.get_at_index(self.size() - 1)
        return output


# BASIC TESTING
if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
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

    print("\n# top example 1")
    s = Stack()
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
