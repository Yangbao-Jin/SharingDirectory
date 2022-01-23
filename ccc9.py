file = open("ccc9_file", "r")
lines = file.readlines()


yesterday = list(lines[1])
today = list(lines[2])

yesterday.pop()

answer = 0
x = 0

while x < len(yesterday):
    if yesterday[x] == "C" and today[x] == "C":
        answer += 1

    x += 1

print(answer)