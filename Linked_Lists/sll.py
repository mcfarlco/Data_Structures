# Name: Corey McFarland
# Description: To implement Deque and Bag ADTs with a singly linked list.


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        """
        return self.head.next == self.tail

    def add_front(self, value: object) -> None:
        """
        Method to add node with provided value to front of linked list.
        """

        # Initialize variable
        new_node = SLNode(value)

        # Add node
        new_node.next = self.head.next
        self.head.next = new_node

    def add_back(self, value: object) -> None:
        """
        Method to add node with provided value to end of linked list.
        """
        # Initialize variables
        new_node = SLNode(value)
        cur_node = self.head

        # Iterate to last item in list
        while cur_node.next != self.tail:
            cur_node = cur_node.next

        # Add node.
        new_node.next = self.tail
        cur_node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Method to insert new node with the provided value into the linked list.
        """

        # Check if index is valid.
        if index < 0 or index > self.length():
            raise SLLException

        # Initialize variables
        new_node = SLNode(value)
        cur_node = self.head

        # Iterate to index
        for i in range(index):
            cur_node = cur_node.next

        # Add node
        new_node.next = cur_node.next
        cur_node.next = new_node

    def remove_front(self) -> None:
        """
        Method to remove first node in a linked list
        """

        # Check if linked list is empty
        if self.head.next == self.tail:
            raise SLLException

        # Remove first node
        self.head.next = self.head.next.next

    def remove_back(self) -> None:
        """
        Method to remove last node in linked list.
        """

        # Check if list is empty
        if self.head.next == self.tail:
            raise SLLException

        # Initialize variable
        cur_node = self.head

        # Iterate until second to last node.
        while cur_node.next.next != self.tail:
            cur_node = cur_node.next

        # Remove last node.
        cur_node.next = self.tail

    def remove_at_index(self, index: int) -> None:
        """
        Method to remove a node at the provided index from the linked list.
        """

        # Check if index is valid
        if index < 0 or index >= self.length():
            raise SLLException

        # Initialize variables
        cur_node = self.head.next
        prev_node = self.head

        # Iterate through to index
        for i in range(index):
            prev_node = cur_node
            cur_node = cur_node.next

        # Remove node.
        prev_node.next = cur_node.next

    def get_front(self) -> object:
        """
        Method to return value of first node in linked list.
        """

        # Check if linked list is empty.
        if self.head.next == self.tail:
            raise SLLException

        return self.head.next.value

    def get_back(self) -> object:
        """
        Method to return value of last node.
        """

        # Check if list is empty.
        if self.head.next == self.tail:
            raise SLLException

        # Initialize variable
        cur_node = self.head

        # Iterate until second to last node.
        while cur_node.next != self.tail:
            cur_node = cur_node.next

        return cur_node.value

    def remove(self, value: object) -> bool:
        """
        Method to remove the first node containing the provided value from the linked list.
        """

        # Initialize variables
        cur_node = self.head.next
        prev_node = self.head

        # Iterate through list until value is found.
        while cur_node.value != value:

            # If list does not contain value, return false.
            if cur_node == self.tail:
                return False

            else:
                prev_node = cur_node
                cur_node = cur_node.next

        # Remove node from list
        prev_node.next = cur_node.next
        return True

    def count(self, value: object) -> int:
        """
        Method to count the number of times a value appears in the linked list.
        """

        # Initialize variables
        cur_node = self.head.next
        count = 0

        # Iterate through list, adding 1 to count for each time value is found.
        while cur_node != self.tail:
            if cur_node.value == value:
                count += 1

            cur_node = cur_node.next

        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Method to create a new linked list from the provided slice.
        """

        # Check if index and size are valid:
        if start_index < 0 or start_index == self.length() or (start_index + size) > self.length() or size < 0:
            raise SLLException

        # Initialize variables
        slice_list = LinkedList()
        cur_node = self.head.next

        # Move to start index
        for i in range(start_index):
            cur_node = cur_node.next

        # Add slice to list
        for i in range(size):
            slice_list.add_back(cur_node.value)
            cur_node = cur_node.next

        return slice_list


if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

