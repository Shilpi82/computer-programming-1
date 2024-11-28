#Basic Calculator
def calculate(s: str) -> int:
    stack, sign, num = [], 1, 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in '+-':
            stack.append(sign * num)
            sign = 1 if c == '+' else -1
            num = 0
        elif c == '(':
            stack.append('(')
        elif c == ')':
            stack.append(sign * num)
            num = 0
            result = 0
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # Remove '('
            stack.append(result)
    return sum(stack) + num
