def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['
    righty = ')}]'

    lefty_stack = []

    for char in expr:
        if char in lefty:
            lefty_stack.append(char)
        elif char in righty:
            if len(lefty_stack) == 0:
                return False
            elif righty[lefty.index(lefty_stack[-1])] == char:
                lefty_stack.pop()


    return len(lefty_stack) == 0

def main():
    text = ["()(()){([()])}", "((( )(( )){([( )])}))", ")(( )){([( )])}", "({[ ])}", "("]

    for i in text:
        print(is_matched(i))

if __name__ == '__main__':
    main()
