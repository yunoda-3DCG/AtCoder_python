n, t = map(int, input().split())
a = list(map(int, input().split()))

total = 0
for i in range(n):
    total += a[i]

time = t % total
num = 0
while time > a[num]:
    time -= a[num]
    num += 1
    if num + 1 > n:
        num = 0

print(str(num + 1) + " " + str(time))