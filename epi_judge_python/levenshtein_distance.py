from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    dp[0] = [n for n in range(len(B) + 1)]

    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            if j == 0:
                dp[i][j] = i
            else:
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
