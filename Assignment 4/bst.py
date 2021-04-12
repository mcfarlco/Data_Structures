# Course: CS261 - Data Structures
# Student Name: Corey McFarland
# Assignment: 4.1
# Description: To implement at BST.


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Method to add a new value to the BST.
        """

        if self.root is None:
            self.root = TreeNode(value)
            return

        parent_node = None
        cur_node = self.root

        while cur_node is not None:
            parent_node = cur_node

            if value < cur_node.value:
                cur_node = cur_node.left

            else:
                cur_node = cur_node.right

        if value < parent_node.value:
            parent_node.left = TreeNode(value)

        else:
            parent_node.right = TreeNode(value)

    def contains(self, value: object) -> bool:
        """
        Method to determine if the provided value is within the BST.
        """
        cur_node = self.root

        while cur_node is not None:

            if value == cur_node.value:
                return True

            elif value < cur_node.value:
                cur_node = cur_node.left

            else:
                cur_node = cur_node.right

        return False

    def get_first(self) -> object:
        """
        Method to return value of root node of a BST.
        """

        if self.root is None:
            return None

        return self.root.value

    def remove_first(self) -> bool:
        """
        Method to remove root node from a BST.
        """

        # Check if tree is empty
        if self.root is None:
            return False

        # Check if root has only a left child
        if self.root.right is None:

            # Check if root has no children
            if self.root.left is None:
                self.root = None
                return True

            # Make left child the new root
            else:
                self.root = self.root.left
                return True

        # Otherwise find in order successor
        sub_parent = None
        successor = self.root.right

        while successor.left is not None:
            sub_parent = successor
            successor = successor.left

        if sub_parent is not None:
            sub_parent.left = successor.right
            successor.right = self.root.right

        # Set successor to new root
        successor.left = self.root.left
        self.root = successor

        return True

    def remove(self, value) -> bool:
        """
        Method to remove the first instance of a provided value from a BST.
        """

        # Check if tree is empty or value is not in tree
        if self.root is None or self.contains(value) == False:
            return False

        # Check if value is at root
        if self.root.value == value:
            self.remove_first()
            return True

        # Initialize variables
        parent = None
        cur_node = self.root

        # Find node to remove
        while cur_node.value != value:
            parent = cur_node

            if value < cur_node.value:
                cur_node = cur_node.left

            else:
                cur_node = cur_node.right

        # Check if node has only a left child
        if cur_node.right is None:

            # Check if node is a leaf, remove if so
            if cur_node.left is None:
                if value < parent.value:
                    parent.left = None
                else:
                    parent.right = None
                return True

            # Make left child the child of the parent node
            else:
                if value < parent.value:
                    parent.left = cur_node.left
                else:
                    parent.right = cur_node.left
                return True

        # Otherwise find in order successor
        sub_parent = None
        successor = cur_node.right

        while successor.left is not None:
            sub_parent = successor
            successor = successor.left

        if sub_parent is not None:
            sub_parent.left = successor.right
            successor.right = cur_node.right

        if successor.value < parent.value:
            parent.left = successor
            successor.left = cur_node.left

        else:
            parent.right = successor
            successor.left = cur_node.left

        return True

    def pre_order_traversal(self) -> Queue:
        """
        Method to traverse a BST in a pre-order method and output the nodes visited in order.
        """

        # Check if tree is empty
        if self.root is None:
            return Queue()

        # Initialize variables
        visit_queue = Queue()
        cur_node = self.root

        # Add node to queue when on its left side.
        def traverse(node):
            if node is not None:
                visit_queue.enqueue(node.value)
                traverse(node.left)
                traverse(node.right)

        traverse(cur_node)

        return visit_queue

    def in_order_traversal(self) -> Queue:
        """
        Method to traverse a BST in an in-order method and output the nodes visited in order.
        """

        # Check if tree is empty
        if self.root is None:
            return Queue()

        # Initialize variables
        visit_queue = Queue()
        cur_node = self.root

        # Add node to queue when on its bottom side.
        def traverse(node):
            if node is not None:
                traverse(node.left)
                visit_queue.enqueue(node.value)
                traverse(node.right)

        traverse(cur_node)

        return visit_queue

    def post_order_traversal(self) -> Queue:
        """
        Method to traverse a BST in a post-order method and output the nodes visited in order.
        """

        # Check if tree is empty
        if self.root is None:
            return Queue()

        # Initialize variables
        visit_queue = Queue()
        cur_node = self.root

        # Add node to queue when on its right side
        def traverse(node):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                visit_queue.enqueue(node.value)

        traverse(cur_node)

        return visit_queue

    def by_level_traversal(self) -> Queue:
        """
        Method to traverse a BST in a post-order method and output the nodes visited in order.
        """

        if self.root is None:
            return Queue()

        cur_node = self.root
        visit_queue = Queue()
        ordered_queue = Queue()

        visit_queue.enqueue(cur_node)
        while not visit_queue.is_empty():
            index_node = visit_queue.dequeue()
            if index_node is not None:
                ordered_queue.enqueue(index_node.value)
                visit_queue.enqueue(index_node.left)
                visit_queue.enqueue(index_node.right)

        return ordered_queue

    def is_full(self) -> bool:
        """
        Method to determine if BST is a full tree.
        """

        # Check if tree is empty
        if self.root is None:
            return True

        def recursive_check(node):

            # If node is a leaf, return true
            if node.left is None and node.right is None:
                return True

            # If node is a parent with a single child, return false
            if node.left is None or node.right is None:
                return False

            # Recurse over child nodes
            return recursive_check(node.left) and recursive_check(node.right)

        return recursive_check(self.root)

    def is_complete(self) -> bool:
        """
        Method to check if BST is a complete tree.
        """

        # Check if tree is empty
        if self.root is None:
            return True

        # Initialize Variables
        cur_node = self.root
        visit_queue = Queue()
        ordered_queue = Queue()

        # Iterate through tree by level, left to right, and add both empty and non-empty nodes.
        visit_queue.enqueue(cur_node)
        while not visit_queue.is_empty():
            index_node = visit_queue.dequeue()

            if index_node is not None:
                ordered_queue.enqueue(index_node.value)
                visit_queue.enqueue(index_node.left)
                visit_queue.enqueue(index_node.right)

            if index_node is None:
                ordered_queue.enqueue(index_node)

        # Remove root from queue
        ordered_queue.dequeue()

        # While queue is not empty
        while not ordered_queue.is_empty():
            value = ordered_queue.dequeue()

            # If left node is empty
            if value is None:

                # Check remaining nodes for values
                while not ordered_queue.is_empty():
                    value = ordered_queue.dequeue()

                    # return false if a value is found
                    if value is not None:
                        return False

            # If queue is still not empty
            if not ordered_queue.is_empty():

                # Check value of right node
                value = ordered_queue.dequeue()

                # If right node is empty
                if value is None:

                    # Check remaining nodes for values
                    while not ordered_queue.is_empty():
                        value = ordered_queue.dequeue()

                        # return false if a value is found as tree is not perfect before last depth
                        if value is not None:
                            return False

        # Otherwise no issues found
        return True

    def is_perfect(self) -> bool:
        """
        Method to check if a BST is a perfect tree.
        """

        # Check if tree is empty
        if self.root is None:
            return True

        # Initialize variables
        count = 0
        height_queue = Queue()

        def recursive_height(node):

            # Retain the count
            nonlocal count

            # If a leaf, enqueue the count, reduce it, then return to previous node.
            if node.left is None and node.right is None:
                height_queue.enqueue(count)
                count -= 1
                return

            # Go to left child first if possible and increase count.
            if node.left is not None:
                count += 1
                recursive_height(node.left)

            # Go to right child and increase count.
            if node.right is not None:
                count += 1
                recursive_height(node.right)

            # If all children have been visited, return to previous node and reduce count.
            count -= 1
            return

        # Recursive call
        recursive_height(self.root)

        # Check if all heights are the same
        same_height = True
        height = None
        while not height_queue.is_empty():

            # Pull off count from first leaf in queue
            value = height_queue.dequeue()

            # If first value, set to height
            if height is None:
                height = value

            # Else compare with height, if not equal return false
            elif value != height:
                return False

        return self.is_full() and same_height

    def size(self) -> int:
        """
        Method to count the size of a BST.
        """

        count = 0
        count_queue = self.by_level_traversal()

        while not count_queue.is_empty():
            count_queue.dequeue()
            count += 1

        return count

    def height(self) -> int:
        """
        Method to determine the height of a BST.
        """

        # Check if tree is empty
        if self.root is None:
            return -1

        # Initialize variables
        count = 0
        max_queue = Queue()

        def recursive_height (node):

            # Retain the count
            nonlocal count

            # If a leaf, enqueue the count, reduce it, then return to previous node.
            if node.left is None and node.right is None:
                max_queue.enqueue(count)
                count -= 1
                return

            # Go to left child first if possible and increase count.
            if node.left is not None:
                count += 1
                recursive_height(node.left)

            # Go to right child and increase count.
            if node.right is not None:
                count += 1
                recursive_height(node.right)

            # If all children have been visited, return to previous node and reduce count.
            count -= 1
            return

        # Recursive call
        recursive_height(self.root)

        # Check maximum value
        max_count = None
        while not max_queue.is_empty():

            # Pull off count from first leaf in queue
            value = max_queue.dequeue()

            # If first value, set to max
            if max_count is None:
                max_count = value

            # Else compare with max and update if needed
            elif value > max_count:
                max_count = value

        return max_count

    def count_leaves(self) -> int:
        """
        Method to count leaves of a BST.
        """

        # Check if tree is empty
        if self.root is None:
            return 0

        # Initialize variables
        count = 0

        def recursive_height(node):

            # Retain the count
            nonlocal count

            # If a leaf, enqueue the count, reduce it, then return to previous node.
            if node.left is None and node.right is None:
                count += 1
                return

            # Go to left child first if possible.
            if node.left is not None:
                recursive_height(node.left)

            # Then go to right child.
            if node.right is not None:
                recursive_height(node.right)

            # If all children have been visited then return to previous node
            return

        # Recursive call
        recursive_height(self.root)

        return count

    def count_unique(self) -> int:
        """
        Method to count the number of unique values in a BST.
        """

        if self.root is None:
            return 0

        count = 1
        value_queue = self.by_level_traversal()
        unique_one = Queue()
        unique_two = Queue()

        while not value_queue.is_empty():

            value = value_queue.dequeue()

            # If first value, add to unique queue.
            if unique_one.is_empty() and unique_two.is_empty():
                unique_one.enqueue(value)

            # If values in unique_one
            if unique_two.is_empty():

                # For every unique value in unique_one
                while not unique_one.is_empty():
                    unq_value = unique_one.dequeue()

                    # If value matches the unique value reduce count and move to next unique value
                    if value == unq_value:
                        count -= 1
                        continue

                    # Otherwise add unique value to other queue.
                    unique_two.enqueue(unq_value)

                # Move current value to other queue and increase count
                unique_two.enqueue(value)
                count += 1

            # If values in unique_two
            else:

                # Same as above except switch queues.
                while not unique_two.is_empty():
                    unq_value = unique_two.dequeue()
                    if value == unq_value:
                        count -= 1
                        continue
                    unique_one.enqueue(unq_value)
                unique_one.enqueue(value)
                count += 1

        return count


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')



