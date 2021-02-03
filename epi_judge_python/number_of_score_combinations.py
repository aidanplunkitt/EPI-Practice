from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # R, C = len(individual_play_scores), final_score + 1
    # # dp = [[0 for _ in range(C)] for _ in range(R)]
    # dp = [0 for _ in range(C)]
    # dp[0] = 1

    # for i, score in enumerate(individual_play_scores):
    #     for j in range(1, final_score + 1):
    #         if j >= score and dp[j-score]:
    #             dp[j] += 1

    # print(dp)

    # return dp[-1]
    dp = [1] + [0 for _ in range(final_score)]

    for score in individual_play_scores:
        for j in range(1, final_score + 1):
            if j >= score and dp[j-score]:
                dp[j] += dp[j-score]

    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
