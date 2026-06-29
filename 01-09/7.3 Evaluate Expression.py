def evaluate_expression(s: str) -> int:
    res, curr_num, sign = 0, 0, 1
    stack = []

    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)

        elif c == '+' or c == '-':
            res += curr_num * sign
            curr_num = 0
            sign = -1 if c == '-' else 1

        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1

        elif c == ")":
            res += sign * curr_num
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0

    return res + curr_num * sign