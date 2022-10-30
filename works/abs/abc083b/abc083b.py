n, a, b = map(int, input().split())

result = 0
for i in range(1, n+1):
    num = []
    origin = i
    while origin != 0:
        num.append(origin % 10)
        origin /= 10
    num.reverse()

    sum = 0
    for t in range(len(num)):
        sum += int(num[t])

    if a <= sum and sum <= b:
        result += i

print(result)