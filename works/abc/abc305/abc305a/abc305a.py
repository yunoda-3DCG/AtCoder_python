n = int(input())
result = 0
if n % 5 < 3:
    result = (n//5)*5
else:
    result = (n//5 + 1)*5

print(*result(sep = ''))