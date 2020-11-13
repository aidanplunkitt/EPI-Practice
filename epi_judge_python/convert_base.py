from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    i = 0
    signed = False

    if num_as_string == '0': return num_as_string    
    if num_as_string[0] == '+':
        i = 1
    elif num_as_string[0] == '-':
        signed = True
        i = 1
    
    x = 0
    while i < len(num_as_string):
        tmp = 0
        if num_as_string[i] in 'ABCDEF':
            tmp = 10 + ord(num_as_string[i]) - ord('A')
        else:
            tmp = int(num_as_string[i])
        x = x * b1 + tmp
        i += 1

    #convert from base 10 to b2
    result = ''
    while x:
        x, digit = divmod(x, b2)
        if digit > 9:
            digit = chr(ord('A') + digit - 10)
        else:
            digit = str(digit)
        result += digit

    result = ('-' if signed else '') + result[::-1]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
