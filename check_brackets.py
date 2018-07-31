# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def test(text):
        opening_brackets_stack = []
        for i, next in enumerate(text):
            if next == '(' or next == '[' or next == '{':
                # Process opening bracket, write your code here
                opening_brackets_stack.append(Bracket(next, i))

            if next == ')' or next == ']' or next == '}':
                # Process closing bracket, write your code here
                if opening_brackets_stack[len(opening_brackets_stack) - 1].Match(next):
                    opening_brackets_stack.pop()
                else:
                    return (i + 1)

        # if len(opening_brackets_stack) != 0:
        #     return (opening_brackets_stack[len(opening_brackets_stack) - 1].position + 1)

        return "Success"

if __name__ == "__main__":
    # text = sys.stdin.read()

    # opening_brackets_stack = []
    path = 'D:/PyDataStructures/check_brackets_in_code/tests/32'
    with open(path) as f:
        print(f.read())
        text = (f.read())

    text1 = "({()(})"

    print(test(text))
    print(test(text1))

    