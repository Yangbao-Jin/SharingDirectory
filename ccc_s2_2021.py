x = input()

must_be_in_same_group = []

for i in range(0, int(x)):
    x_input = input()
    must_be_in_same_group.append(x_input.split())

y = input()

must_not_be_in_same_group = []

for i in range(0, int(y)):
    y_input = input()
    must_not_be_in_same_group.append(y_input.split())

g = input()

groups = []

for i in range(0, int(g)):
    g_input = input()
    groups.append(g_input.split())

violation_count = 0

for i in groups:
    for k1 in must_be_in_same_group:
        print(violation_count)
        if (k1[0] not in i == False and k1[1] in i) or (k1[1] not in i and k1[0] in i):
            violation_count += 1

    for k2 in must_not_be_in_same_group:
        if k2[0] in i and k2[1] not in i:
            violation_count += 1

print(violation_count)