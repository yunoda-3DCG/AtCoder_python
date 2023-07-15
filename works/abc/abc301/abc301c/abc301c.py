s = list(input())
t = list(input())

isWin = True
wild_s = s.count('@')
wild_t = t.count('@')

for i in range(97, 123):
    c = chr(i)
    dif = s.count(c) - t.count(c)
    if dif != 0:
        if (    c == 'a'
             or c == 't' 
             or c == 'c' 
             or c == 'o'
             or c == 'd'
             or c == 'e'
             or c == 'r'):
            if dif < 0:
                wild_s -= abs(dif)
            elif dif > 0:
                wild_t -= abs(dif)

            if wild_s < 0 or wild_t < 0:
                isWin = False
                break
        else:
            isWin = False
            break

print('Yes' if isWin else 'No')