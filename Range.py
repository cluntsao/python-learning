class Range:

    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k+=self._length

        if not 0 <= k < self._length:
            raise IndexError("out of index")
        
        return self._start + (k * self._step)

def main():
    myR = Range(9)
    print(len(myR))
    print(myR[5])

    for i in myR:
        print(i)

if __name__ == '__main__':
    main()