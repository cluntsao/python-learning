def main():
    
    def fibonacci(n):
        a = 0
        b = 1
        for _ in range(n):
            yield a
            future = a + b
            a = b
            b = future

    
    print([i for i in fibonacci(10)])
    print([i for i in fibonacci(20)])


if __name__ == '__main__':
    main()