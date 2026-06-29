def eval_rpn(expression):
    stack = []
    operators = {
        lambda a, b: a + b,
        lambda a, b: a - b,
        lambda a, b: a * b,
        lambda a, b: int(a / b),  # chia lấy phần nguyên
    }

    for token in expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(int(token))

    return stack[0]


# Test
print(eval_rpn("3 4 + 2 *"))     
print(eval_rpn("5 1 2 + 4 * + 3 -"))  
print(eval_rpn("2 3 * 4 5 * +"))   
print(eval_rpn("10 2 /"))          