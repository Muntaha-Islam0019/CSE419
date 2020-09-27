class py_solution:
    def is_valid_parenthese(self, a_string):

        stack = []
        parentheses = {"(": ")", "{": "}", "[": "]"}

        for parenthese in a_string:
            if parenthese in parentheses:
                stack.append(parenthese)
            elif len(stack) == 0 or parentheses[stack.pop()] != parenthese:
                return False

        return len(stack) == 0


print(py_solution().is_valid_parenthese("{[[()]]{}}"))
