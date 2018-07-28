#  SelectionSort
from math import floor
import random

def merge(A, p, q, r):
  arr1 = A[p:q+1]
  arr2 = A[q+1:r+1]

  i = 0
  j = 0

  arr1.append(10000000)
  arr2.append(10000000)

  for k in range(p, r+1):
    if(arr1[i] >= arr2[j]):
      A[k] = arr2[j]
      j+=1
    else:
      A[k] = arr1[i]
      i+=1

  # return A

def mergeSort(A, p, r):
  if p < r:
    q = floor((p + r) / 2)

    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)

def main():
  s = random.randint(5, 100)
  A = [random.randint(0, 1000) for i in range(s)]
  print("Original Array: {}".format(A))
  mergeSort(A, 0, len(A) - 1)
  print()
  print("sorted Array: {}".format(A))

if __name__ == "__main__":
  main()