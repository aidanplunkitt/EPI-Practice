from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n == 0: return ''
    if n == 1: return '1'
    if n == 2: return '11'
    
    a, b = [], [1, 1]
    j = 1
    for _ in range(n-2):
        a, b = b, []
        j = 1
        for i in range(1,len(a)):
            if a[i] == a[i-1]:
                j += 1
            else:
                b.extend([j, a[i-1]])
                j = 1
        b.extend([j, a[-1]])

    return ''.join(str(x) for x in b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
