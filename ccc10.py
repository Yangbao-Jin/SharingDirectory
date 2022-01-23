file = open("ccc10_file", "r")
lines = file.read()

distances = lines.split()
distances.insert(0, "0")

i = 1
answer = ""
while i < len(distances):
    for x in distances:
        if int(x) < int(distances[i]):
            answer = answer + f"{int(distances[i]) - int(x)} "

        elif int(x) == int(distances[i]):
            answer = answer + "0 "

        elif int(x) > int(distances[i]):
            answer = answer + f"{int(x) - int(distances[i])} "

    i += 1
    answer = answer + "\n"

print(answer)