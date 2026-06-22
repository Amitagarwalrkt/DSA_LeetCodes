class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i, n = 0, len(s)

        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0


        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

           
            if sign * num < INT_MIN:
                return INT_MIN
            if sign * num > INT_MAX:
                return INT_MAX

        return sign * num