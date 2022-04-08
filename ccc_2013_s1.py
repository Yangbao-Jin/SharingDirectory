user_input = int(input(""))
d = str(user_input + 1)

while True:
    distinct = True
    for i in d:
        if d.count(i) > 1:
            distinct = False
    if distinct:
        print((int(d)))
        break
    else:
        d = str(int(d) + 1)