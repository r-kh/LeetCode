class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            s = str(x)
            if s[::-1] == s:
                return True
        return False


s = Solution()
result = s.isPalindrome(121)
print(result)
