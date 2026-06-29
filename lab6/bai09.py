def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack  = []

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token not in precedence and token not in '()':
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # bỏ '('

        else:  # toán tử
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


print(infix_to_postfix("a+b*c"))
print(infix_to_postfix("a+b*c-d"))
print(infix_to_postfix("(a+b)*c"))
print(infix_to_postfix("a*(b+c)-d/e"))
print(infix_to_postfix("(a+b)*(c-d)"))