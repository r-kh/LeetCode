from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        indexes = []
        for i in range(len(nums)):
            num = nums[i]
            if num <= target:
                dif = target - num
                if dif in my_list:
                    return List[i, indexes[my_list.index(dif)]]
                else:
                    my_list.append(num)
                    indexes.append(i)