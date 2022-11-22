n = int(input())

for i in range(2 ** n)):
    result = ""
    sum = 0
    for j in reversed(range(n)):
        if ((i >> j) & 1):
            sum -= 1
            result += ")"
        else:
            sum += 1
            result += "("
        
        if sum < 0:
            break

    if sum == 0:
        print(result)

if n % 2 == 1:
    print("")
