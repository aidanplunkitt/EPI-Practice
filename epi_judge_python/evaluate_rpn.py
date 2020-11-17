from test_framework import generic_test


def evaluate(expression: str) -> int:
    nums = []
    tokens = expression.split(",")
    for t in tokens:
        if t.isnumeric():
            nums.append(int(t))
        else:
            a = nums.pop()
            b = nums.pop()
            if t == '*':
                nums.append(a * b)
            elif t == '+':
                nums.append(a + b)
            else:
                raise ValueError("Invalid token")

    return nums.pop()



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
