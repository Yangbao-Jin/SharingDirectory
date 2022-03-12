#  #All copyright reserved by Jim Jin
#

# Read input file
StringFile = open("person.txt", "r")
String = StringFile.read()

StringList = String.splitlines()
N = int(StringList[0])
PersonList = StringList[1:N + 1]
print(PersonList)
for i in range(N):
    PersonList[i] = PersonList[i].split(' ', 2)


print(PersonList)
print(N)
poslist=[]

for i in range(N):
    poslist.append(int(PersonList[i][0]))

print(poslist)
M=max(poslist)

TimeList=[]

distance = 0
sumtime = 0
c=0
while c < M:
    for j in range(N):
        distance = abs(c - int(PersonList[j][0]))
        diff = distance - int(PersonList[j][2])
        if diff > 0:
            time = diff * int(PersonList[j][1])
        else:
            time = 0
        sumtime += time
    TimeList.append(sumtime)
    c += 1
    sumtime = 0
print(TimeList)
print(min(TimeList))
