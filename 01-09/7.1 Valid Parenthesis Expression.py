def valid_parenthesis_expression(s: str) -> bool:
    stack = []
    hashmap = {'(': ')', '{':'}', '[':']'}

    for c in s:
        # opening or closing
        if c in hashmap:
            stack.append(c)
        else:
            # check if stack non empty and matches last opening bracket
            if stack and hashmap[stack[-1]] == c:
                stack.pop()
            else:
                return False

    return not stack