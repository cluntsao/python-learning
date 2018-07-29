def main():
    arr = [1, 2, 3, 4, 5, 6]
    
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
    


if __name__ == '__main__':
    main()