import random

def main():
    arr = [1, 2, 3, 4, 5, 6]

    def demo(first_arg, *args):
        print("first argument: \n{}".format(first_arg))
        for arg in args:
            print(arg)

    demo("1", "2", "3", "4")

    def demo2(**kwargs):
        for k, v in kwargs.items():
            print(k, v)

    demo2(name = "John")
    
    string = "string"

    print([char + "%" for char in string])

    total = ""
    for ele in [char + "%" for char in string]:
        total+=ele

    newMap = map(lambda x: x**2, arr)
    print(next(newMap))
    print(next(newMap))

    print(string[::-1])

    print(sorted([23, 54,112, 1, 9, 3], reverse=True))

    # with open('d:/sample1.txt', encoding='utf8') as f:
        
    #     print(f.read())

    if isinstance(9.8, (int, float)):
        print("Wrong")

    def factor(n):
        for k in range(1, n+1):
            if k % 2 == 0:
                yield k

    # Fast if else
    param = 1 if 3 > 0 else 6
    print(param)
    
    # packing & unpacking
    a, b = divmod(7, 2)
    print(a, b)
    print("========================")
    for x, y in [(7, 2), (5, 8), (6, 4)]:
        print(x, y)

    print([0] * 8)

    """ print('index', 'value')
    for idx, val in enumerate([23, 24, 25, 26]):
        print("{:2d}      {:3d}".format(idx, val)) """

    mask = (1 << 32) - 1
    h = 0
    h += ord('l')
    print((h << 5 & mask) | (h >> 27))
    print(0 >> 1)

    print(hash((1, 4)))

if __name__ == '__main__':
    main()