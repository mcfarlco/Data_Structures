# Course: CS261 - Data Structures
# Student Name: Corey McFarland
# Assignment: 2.1
# Description: Implement a Dynamic Array
# Last revised: 10/27/20


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """
        Internal function to increase the capacity of the provided DynamicArray to the provided amount.
        """

        # Checks for invalid inputs
        if new_capacity < self.size:
            return

        if new_capacity <= 0:
            return

        else:

            # Update Capacity
            self.capacity = new_capacity

            # Create new StaticArray at the new capacity with the elements from the user provided DynamicArray
            cur_arr = StaticArray(new_capacity)
            for i in range(self.size):
                cur_arr[i] = self.data[i]

            # Update user provided DynamicArray data to new StaticArray
            self.data = cur_arr
            return

    def append(self, value: object) -> None:
        """
        Function to add a user provided element to the end of a provided DynamicArray, increasing capacity as needed.
        """

        # Do nothing if an element containing None is passed
        if value is None:
            return

        # Otherwise check if capacity needs to increase.
        if self.size == self.capacity:
            self.resize(self.size * 2)

        # Initialize list if empty
        if self.size == 0:
            self.data[0] = value
            self.size += 1

        # Add value to end of the array
        else:
            self.data[self.size] = value
            self.size += 1
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Function to insert a provided element to a provided index within the provided DynamicArray.
        """

        # Check for value index
        if index > self.size or index < 0:
            raise DynamicArrayException

        # If index is at the end of the list, send to append function.
        if index == self.size:
            self.append(value)
            return

        # if adding an element would be over the capacity, increase capacity.
        if self.size + 1 > self.capacity:
            self.resize(self.size * 2)

        # Create temporary DynamicArray to properly order elements.
        shift_arr = DynamicArray()

        # If index is 0, append new value first then append the remaining elements of the array.
        if index == 0:

            shift_arr.append(value)

            for i in range(self.size):
                shift_arr.append(self.data[i])

        # Otherwise append the elements from the array up to the index, append the new value, then append the rest.
        else:
            for i in range(index):
                shift_arr.append(self.data[i])

            shift_arr.append(value)

            for i in range(self.size - index):
                shift_arr.append(self.data[i + index])

        self.size += 1
        self.data = shift_arr.data
        return

    def get_at_index(self, index: int) -> object:
        """
        Function to return data value from a DynamicArray at the provided index.
        """

        # Check for invalid index
        if index > (self.size - 1) or index < 0:
            raise DynamicArrayException

        return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        Function to delete an element of a DynamicArray at the provided index.
        """

        # Check for valid index
        if index > (self.size - 1) or index < 0:
            raise DynamicArrayException

        # Check if capacity needs to be reduced, with a minimum capacity of 10 unless already below at which point no
        # reduction occurs.
        if self.size < (self.capacity / 4) and self.capacity >= 10:
            if self.size * 2 < 10:
                self.capacity = 10

            else:
                self.capacity = self.size * 2

        # Remove element from array.
        self.data[index] = None
        self.size -= 1

        # Create temporary array to re-order the elements.
        rem_arr = DynamicArray()

        if index == 0:

            for i in range(self.size):
                rem_arr.append(self.data[i+1])

        else:
            for i in range(index):
                rem_arr.append(self.data[i])

            for i in range(self.size - index):
                rem_arr.append(self.data[i + index + 1])

        self.data = rem_arr.data

        return

    def slice(self, start_index: int, quantity: int) -> object:
        """
        Function to return a new DynamicArray of a slice of the provided DynamicArray.
        """

        # Check to invalid index
        if start_index > (self.size - 1) or start_index < 0:
            raise DynamicArrayException

        # Check for invalid quantity
        if quantity > self.size or (start_index + quantity) > self.size or quantity < 0:
            raise DynamicArrayException

        # DynamicArray of sliced values.
        slice_arr = DynamicArray()

        for i in range(quantity):
            slice_arr.append(self.data[i + start_index])

        return slice_arr

    def merge(self, second_da: object) -> None:
        """
        Function to append each element of a DynamicArray to the initial array.
        """

        for i in range(second_da.size):
            self.append(second_da.data[i])

        pass

    def map(self, map_func) -> object:
        """
        Function to create a new Dynamic array that applies a provided map function to the provided DynamicArray
        """

        map_arr = DynamicArray()
        for i in range(self.size):
            map_arr.append(map_func(self.data[i]))

        return map_arr

    def filter(self, filter_func) -> object:
        """
        Function to create a new Dynamic array consisting of true values of a provided filter function.
        """

        filter_arr = DynamicArray()
        for i in range(self.size):
            if filter_func(self.data[i]) is True:
                filter_arr.append(self.data[i])

        return filter_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Function to apply a reduce function to a provided array, utilizing a provided initalizer as needed.
        """

        # If array is empty, return value of initializer
        if self.size == 0:
            return initializer

        # If initalizer is not provided, use first value in array as initalizer and apply reduce function.
        if initializer is None:
            var_x = self.data[0]
            for i in range(1, self.size):
                var_x = reduce_func(var_x, self.data[i])

            return var_x

        # If initalizer is provided, insert at first value before applying reduce function then remove.
        else:
            self.insert_at_index(0, initializer)

            var_x = self.data[0]
            for i in range(1, self.size):
                var_x = reduce_func(var_x, self.data[i])

            self.remove_at_index(0)

            return var_x


# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOUCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
