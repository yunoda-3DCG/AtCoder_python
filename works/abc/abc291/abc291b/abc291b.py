n = int(input())
x = list(map(int, input().split()))

x.sort()
del x[:n]
del x[-n:]

average = sum(x) / len(x)
print(average)