
class node:
    def __init__(self,string):
        self.string=string
        self.next=[]
        #self.level=level

class graph:
    def __init__(self):
        self.nodelist=[]
        self.stringlist=[]
        self.newstringlist=[]


    def addnode(self,currentnode,node):
        if node.string not in self.stringlist:
        #if node.string not in self.nodelist
            self.nodelist.append(node)
            self.stringlist.append(node.string)
            currentnode.next.append(node)
            self.newstringlist.append(node.string)

        else:
            idx=self.stringlist.index(node.string)
            currentnode.next.append(self.nodelist[idx])

    def addbranch(self,currentnode):
        for rule in RuleList:  # each rule
            mystr = Mystring(currentnode.string, rule[0], rule[1])
            for i in mystr.Myreplace():
                nodei = node(i)
                self.addnode(snode, nodei)

    def addnewnode(self, string):
        self.newstringlist.append(string)

    def delnewnode(self, string):
        self.newstringlist.remove(string)


class Mystring:
    def __init__(self,Fstr,Ostr,Tstr):
        self.fstr=str(Fstr)
        self.ostr=str(Ostr)
        self.tstr=str(Tstr)

    def Myreplace(self):
        times=self.fstr.count(self.ostr,0,len(self.fstr))
        i=0
        idx=[]
        afterep=[]
        while i<times:
            if i==0:
                idxt=self.fstr.index(self.ostr,0,len(self.fstr))
                idx.append(idxt)
            else:
                idxt = self.fstr.index(self.ostr, idx[i-1]+1, len(self.fstr))
                idx.append(idxt)

            Ilen=len(self.fstr)
            if idx[i]!=0:
                forstr=self.fstr[0:idx[i]]
            else:
                forstr=""
            tempstr=self.fstr[idx[i]:len(self.fstr)].replace(self.ostr, self.tstr,1)
            afterep.append(forstr+tempstr)
            #afterep.append(self.fstr[idx[i]:Ilen].replace(self.ostr,self.tstr,1))
            i=i+1
        #print idx
        #print times
        return afterep

if __name__=='__main__':

    #Read rules file
    StringFile = open("RuleofThree.txt", "r")
    String = StringFile.read()

    StringList=String.splitlines()
    #
    Rule1, Rule2, Rule3 = StringList[0], StringList[1], StringList[2]
    Requirement=StringList[3]
    Req=Requirement.split()
    S=Req[0]
    I=Req[1]
    F=Req[2]

    Rule1List=Rule1.split()
    Rule2List=Rule2.split()
    Rule3List=Rule3.split()

    RuleList=[Rule1List,Rule2List,Rule3List]
    print RuleList
    print(Rule1List,Rule2List,Rule3List)
    print(Rule1)
    print(Rule2)
    print(Rule3)
    print(S)
    print(I)
    print(F)

    snode=node(I)
    g=graph()
    g.nodelist.append(snode)
    g.stringlist.append(I)
    g.newstringlist.append(I)
    stepstring=[I]
    for step in range(0,int(S)):# each step
        for i in stepstring:
            inode=node(i)
            g.addbranch(inode)

            g.delnewnode(i)
        stepstring=g.newstringlist[:]
        if step==int(S)-1:
            if F in stepstring:
                print("Solved")
            else:
                print("No solution")



    print g.stringlist
    #print g.newstringlist
    #print g.nodelist

    #print g.nodelist[0].next


