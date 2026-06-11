class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        i = 0
        n = len(s)

        while i < n:
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                continue

            elif s[i] == '+':
                sign = 1

            elif s[i] == '-':
                sign = -1

            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif s[i] == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result

            i += 1

        return result