class Progression:
    """Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start = 0):
        self._current = start

    def _advance(self):
        """ Update self._current to a new value

        This shoudl be overriden by a subclass to customize progression

        By convention, if current is set to None, this designates the end of a finite progression
        """

        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""

        return self

    def print_progression(self, n):
        print(" ".join(str(next(self)) for j in range(n)))

def main():
    p1 = Progression()
    p1.print_progression(10)          # 0 1 2 3 4 5 6 7 8 9

if __name__ == '__main__':
    main()