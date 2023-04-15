s = list(input())

first_B = -1
second_B = -1
first_R = -1
second_R = -1
first_K = -1
for index, i in enumerate(s):
    if i == 'B':
        if first_B == -1:
            first_B = index
        else:
            second_B = index
    elif i == 'R':
        if first_R == -1:
            first_R = index
        else:
            second_R = index
    elif i == 'K':
        first_K = index
if (first_B + second_B) % 2 == 1 and first_R < first_K and first_K < second_R:
    print('Yes')
else:
    print('No')