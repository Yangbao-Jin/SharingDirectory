# Read input file
StringFile = open("Room", "r")
String = StringFile.read()

StringList = String.splitlines()
print(StringList)

M,N=(int(StringList[0]),int(StringList[1]))
print(M,N)

StringMatrix=StringList[2:]
print(StringMatrix)

Matrix=[]
for i in range(M):
   Matrix.append(StringMatrix[i].split(' ', N-1))

for i in range(M):
    for j in range(N):
        Matrix[i][j]=int(Matrix[i][j])

print(Matrix)

