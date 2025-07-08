from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            dif = target - num
            if dif in dict:
                return [i, dict[dif]]
            dict[num] = i


s = Solution()
result = s.twoSum([-3, 4, 3, 90], 0)
print(result)