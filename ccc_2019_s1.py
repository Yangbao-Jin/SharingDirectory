orientation = input("")
grid = [[1, 2], [3, 4]]

for i in orientation:
    if i == "H":
        grid.append(grid[0])
        grid.pop(0)

    else:
        grid[0].append(grid[0][0])
        grid[1].append(grid[1][0])
        grid[0].pop(0)
        grid[1].pop(0)

ans_str = ''
for i in grid:
    for k in i:
        ans_str = ans_str + str(k) + " "
    ans_str += "\n"

print(ans_str)