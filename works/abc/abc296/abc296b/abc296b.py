count = 0
row = ['8', '7', '6', '5', '4', '3', '2', '1']
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
while count < 8:
    target = list(input())
    for i in range(8):
        if target[i] == '*':
            print(column[i] + row[count])
            break
    count += 1