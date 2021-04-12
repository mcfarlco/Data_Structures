# Course: CS261 - Data Structures
# Assignment: 5.2
# Student: Corey McFarland
# Description: To implement a MinHeap


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *
import random

class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Method to add a new object to the MinHeap.
        """

        self.heap.append(node)
        node_index = self.heap.length() - 1

        # If node_index is a child
        if node_index > 0:

            # Find parent and percolate as needed until root is found.
            p_node = (node_index - 1) // 2
            while p_node is not None:
                if self.heap.get_at_index(p_node) > self.heap.get_at_index(node_index):
                    self.heap.swap(p_node, node_index)

                if p_node == 0:
                    p_node = None

                else:
                    node_index = p_node
                    p_node = (node_index - 1) // 2

        return

    def get_min(self) -> object:
        """
        Method to return the minimum object of a heap.
        """

        # If heap is empty, raise exception
        if self.heap.length() == 0:
            raise MinHeapException

        # Otherwise return root
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Method to remove the minimum object of a heap.
        """

        # If heap is empty, raise exception
        if self.heap.length() == 0:
            raise MinHeapException

        # Initialize variables
        temp = self.get_min()
        node_index = 0

        # Swap root with last index and remove
        self.heap.swap(0, self.heap.length() - 1)
        self.heap.pop()

        if self.heap.length() > 1:

            # Find least value child
            if node_index * 2 + 2 > self.heap.length() - 1 or \
                    self.heap.get_at_index(node_index * 2 + 1) <= self.heap.get_at_index(node_index * 2 + 2):
                c_node = node_index * 2 + 1

            else:
                c_node = node_index * 2 + 2

            # While parent is not at a leaf
            while c_node is not None:

                # If parent is larger, swap with least value child
                if self.heap.get_at_index(node_index) > self.heap.get_at_index(c_node):
                    self.heap.swap(node_index, c_node)

                # Move index to child
                node_index = c_node

                # Check if child is a leaf
                if node_index * 2 + 1 > self.heap.length() - 1:
                    c_node = None

                # Otherwise find next child
                else:
                    if node_index * 2 + 2 > self.heap.length() - 1 or \
                            self.heap.get_at_index(node_index * 2 + 1) <= self.heap.get_at_index(node_index * 2 + 2):
                        c_node = node_index * 2 + 1

                    else:
                        c_node = node_index * 2 + 2

        return temp

    def build_heap(self, da: DynamicArray) -> None:
        """
        Method to create a MinHeap from a provided array and replace the current MinHeap
        """

        # Initialize empty array
        self.heap = DynamicArray()

        for _ in da:
            self.heap.append(_)

        # Start at last parent
        p_node = self.heap.length() // 2 - 1

        # While not at the root
        while p_node >= 0:

            # Find least value child of parent
            if p_node * 2 + 2 > self.heap.length() - 1 or \
                    self.heap.get_at_index(p_node * 2 + 1) <= self.heap.get_at_index(p_node * 2 + 2):
                c_node = p_node * 2 + 1

            else:
                c_node = p_node * 2 + 2

            # Swap if least value child is less than parent
            if self.heap.get_at_index(p_node) > self.heap.get_at_index(c_node):
                self.heap.swap(p_node, c_node)

            # Check if child is a leaf
            if c_node * 2 + 1 > self.heap.length() - 1:
                c_node = None

            node_index = c_node

            # Check if additional percolation is necessary.
            while c_node is not None:

                # Find least value child of index
                if node_index * 2 + 2 > self.heap.length() - 1 or \
                        self.heap.get_at_index(node_index * 2 + 1) <= self.heap.get_at_index(node_index * 2 + 2):
                    c_node = node_index * 2 + 1

                else:
                    c_node = node_index * 2 + 2

                # If parent is larger, swap with least value child
                if self.heap.get_at_index(node_index) > self.heap.get_at_index(c_node):
                    self.heap.swap(node_index, c_node)

                # Move to index of previous child
                node_index = c_node

                # Check if child is a leaf
                if node_index * 2 + 1 > self.heap.length() - 1:
                    c_node = None

                # Otherwise find next child
                else:
                    if node_index * 2 + 2 > self.heap.length() - 1 or \
                            self.heap.get_at_index(node_index * 2 + 1) < self.heap.get_at_index(node_index * 2 + 2):
                        c_node = node_index * 2 + 1

                    else:
                        c_node = node_index * 2 + 2

            # Move to next node
            p_node -= 1


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)


