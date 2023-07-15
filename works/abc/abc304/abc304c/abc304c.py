n, d = map(int, input().split())

class person:
    pos_x = 0
    pos_y = 0
    isInfected = False

    def __init__(self, x, y, state):
        self.pos_x = x
        self.pos_y = y
        self.isInfected = state

people_origin = []
isInfected = []
for i in range(n):
    x, y = map(int, input().split())
    people_origin.append(person(x, y, False))

isInfecting = True
people_origin[0].isInfected = True
carrier = [people_origin[0]]
people = people_origin.copy()
people.remove(people_origin[0])
counter = 0
carrier_next = []
while isInfecting and counter < 1000:
    carrier_next.clear()
    for c in carrier:
        for p in people:
            if d**2 >= (c.pos_x - p.pos_x)**2 + (c.pos_y - p.pos_y)**2:
                if not p.isInfected:
                    p.isInfected = True
                    people.remove(p)
                    carrier_next.append(p)
    if len(carrier_next) == 0:
        isInfecting = False
    else:
        carrier = carrier_next.copy()
    counter += 1

for p in people_origin:
    print('Yes' if p.isInfected else 'No')