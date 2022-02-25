input_file = open("aoc_2015_q2_file", "r")
lines = input_file.readlines()

real_lines = []

for i in lines:
    i_list = list(i)
    for k in i_list:
        if k == "\n":
            i_list.remove("\n")

    i_str = ""
    for s in i_list:
        i_str = i_str + s

    print(i_str)

    real_lines.append(i_str)

wrapping_paper_total = 0
ribbon_total = 0
for p in real_lines:
    split_lines = p.split("x")
    l = int(split_lines[0])
    w = int(split_lines[1])
    h = int(split_lines[2])

    all_areas = []
    all_areas.append(l * w)
    all_areas.append(l * h)
    all_areas.append(w * h)
    all_areas.sort()
    smallest_side = all_areas[0]

    all_perimeters = []
    all_perimeters.append(l + l + w + w)
    all_perimeters.append(l + l + h + h)
    all_perimeters.append(w + w + h + h)
    all_perimeters.sort()
    smallest_perimeter = all_perimeters[0]
    ribbon_total = ribbon_total + smallest_perimeter + l*w*h

    wrapping_paper_total = wrapping_paper_total + l * w * 2 + l * h * 2 + w * h * 2 + smallest_side

print(f'Total Wrapping Paper: {wrapping_paper_total}')
print(f'Total Ribbon: {ribbon_total}')

