from _DoubleLinkedBase import _DoubleLinkedBase

class Empty(Exception):
    pass

class LinkedDeque(_DoubleLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty!!!")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty!!!")
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty!!!")
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty!!!")
        self._delete_node(self._trailer._prev)

def main():
    obj = LinkedDeque()
    obj.insert_first(5)
    obj.insert_last(6)
    print(obj.last())
    obj.insert_first(7)
    print(obj.last())
    print(obj.first())

if __name__ == '__main__':
    main()
