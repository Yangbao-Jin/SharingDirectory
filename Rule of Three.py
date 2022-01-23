#Rule of Three

#Read rules file
StringFile = open("RuleofThree.txt", "r")
String = StringFile.read()
#print(String)

StringList=String.splitlines()
#print(StringList)
Rule1, Rule2, Rule3 = StringList[0], StringList[1], StringList[2]
Requirement=StringList[3]
Req=Requirement.split()
S=Req[0]
I=Req[1]
F=Req[2]

Rule1List=Rule1.split()
Rule2List=Rule2.split()
Rule3List=Rule3.split()

'''
print(Rule1List,Rule2List,Rule3List)
print(Rule1)
print(Rule2)
print(Rule3)
print(S)
print(I)
print(F)

'''

