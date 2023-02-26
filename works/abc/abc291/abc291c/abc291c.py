n = int(input())
s = list(str(input()))
p = []

def GetPos(code: str):
    return [code[0:7], code[7:14]]

def GetCode(x: int, y: int):
    code = str(x).zfill(7) + str(y).zfill(7)
    return code

p.append('00000000000000')
for i in range(n):
    prevPos = GetPos(p[i])
    if s[i] == 'R':
        p.append(GetCode(int(prevPos[0]) + 1,  int(prevPos[1])))
    elif s[i] == 'L':
        p.append(GetCode(int(prevPos[0]) - 1,  int(prevPos[1])))
    elif s[i] == 'U':
        p.append(GetCode(int(prevPos[0]),  int(prevPos[1]) + 1))
    elif s[i] == 'D':
        p.append(GetCode(int(prevPos[0]),  int(prevPos[1]) - 1))

if len(p) != len(set(p)):
    print("Yes")
else:
    print("No")