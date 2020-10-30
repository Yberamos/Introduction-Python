# _*_ coding:Utf8 _*_
print("Suite de Fibonacci")

a, b, c = 1, 1, 1

print(b)
while c < 15:
    a, b, c = b, a+b, c+1
    print(b)
