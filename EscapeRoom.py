from pythonds.basic.stack import Stack


# Read input file
class Node:
    def __init__(self):
        self.coordination = []
        self.nextnodelist = []  # Coordinantion+Takenflag


StringFile = open("Room", "r")
String = StringFile.read()

StringList = String.splitlines()
print(StringList)

M, N = (int(StringList[0]), int(StringList[1]))
print(M, N)

StringMatrix = StringList[2:]
print(StringMatrix)

Matrix = []
for i in range(M):
    Matrix.append(StringMatrix[i].split(' ', N - 1))

for i in range(M):
    for j in range(N):
        Matrix[i][j] = int(Matrix[i][j])

print(Matrix)


def Multiplier(num):
    route = []
    for i in range(num + 1):
        if num % (i + 1) == 0:
            row, col = i + 1, num // (i + 1)
            if row <= M and col <= N:
                route.append([row - 1, col - 1])
    return route


def RouteExist(nodelist):
    for index in range(len(nodelist)):
        if nodelist[index][2]:
            return index+1
    return False

#print(Multiplier(3))

Route = Stack()
node = Node()
takenflag = False

num = Matrix[0][0]
nxtnodelist = Multiplier(num)

for i in range(len(nxtnodelist)):
    nxtnodelist[i].append(True)
    node.nextnodelist.append(nxtnodelist[i])
print(node.nextnodelist)

node.coordination = [0, 0]
Route.push(node)
print(node.nextnodelist)

while True:
    if node.coordination==[M-1,N-1]:
        print("Yes,Escaped!")
        break
    else:
        index=RouteExist(node.nextnodelist)
        if node.coordination==[0,0] and index==False:
            print("No escape!")
            break
        else:
            index=index-1
            if node.nextnodelist[index][2]:
                coord=node.nextnodelist[index][0:2]
                node.nextnodelist[index][2]=False
                numb=Matrix[coord[0]][coord[1]]
                nxtnodelist=Multiplier(numb)
                node=Node()
                node.coordination=coord
                #node.nextnodelist.append(nxtnodelist)
                for i in range(len(nxtnodelist)):
                    nxtnodelist[i].append(True)
                    node.nextnodelist.append(nxtnodelist[i])
                Route.push(node)
            else:
                node=Route.pop()

node=Route.pop()
while node:
    print(node.coordination)
    node=Route.pop()





