# 이진수 뎃셈

a, b = map(str, input().split())
a, b = int(a, 2), int(b, 2)
print(a, b)
result = bin(a + b)
print(result[2:])