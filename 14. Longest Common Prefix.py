class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = ('(', '{', '[')
        closed_brackets = (')', '}', ']')

        if len(s) <= 1 or s.startswith(closed_brackets):
            return False

        my_str = s[0]
        i = 1
        while i < len(s):
            bracket = s[i]
            if bracket in closed_brackets:
                if len(my_str) == 0:
                    return False
                index = closed_brackets.index(bracket)
                if open_brackets[index] == my_str[-1]:
                    my_str = my_str[:-1]
                else:
                    return False
            else:
                my_str += bracket
            i += 1

        return my_str == ""


s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("([])"))

# как в реальном мире ?
# строка пустая или в ней 1 символ - False

# пробегаемся по строке
# открытая скобка в начале ?
#   нет - False

#   да,
#       есть следующая ?
#           да
#               она открытая ?
#                   нет
#                       она может закрыть стоящую перед ней ?
#                           нет - False

#                           да - убираем обе

#           нет
#               вернуть равнали строка ""


# если скобка открылась, то её можно либо закрыть парой и удалить, либо открыть новую такую-же функцию и ожидать что она закроется
