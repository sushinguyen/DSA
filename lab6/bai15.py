def sort_stack(stack):
    aux = []

    while stack:
        tmp = stack.pop()
        while aux and aux[-1] > tmp:
            stack.append(aux.pop())
        aux.append(tmp)

    while aux:
        stack.append(aux.pop())

    return stack


s1 = [3, 1, 2]
print(sort_stack(s1))

s2 = [5, 1, 4, 2, 3]
print(sort_stack(s2))

s3 = [1]
print(sort_stack(s3))
