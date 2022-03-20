N = input('')
matrix = []
for i in range(int(N)):
    user_input = input()
    matrix.append(user_input.split())

def meet_requirement(user_list):
    if user_list == sorted(user_list):
        return True
    else:
        return False

for k in range(4):
    tuple_matrix = list(zip(*matrix[::-1]))
    matrix = []
    for i in tuple_matrix:
        matrix.append(list(i))

    row_requirement = True
    for i in matrix:
        if meet_requirement(i) == False:
            row_requirement = False

    column_matrix = list(zip(*matrix))
    column_requirement = True

    for l in column_matrix:
        if meet_requirement(list(l)) == False:
            column_requirement = False

    if column_requirement and row_requirement:
        for i in matrix:
            print(' '.join(i))