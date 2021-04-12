# Name: Corey McFarland
# Description: To implement a Deque and Bag ADT with a circular doubly linked list.


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        """
        return self.sentinel.next == self.sentinel

    def add_front(self, value: object) -> None:
        """
        Method to add node with provided value to front of linked list.
        """

        # Initialize variable
        new_node = DLNode(value)

        # Add node
        new_node.next = self.sentinel.next
        new_node.next.prev = new_node

        self.sentinel.next = new_node
        new_node.prev = self.sentinel

    def add_back(self, value: object) -> None:
        """
        Method to add node with provided value to end of linked list.
        """
        # Initialize variable
        new_node = DLNode(value)

        # Add node.
        new_node.prev = self.sentinel.prev
        self.sentinel.prev.next = new_node

        new_node.next = self.sentinel
        self.sentinel.prev = new_node


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Method to insert new node with the provided value into the linked list.
        """

        # Check if index is valid.
        if index < 0 or index > self.length():
            raise CDLLException

        # Initialize variables
        new_node = DLNode(value)
        cur_node = self.sentinel

        # Iterate to index
        for i in range(index):
            cur_node = cur_node.next

        # Add node
        new_node.next = cur_node.next
        cur_node.next.prev = new_node

        cur_node.next = new_node
        new_node.prev = cur_node



    def remove_front(self) -> None:
        """
        Method to remove first node in a linked list
        """

        # Check if linked list is empty
        if self.length() == 0:
            raise CDLLException

        # Remove first node
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        Method to remove last node in a linked list
        """

        # Check if linked list is empty
        if self.length() == 0:
            raise CDLLException

        # Remove last node
        self.sentinel.prev = self.sentinel.prev.prev
        self.sentinel.prev.next = self.sentinel

    def remove_at_index(self, index: int) -> None:
        """
        Method to remove a node at the provided index from the linked list.
        """

        # Check if index is valid
        if index < 0 or index >= self.length():
            raise CDLLException

        # Initialize variables
        cur_node = self.sentinel.next

        # Iterate through to index
        for i in range(index):
            cur_node = cur_node.next

        # Remove node.
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev

    def get_front(self) -> object:
        """
        Method to return value of first node in linked list.
        """

        # Check if linked list is empty.
        if self.length() == 0:
            raise CDLLException

        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Method to return value of last node in linked list.
        """

        # Check if linked list is empty.
        if self.length() == 0:
            raise CDLLException

        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Method to remove the first node containing the provided value from the linked list.
        """

        # Initialize variable
        cur_node = self.sentinel.next

        # Iterate through list until value is found.
        while cur_node.value != value:

            # If list does not contain value, return false.
            if cur_node == self.sentinel:
                return False

            else:
                cur_node = cur_node.next

        # Remove node from list
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev

        return True

    def count(self, value: object) -> int:
        """
        Method to count the number of times a value appears in the linked list.
        """

        # Initialize variables
        cur_node = self.sentinel.next
        count = 0

        # Iterate through list, adding 1 to count for each time value is found.
        while cur_node != self.sentinel:
            if cur_node.value == value:
                count += 1

            cur_node = cur_node.next

        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Method to swap the nodes for two provided indexes in the linked list
        """

        # Check if indexes are valid
        if index1 < 0 or index1 >= self.length() or index2 < 0 or index2 >= self.length():
            raise CDLLException

        # Initialize variables
        node_one = self.sentinel.next
        node_two = self.sentinel.next

        # Iterate through to index1
        for i in range(index1):
            node_one = node_one.next

        # Iterate through to index2
        for i in range(index2):
            node_two = node_two.next

        # Initialize holding variables
        temp_next = node_one.next
        temp_prev = node_one.prev

        # If indexes are forwards adjacent
        if index1 - index2 == -1:

            # Set node one's next to node two's
            node_one.next = node_two.next
            node_one.next.prev = node_one

            # Swap positions
            node_one.prev = node_two
            node_one.prev.next = node_one

            # Set node two's previous to node one's
            node_two.prev = temp_prev
            node_two.prev.next = node_two

            return

        # If indexes are backwards adjacent
        if index1 - index2 == 1:

            # Set node one's previous to node two's
            node_one.prev = node_two.prev
            node_one.prev.next = node_one

            # Swap positions
            node_one.next = node_two
            node_one.next.prev = node_one

            # Set node two's next to node one's
            node_two.next = temp_next
            node_two.next.prev = node_two

            return

        else:
            # Swap node one to node two
            node_one.next = node_two.next
            node_one.next.prev = node_one

            node_one.prev = node_two.prev
            node_one.prev.next = node_one

            # Swap node two to node one
            node_two.next = temp_next
            node_two.next.prev = node_two

            node_two.prev = temp_prev
            node_two.prev.next = node_two

    def reverse(self) -> None:
        """
        Method to reverse the nodes in the linked list
        """

        for i in range(self.length() // 2):
            self.swap_pairs(i, (self.length() - 1 - i))


    def sort(self) -> None:
        """
        Method to sort nodes in ascending order.
        """

        # Initialize variables
        index = self.sentinel.next
        index_num = 0

        # Insertion sort
        while index.next != self.sentinel:

            # Update index
            index = index.next
            index_num += 1

            # Update comparison position
            pos = index.prev
            pos_num = index_num - 1

            while pos != self.sentinel and pos.value > index.value:

                # Swap nodes at position
                self.swap_pairs(pos_num + 1, pos_num)

                # If node was swapped, update index of node
                if pos_num + 1 == index_num:
                    index_num -= 1

                # Update comparison position
                pos = pos.prev.prev
                pos_num -= 1

    def rotate(self, steps: int) -> None:
        """
        Method to rotate nodes in a linked list a number of steps in the provided positive or negative direction.
        """

        # Check if linked list is empty
        if self.is_empty():
            return self

        # If steps are positive, rotate to the left.
        if steps > 0:
            for i in range(steps % self.length()):

                # Initialize variable
                temp_prev = self.sentinel.prev.prev

                # Set sentinel's previous' next to the sentinel's
                self.sentinel.prev.next = self.sentinel.next
                self.sentinel.next.prev = self.sentinel.prev

                # Swap positions
                self.sentinel.prev.prev = self.sentinel
                self.sentinel.prev.prev.next = self.sentinel.prev

                # Set sentinel's previous to its previous'
                self.sentinel.prev = temp_prev
                self.sentinel.prev.next = self.sentinel

        # If steps are negative, rotate to the right
        if steps < 0:
            for i in range(abs(steps) % self.length()):

                # Initialize variable
                temp_next = self.sentinel.next.next

                # Set sentinel next's previous to sentinel's
                self.sentinel.next.prev = self.sentinel.prev
                self.sentinel.next.prev.next = self.sentinel.next

                # Swap positions
                self.sentinel.next.next = self.sentinel
                self.sentinel.next.next.prev = self.sentinel.next

                # Set sentinel's next to sentinel next's
                self.sentinel.next = temp_next
                self.sentinel.next.prev = self.sentinel

    def remove_duplicates(self) -> None:
        """
        Method to remove duplicates
        """

        if self.is_empty():
            return

        size = 0
        start_val = self.get_front()

        while size != self.length():
            if self.count(self.get_front()) > 1:
                for i in range(self.count(self.get_front())):
                    self.remove_front()

                if self.length() > 0 and size == 0:
                    start_val = self.get_front()

            else:
                size += 1
                self.rotate(-1)

    def odd_even(self) -> None:
        """
        Method to order odd position nodes before even position nodes
        """

        # Start node is first even node
        even_node = self.sentinel.next.next
        even_value = even_node.value

        # Iterate over each even node
        for i in range(self.length() // 2):

            # Add node value to end
            self.add_back(even_value)

            # Move to next node
            even_node = even_node.next.next

            # Remove previous node
            self.remove(even_value)

            # Update node value
            even_value = even_node.value


if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)

    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)

    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())

    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)

    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)

    print('\n# reverse example 3')


    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age

        def __eq__(self, other):
            return self.age == other.age

        def __str__(self):
            return str(self.name) + ' ' + str(self.age)


    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)

    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)

    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)

    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)

    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)

    print('\n# odd_even example 1')
    test_cases = (
        [1, 2, 3, 4, 5], list('ABCDE'),
        [], [100], [100, 200], [100, 200, 300],
        [100, 200, 300, 400],
        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)
