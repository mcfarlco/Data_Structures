# Name: Corey McFarland

class _bagIterator:
    def __init__(self, theList):
        self._listItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Method to return double the amount of the next item in the container.
        """

        if self._curItem == len(self._listItems) - 1:
            self._curItem = 0
            return

        self._curItem += 1
        node = self._listItems[self._curItem]

        return node * 2
