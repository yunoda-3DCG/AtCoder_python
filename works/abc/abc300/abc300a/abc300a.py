n, a, b = map(int, input().split())
value = a + b
 
Cs =  list(map(int, input().split()))
for index, c in enumerate(Cs):
    if c == value:
        print(index+1)
        break