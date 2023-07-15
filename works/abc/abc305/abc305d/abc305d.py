n = int(input())
As = list(map(int, input().split()))
q = int(input())
Ls = [list(map(int, input().split())) for i in range(q)]

def GetSleepTime(endtime):
    sum = 0
    index = 0
    while As[index] < endtime:
        if endtime < As[index+1]:
            time = endtime - As[index]
        else:
            time = As[index+1] - As[index]
        
        if index % 2 == 1:
            sum += time
        else:
            pass
        
        index += 1

    return sum

for quiz in Ls:
    print(GetSleepTime(quiz[1]) - GetSleepTime(quiz[0]))