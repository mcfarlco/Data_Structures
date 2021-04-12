# Course: CS261 - Data Structures
# Assignment: 5.1
# Student: Corey McFarland
# Description: To implement a Hash Map


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Method to clear hash map content.
        """

        # For all buckets
        for _ in range(self.capacity):

            # If bucket is not empty, make empty and reduce size by linked list length
            if self.buckets.get_at_index(_).length() != 0:
                self.size -= self.buckets.get_at_index(_).length()
                self.buckets.set_at_index(_, LinkedList())


    def get(self, key: str) -> object:
        """
        Method to return value of provided key in hash table.
        """

        # Check if key is in hash table
        if not self.contains_key(key):
            return None

        hash = self.hash_function(key)
        index = hash % self.capacity

        return self.buckets.get_at_index(index).contains(key).value

    def put(self, key: str, value: object) -> None:
        """
        Method to update key of hash table with provided value.
        """

        hash = self.hash_function(key)
        index = hash % self.capacity

        # If index already has the key, remove it
        if self.buckets.get_at_index(index).contains(key) is not None:
            self.buckets.get_at_index(index).remove(key)
            self.size -= 1

        # Add key
        self.buckets.get_at_index(index).insert(key, value)
        self.size += 1

        return

    def remove(self, key: str) -> None:
        """
        Method to remove key and related value from hash map.
        """

        # Check if key is in hash table
        if not self.contains_key(key):
            return

        hash = self.hash_function(key)
        index = hash % self.capacity

        # Go to index and remove key
        self.buckets.get_at_index(index).remove(key)
        self.size -= 1

        return


    def contains_key(self, key: str) -> bool:
        """
        Method to determine if a hash table contains the provided key.
        """

        if self.size == 0:
            return False

        # Iterate through buckets and any linked lists, return true if key is found
        for _ in range(self.capacity):
            if self.buckets.get_at_index(_).contains(key) is not None:
                return True

        return False

    def empty_buckets(self) -> int:
        """
        Method to return the number of empty buckets in the hash table.
        """

        count = self.capacity

        for _ in range(self.capacity):
            # Reduce count for each non-empty bucket
            if self.buckets.get_at_index(_).length() > 0:
                count -= 1

        return count

    def table_load(self) -> float:
        """
        Method to determine the load factor of the hash table.
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        Method to change capacity size to provided value.
        """

        # Check if capacity is valid
        if new_capacity < 1:
            return

        # Initialize variables
        temp_array = self.buckets
        old_capacity = self.capacity
        clean_array = HashMap(new_capacity, self.hash_function)

        # Remove content and update capacity
        self.buckets = clean_array.buckets
        self.capacity = new_capacity

        # If hash map had content
        if self.size > 0:
            # For each previous index with non-empty buckets, add a node without increasing size.
            for _ in range(old_capacity):
                if temp_array.get_at_index(_).length() > 0:
                    for node in temp_array.get_at_index(_):
                        self.size -= 1
                        self.put(node.key, node.value)

        return

    def get_keys(self) -> DynamicArray:
        """
        Method to return an array of keys from the hash map.
        """

        key_array = DynamicArray()

        # If hash table is empty, return empty array
        if self.size < 1:
            return key_array

        # Else, iterate through buckets and linked lists in non-empty buckets to append the key.
        for _ in range(self.capacity):
            if self.buckets.get_at_index(_).length() > 0:
                for node in self.buckets.get_at_index(_):
                    key_array.append(node.key)


        return key_array


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
