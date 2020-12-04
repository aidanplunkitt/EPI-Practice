from typing import List

from test_framework import generic_test

# 16.1, O(k*n) time, O(n) space
def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    ways_to_reach_score = [1] + [0] * final_score

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            if j - individual_play_scores[i] >= 0:
                ways_to_reach_score[j] += ways_to_reach_score[j - individual_play_scores[i]]

    return ways_to_reach_score[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
