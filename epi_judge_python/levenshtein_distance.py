from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    # ensure O(min(A,B)) space
    if len(A) < len(B):
        A, B = B, A

    # initialize first row
    dp = [n for n in range(len(B) + 1)]

    for i in range(1, len(A) + 1):
        # initialize first col
        diag = dp[0]
        dp[0] = i
        for j in range(1, len(dp)):
            up, left = dp[j], dp[j-1]
            if A[i-1] == B[j-1]:
                # curr[j] = last[j-1]
                dp[j] = diag
            else:
                # curr[j] = min(curr[j-1], last[j], last[j-1]) + 1
                dp[j] = min(up, left, diag) + 1

            diag = up

    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
