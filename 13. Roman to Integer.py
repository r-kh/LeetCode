class Solution:

    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arr = list(s)
        target = 0
        i = 0
        while i < len(arr):

            if len(arr) == i + 1:
                return target + dict[arr[i]]

            first_num = dict[arr[i]]
            second_num = dict[arr[i + 1]]

            if second_num > first_num:
                target += second_num - first_num
                i += 2
            else:
                target += first_num
                i += 1
        return target


s = Solution()
result = s.romanToInt("MCMXCIV")
print(result)
