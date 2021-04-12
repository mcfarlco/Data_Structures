# Course: CS261 - Data Structures
# Student Name: Corey McFarland
# Assignment: 2.4
# Description: To implement a QueueADT utilizing DynamicArray
# Last revised: 10/27/20

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    def enqueue(self, value: object) -> None:
        """
        Function to add provided object to end of queue using DynamicArray append().
        """
        self.da.append(value)

    def dequeue(self) -> object:
        """
        Function to return value from front of the queue and remove from array using DynamicArray get_at_index()
        and remove_at_index().
        """

        # Check if stack is empty
        if self.size() == 0:
            raise QueueException

        output = self.da.get_at_index(0)
        self.da.remove_at_index(0)
        return output


# BASIC TESTING
if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
