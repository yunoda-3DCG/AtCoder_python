n = int(input())
s = list(input())

pipes = [i for i, x in enumerate(s) if x == '|']
asterisk = s.index('*')

if pipes[0] < asterisk and asterisk < pipes[1]:
    print('in')
else:
    print('out')