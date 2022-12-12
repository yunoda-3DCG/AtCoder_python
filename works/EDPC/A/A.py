n = int(input())
h = list(map(int, input().split()))

dp = [[0] for i in range(n)]

dp[0] = 0
dp[1] = h[1] - h[0]
for i in range(1, len(dp)):
    cost = min(sum(dp[i-1], abs(h[i] - h[i-1])), sum(dp[i-2], abs(h[i] - h[i-2])))
    dp[i] = cost

print(dp[len(dp)-1])