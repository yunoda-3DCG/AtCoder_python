n = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def GetDuplicationCount(target):
    tmp = list(set(target))
    result = 1
    for i in range(len(tmp)):
        result *= 1 + target.count(tmp[i])
    return result

index = 1
result = 0

while index < n:
    primes_R = prime_factorize(index)
    primes_L = prime_factorize(n - index)
    result += GetDuplicationCount(primes_L) * GetDuplicationCount(primes_R)
    index += 1

print(result)