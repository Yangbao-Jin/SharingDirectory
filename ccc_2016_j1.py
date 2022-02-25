a = input("")
b = input("")
c = input("")
d = input("")
e = input("")
f = input("")

inputs = []
inputs.append(a)
inputs.append(b)
inputs.append(c)
inputs.append(d)
inputs.append(e)
inputs.append(f)

wins = 0
for i in inputs:
    if i == "W":
        wins += 1

if wins == 1 or wins == 2:
    print(3)

elif wins == 3 or wins == 4:
    print(2)

elif wins == 5 or wins == 6:
    print(1)

else:
    print(-1)