class Empty(Exception):
    pass

class LinkedQueue:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, item):
        newest = self._Node(item, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1

def main():
    obj = LinkedQueue()
    obj.enqueue(12)
    obj.enqueue(13)
    print(obj.dequeue())

if __name__ == '__main__':
    main()