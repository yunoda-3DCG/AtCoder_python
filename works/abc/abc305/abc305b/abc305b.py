p, q = map(str, input().split())

distance = [3, 1, 4, 1, 5, 9]

def GetIndex(text):
    if text == 'A':
        return 0
    elif text == 'B':
        return 1
    elif text == 'C':
        return 2
    elif text == 'D':
        return 3
    elif text == 'E':
        return 4
    elif text == 'F':
        return 5
    elif text == 'G':
        return 6

result = 0
first = min(GetIndex(p), GetIndex(q))
second = max(GetIndex(p), GetIndex(q))
for i in range(first, second):
    result += distance[i]

print(result)