from typing import List


def rec_sum(nums: List[int]) -> int:
    s = 0
    if len(nums) > 0:
        s += nums.pop()
        s += rec_sum(nums)

    return s


print(rec_sum([1, 2, 5]))
print(rec_sum([1, 2, 3]))
print(rec_sum([]))
