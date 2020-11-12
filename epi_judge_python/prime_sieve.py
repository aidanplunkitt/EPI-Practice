from typing import List
import math

from test_framework import generic_test

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # def isprime(i):
    #     return True
    
    # return [i for i in range(2, int(math.sqrt(n))) if isprime(i)]
    nums = list(range(1, n+1))

    i = 1
    while i < len(nums):
        num = nums[i]
        tmp = num + num
        while tmp <= n:
            if tmp in nums: nums.remove(tmp)
            tmp += num
        i += 1
        

    # remove first element (1) from results
    return nums[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
