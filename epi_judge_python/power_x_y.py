from test_framework import generic_test


def power(x: float, y: int) -> float:
    result = 1.0

    # handle negative powers here to simplify loop logic
    if y < 0:
        x = 1.0 / x
        y *= -1

    while y:
        if y & 1: result *= x
        x *= x
        y >>= 1
        
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
