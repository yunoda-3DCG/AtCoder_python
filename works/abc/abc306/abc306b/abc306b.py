As = list(map(int, input().split()))

sum = 0
for i in range(len(As)):
    sum += As[i] * 2**i 

print(sum)