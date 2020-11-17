from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    class MaxWithCount:
        def __init__(self, val, count):
            self.val, self.count = val, count

    def __init__(self):
        self._elements = []
        self._max_stack = []
    
    def empty(self) -> bool:
        return len(self._elements) == 0

    def max(self) -> int:
        if self.empty(): 
            raise IndexError("called max() on empty stack")
        return self._max_stack[-1].val

    def pop(self) -> int:
        if self.empty():
            raise IndexError("called pop() on empty stack")

        val = self._elements[-1]
        currmax = self._max_stack[-1].val
        if val == currmax:
            if self._max_stack[-1].count > 1:
                self._max_stack[-1].count -= 1
            else:
                self._max_stack.pop()
        self._elements.pop()

        return val

    def push(self, x: int) -> None:
        if len(self._max_stack) > 0:
            currmax = self._max_stack[-1].val
            if x > currmax:
                self._max_stack.append(self.MaxWithCount(x, 1))
            elif x == currmax:
                self._max_stack[-1].count += 1
        else:
            self._max_stack.append(self.MaxWithCount(x, 1))
        self._elements.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
