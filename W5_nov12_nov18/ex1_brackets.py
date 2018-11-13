def is_correct(expr):
    stack = []
    closing = {"(": ")", "{": "}", "[": "]"}
    op = closing.keys()
    cl = closing.values()

    for c in expr:
        if c in cl:
            if not stack or closing[stack[-1]] != c:
                return False
            stack.pop()
        if c in op:
            stack.append(c)
    if not stack:
        return True


expr = input()
print("true" if is_correct(expr) else "false")
