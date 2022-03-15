import itertools

N = input("")
H = input("")

nums = list(N)
permutations = list(itertools.permutations(nums))
non_repeat_permutations = []

for i in permutations:
    if i in non_repeat_permutations:
        pass
    else:
        non_repeat_permutations.append(i)

real_permutations = []
for i in non_repeat_permutations:
    string = ''
    for k in i:
        string += k

    real_permutations.append(string)

H_combinations = [H[i: j] for i in range(len(H)) for j in range(i + 1, len(H) + 1)]
str_H_combinations = []

for i in H_combinations:
    string = ''.join([str(item) for item in i])
    str_H_combinations.append(string)

count = 0
for i in real_permutations:
    if i in str_H_combinations:
        count += 1

print(count)