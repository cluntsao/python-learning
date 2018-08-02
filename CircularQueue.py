class Empty(Exception):
    pass

class CircularQueue:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._size = 0
        self._tail = None
        
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty!!!")
        return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty!!!")

        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, item):
        newest = self._Node(item, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._size += 1
        self._tail = newest

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next