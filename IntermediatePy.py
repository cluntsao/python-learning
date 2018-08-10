def main():
    """ *args, **kwargs """

    def test_var_args(f_arg, *args):
        print(f_arg)
        for arg in args:
            print(arg)

    test_var_args('yoman', 'python', 'crack', 'the', 'interview')

    def test_for_kwargs(**kwargs):
        for k, v in kwargs.items():
            print("{} = {}".format(k, v))

    test_for_kwargs(name = "John", number = 5, sex = "M")

    """ Map, Filter, Reduce """

    # Map
    items = [1, 2, 3, 4, 5]

    print(list(map(lambda x: x**2, items)))
    print()

    func1 = lambda x: x**2
    func2 = lambda x: x*2
    funcs = [func1, func2]

    for item in items:
        val = list(map(lambda x: x(item), funcs))
        print(val)

    # Filter
    print()
    print(list(filter(lambda x: x > 0, range(-5, 5))))
    print(list(filter(lambda c: ord(c) > ord('d'), "abcdstring")))

    # Reduce
    from functools import reduce
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))

    """ Ternary Operations """
    fat = True
    fitness = ("skinny", "fat")[fat]
    print("Ali is ", fitness)

    """ Decorator """
    def hi(name="yasoob"):
        return "hi " + name

    print(hi())
    # output: 'hi yasoob'

    # We can even assign a function to a variable like
    greet = hi
    # We are not using parentheses here because we are not calling the function hi
    # instead we are just putting it into the greet variable. Let's try to run this

    print(greet())
    # output: 'hi yasoob'

    # Let's see what happens if we delete the old hi function!
    """ del hi
    print(hi()) """
    #outputs: NameError

    print(greet())
    #outputs: 'hi yasoob'


    # Returning functions from within functions:
    def hi(name="yasoob"):
        def greet():
            return "now you are in the greet() function"

        def welcome():
            return "now you are in the welcome() function"

        if name == "yasoob":
            return greet
        else:
            return welcome

    a = hi()
    print(a)
    #outputs: <function greet at 0x7f2143c01500>

    #This clearly shows that `a` now points to the greet() function in hi()
    #Now try this

    print(a())
    #outputs: now you are in the greet() function

    from functools import wraps
    def decorator_name(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not can_run:
                return "Function will not run"
            return f(*args, **kwargs)
        return decorated

    @decorator_name
    def func():
        return "Function is running!"

    can_run = True
    print(func())

    can_run = False
    print(func())

    """ Use Cases:

        Logging
     """

    def logit(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            print(func.__name__ + " was called")
            return func(*args, **kwargs)
        return with_logging

    @logit
    def addition_func(x):
        """Do some math."""
        return x + x    


    result = addition_func(4)
    # Output: addition_func was called
    print(result)

    from collections import Counter
    favs = Counter(item for item in [1, 1, 1, 1, 1, 2, 3])
    print(favs)

    print(dir(object))
    

if __name__ == '__main__':
    main()