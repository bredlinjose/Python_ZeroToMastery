def is_balanced(exp):
    stack = []
    for x in exp:
        if x in ['(', '{', '[']:
            stack.append(x)
            continue

        if not stack:
            return False

        if x == ')':
            if stack[-1] != '(':
                return False
            stack.pop()
        elif x == '}':
            if stack[-1] != '{':
                return False
            stack.pop()
        elif x == ']':
            if stack[-1] != '[':
                return False
            stack.pop()

    return not stack


expression = "(){}{[]}(]"
if is_balanced(expression):
    print("Balanced Bracket")
else:
    print("Not Balanced Bracket")
