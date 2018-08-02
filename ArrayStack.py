class Empty(Exception):
    pass

class ArrayStack:
    """LIFO Stack implementation using Python list as underlying storage"""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        return self._data.append(item)

    def top(self):
        """return but not move the element at the top of the stack"""
        if len(self._data) == 0:
            raise Empty("Stack is empty!")

        return self._data[-1]

    def pop(self):
        if len(self._data) == 0:
            raise Empty("Stack is empty!")

        return self._data.pop()