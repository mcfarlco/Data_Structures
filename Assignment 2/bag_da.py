# Course: CS261 - Data Structures
# Student Name: Corey McFarland
# Assignment: 2.2
# Description: Implementation of a Bag ADT utilizing DynamicArray
# Last revised: 10/27/2020

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """
        Function to add provided object to bag using DynamicArray append().
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Function to remove element of provided value from bag using DynamicArray get_at_index() and remove_at_index().
        """
        for i in range(self.size()):
            if self.da.get_at_index(i) == value:
                self.da.remove_at_index(i)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Function to count objects with provided value in bag using DynamicArray filter() and length().
        """

        # Setup filter function using value.
        def filter_func(f_val):
            if f_val == value:
                return True
            else:
                return False

        # Return length of array provided by filter()
        return self.da.filter(filter_func).length()

    def clear(self) -> None:
        """
        Function to clear all objects from the bag using the DynamicArray remove_at_index()
        """
        for i in range(self.size()):
            self.da.remove_at_index(0)

    def equal(self, second_bag: object) -> bool:
        """
        Function to compare two provided bags by checking the size of each along with the count of each value.
        """

        # If size of bags match, check values.
        if second_bag.size() == self.size():
            for i in range(self.size()):
                if self.count(self.da.get_at_index(i)) != second_bag.count(self.da.get_at_index(i)):
                    # If counts don't match return false.
                    return False

            # If no issues found, bags are equal
            return True

        # If size does not match, return false.
        else:
            return False


# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
