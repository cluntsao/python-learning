from PositionalList import PositionalList

class FavoritesList:
    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, v):
            self._value = v
            self._count = 0

    def _find_position(self, e):
        """ Search for element e and return its Position """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """ Move item at Position p earlier in the list based on access count """
        if p != self._data.first():
            walk = self._data.before(p)
            cnt = p.element()._count
            if cnt > walk.element()._count:
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    """ ==================================Public Methods==================================== """

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data.is_empty()

    def access(self, e):
        """ Access element e, thereby increasing its access count """
        p = self._find_position(e)

        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for _ in range(k):
            item = walk.element()._value
            yield item
            walk = self._data.after(walk)