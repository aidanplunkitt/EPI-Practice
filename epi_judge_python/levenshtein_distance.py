from test_framework import generic_test

# 16.2, O(ab) time and space
def levenshtein_distance(A: str, B: str) -> int:
    def compute_distance(a, b):
        if a < 0:
            return b + 1
        elif b < 0:
            return a + 1

        if matrix[a][b] == -1:
            if A[a] == B[b]:
                matrix[a][b] = compute_distance(a-1, b-1)
            else:
                replace = compute_distance(a-1, b-1) # swap val in B for val in A (B[b] = A[a])
                add     = compute_distance(a-1, b) # add A[a] to B (insert at B[b+1])
                delete  = compute_distance(a  , b-1) # delete from B (remove B[b])
                matrix[a][b] = min(replace, add, delete) + 1
        return matrix[a][b]

    matrix = [[-1] * len(B) for _ in A]
    return compute_distance(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
