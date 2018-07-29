class SequenceIterator:
    """An iterator for any of Python's sequence types"""
    def __init__(self, sequence):
        self._seq = sequence     # keep a reference to the underlying data
        self._k = -1             # will increment to 0 on first call to next

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __len__(self):
        return len(self._seq)

    def __iter__(self):
        """ By convention, an iterator must return itself as an iterator """
        return self

def main():
    seq = SequenceIterator([1, 2, 3])
    
    print(len(seq))

    for i in seq:
        print(i)

if __name__ == '__main__':
    main()