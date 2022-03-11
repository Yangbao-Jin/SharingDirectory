m = input('')
n = input('')
k = input('')

brush_instructions = []
for i in range(0, int(k)):
    the_input = input('')
    brush_instructions.append(the_input.split())

art_array = []
for i in range(0, int(m)):
    art_array.append([])

for i in art_array:
    for s in range(0, int(n)):
        i.append("B")

for i in brush_instructions:
    if i[0] == "R":
        art_array_row = art_array[int(i[1]) - 1]
        for index, value in enumerate(art_array_row):
            if value == "B":
                art_array_row.pop(index)
                art_array_row.insert(index, "G")
            elif value == "G":
                art_array_row.pop(index)
                art_array_row.insert(index, "B")


    elif i[0] == "C":
        for s in art_array:
            for index, value in enumerate(s):
                if index == int(i[1]) - 1:
                    if value == "B":
                        s.pop(index)
                        s.insert(index, "G")
                    elif value == "G":
                        s.pop(index)
                        s.insert(index, "B")

gold_count = 0
for i in art_array:
    for k in i:
        if k == "G":
            gold_count += 1

print(gold_count)