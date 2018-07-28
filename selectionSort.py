import random

def selectionSort(A):
  sorted = []
  length = len(A)
  i = 0
  while i < length - 1:
    mininum = min(A)
    A.pop(A.index(mininum))
    sorted.append(mininum)
    i+=1
  
  return sorted + A

def main():
    # length of array
    s = random.randint(5, 1000)
    # random array
    A = [random.randint(1, 1000) for i in range(s)]
    print("original array: {}".format(A))
    print()
    print("sorted array: {}".format(selectionSort(A)))

if __name__ == "__main__":
    main()