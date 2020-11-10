from test_framework import generic_test


def power(x: float, y: int) -> float:
    result = 1.0

    if y == 0:
        pass
    elif y > 0:
        while y:
            if y & 1: result *= x
            x *= x
            y >>= 1
    else:
        y *= -1
        while y:
            if y & 1: result /= x
            x *= x
            y >>= 1
        
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
