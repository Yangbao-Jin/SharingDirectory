#  #All copyright reserved by Jim Jin
#
# line1 = input("")


line = "bananac12345678987654321"
inputs = list(line)


starter = 0
ending = len(inputs)

palindromelist = []
while ending > 0:

    while starter != ending:
        listpiece = inputs[starter:ending]
        flist = listpiece.copy()
        blist = listpiece.copy()
        blist.reverse()

        if flist == blist:
            palindromelist.append(flist)
            starter += 1
        else:
            starter += 1
    ending -= 1
    starter = 0


numlist=[]

for s in palindromelist:
    numlist.append(len(s))

m=max(numlist)
index=numlist.index(m)
print(numlist)

print(palindromelist[index])


