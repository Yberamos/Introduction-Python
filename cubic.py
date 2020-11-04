def volBoite(x=-1, y=-1, z=-1):
    if x == -1:
        return -1
    elif y == -1 :
        return x**3
    elif z == -1:
        return x*x*y
    else:
        return x*y*z


print(volBoite())
print(volBoite(5.2))
print(volBoite(5.2, 3))
print(volBoite(5.2, 3, 7.4))
