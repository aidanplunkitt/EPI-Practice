from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    def get_distance(x, y):
        if dp[x][y] < 0:
            if x == 0:
                return y
            if y == 0:
                return x

            # if letters are equal, continue to submatrix without adding
            if A[x-1] == B[y-1]:
                dp[x][y] = get_distance(x-1, y-1)
            else:  # get min of add/delete/edit
                dp[x][y] = min(get_distance(
                    x-1, y), get_distance(x, y-1), get_distance(x-1, y-1)) + 1

        return dp[x][y]

    dp = [[-1 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    val = get_distance(len(A), len(B))
    return val


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
