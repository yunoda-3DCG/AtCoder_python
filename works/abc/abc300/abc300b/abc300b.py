import numpy

h, w = map(int, input().split())
As = [list(input()) for i in range(h)]
Bs = [list(input()) for i in range(h)]

isSuit = False
for j in range(w):
    for i in range(h):
        temp = numpy.roll(As, (j, i), axis=(1, 0))
        if numpy.array_equal(temp, Bs):
            isSuit = True
            break

    if isSuit:
        break

if isSuit:            
    print('Yes')
else:
    print('No')
