import itertools

J = 90
H = []
for i in range(J):
    H.append(i + 1)

combinations = list(map(list, list(itertools.combinations(H, 4))))
real_combinations = []
for i in combinations:
    if i not in real_combinations:
        real_combinations.append(i)

print(len(real_combinations))
