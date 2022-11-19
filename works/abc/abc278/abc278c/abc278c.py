n, q = map(int, input().split())
t = []
followeesOnUser = []

class Followees:
    global users
    
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)
        self.users = list(set(self.users))

    def delete(self, user):
        try:
            self.users.remove(user)
        except ValueError:
            pass

    def isFollowing(self, user):
        return user in self.users

for i in range(q):
    t.append(list(map(int, input().split())))

for i in range(n):
    followeesOnUser.append(Followees())

for i in range(q):
    if t[i][0] == 1:
        followeesOnUser[t[i][1]-1].add(t[i][2])
    elif t[i][0] == 2:
        followeesOnUser[t[i][1]-1].delete(t[i][2])
    elif t[i][0] == 3:
        if followeesOnUser[t[i][1]-1].isFollowing(t[i][2]) and followeesOnUser[t[i][2]-1].isFollowing(t[i][1]):
            print("Yes")
        else:
            print("No")