import sys
import ctypes # provides low-level arrays

"""Demostrate the list class of Python

data = []
for k in range(50):
    a = len(data)
    b = sys.getsizeof(a)
    print("Length {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)
"""

class DynamicArray:   # aka simplified list in Python

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def __setitem__(self, j, item):
        self._A[j] = item

    def append(self, item):
        if self._n == self._capacity:
            self._resize()
        self[self._n] = item
        self._n += 1

    def _resize(self):
        
        B = self._make_array(self._capacity * 2)
        for i in range(self._capacity):
            B[i] = self[i]

        self._A = B
        self._capacity *= 2

    def _make_array(self, c):
        return (c * ctypes.py_object)()

arr = DynamicArray()

for i in range(12):
    arr.append(i)
print(arr[1])