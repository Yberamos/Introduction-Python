def maximum (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    else:
        return n3


print(maximum(2, 5, 4))
