class Empty(Exception):
    pass

class Deque:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._first = 0
        self._last = 0
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._n = 0

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def first(self):
        return self._data[self._first]

    def last(self):
        return self._data[self._last]

    def delete_first(self):
        if self._n == 0:
            raise Empty("Deque is empty!!!")

        answer = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % len(self)
        self._n -= 1

        return answer

    def delete_last(self):
        if self._n == 0:
            raise Empty("Deque is empty!!!")

        answer = self._data[self._last]
        self._data[self._last] = None
        self._last = (self._last - 1 + len(self)) % len(self)
        self._n -= 1

        return answer

    def add_first(self, item):
        if self._n == len(self._data):
            self._resize(2 * len(self._data))

        if self._n == 0:
            self._data[self._first] = item
            self._n += 1
        else:
            self._first = (self._first - 1 + len(self._data)) % len(self._data)
            self._data[self._first] = item
            self._n += 1

    def add_last(self, item):
        if self._n == len(self._data):
            self._resize(2 * len(self._data))

        if self._n == 0:
            self._data[self._last] = item
            self._n += 1
        else:
            self._last = (self._last + 1) % len(self._data)
            self._data[self._last] = item
            self._n += 1

    def _resize(self, c):
        old = self._data
        self._data = [None] * c
        walk = self._first
        for i in range(self._n):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)

def main():
    D = Deque()
    D.add_last(5)
    print(D._data)
    D.add_first(3)
    print(D._data)
    D.add_first(7)
    print(D._data)
    print(D.first())
    print(D.delete_last())
    print(len(D))
    print(D._data)
    print(D.delete_last())


if __name__ == '__main__':
    main()