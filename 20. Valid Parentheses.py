class Solution:

    # Используем стек.
    #
    # Добавляем открывающие скобки в стек. При встрече закрывающей — сверяем с вершиной стека. Если не совпадает — скобки некорректны.
    #
    # - Time complexity:
    # O(n)
    # - Space complexity:
    # O(n)

    def isValid(self, s: str) -> bool:

        open_brackets = ('(', '{', '[')
        closed_brackets = (')', '}', ']')

        pairs = {'(':')', '[':']', '{':'}'}

        if len(s) <= 1 or s.startswith(closed_brackets):
            return False

        stack = []

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            elif not stack:
                return False
            else:
                if bracket == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return not stack

# s = Solution()
# print(s.isValid("()"))
# print(s.isValid("(]"))
# print(s.isValid("([])"))
# print(s.isValid("(){}}{"))
