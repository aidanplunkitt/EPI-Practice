from test_framework import generic_test

# 16.2, O(ab) time, O(min(a,b)) space
def levenshtein_distance(A: str, B: str) -> int:
    # for min(A,B) space
    if len(A) < len(B):
        A, B = B, A
    distances = list(range(len(B)+1))
    for A_idx in range(1, len(A)+1):
        diag = distances[0]
        distances[0] = A_idx
        for B_idx in range(1, len(B)+1):
            next_diag = distances[B_idx]
            if B[B_idx - 1] == A[A_idx - 1]:
                distances[B_idx] = diag
            else: 
                distances[B_idx] = 1 + min(diag, distances[B_idx], distances[B_idx - 1]) # diag, up, left
            diag = next_diag
    return distances[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
