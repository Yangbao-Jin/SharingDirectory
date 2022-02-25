input = open("aoc_2015_q3_file", "r").read()

x = 0
y = 0

input_list = list(input)

been_to_houses = []
number_of_houses = 0

# ^>v<

for i in input_list:
    if i == "^":
        y += 1
        been_to = False
        house_coordinate = [x, y]
        for k in been_to_houses:
            if k == house_coordinate:
                been_to = True
                break

        if been_to == False:
            number_of_houses += 1
            been_to_houses.append(house_coordinate)

    elif i == "v":
        y -= 1
        been_to = False
        house_coordinate = [x, y]
        for k in been_to_houses:
            if k == house_coordinate:
                been_to = True
                break

        if been_to == False:
            number_of_houses += 1
            been_to_houses.append(house_coordinate)

    elif i == ">":
        x += 1
        been_to = False
        house_coordinate = [x, y]
        for k in been_to_houses:
            if k == house_coordinate:
                been_to = True
                break

        if been_to == False:
            number_of_houses += 1
            been_to_houses.append(house_coordinate)

    elif i == "<":
        x -= 1
        been_to = False
        house_coordinate = [x, y]
        for k in been_to_houses:
            if k == house_coordinate:
                been_to = True
                break

        if been_to == False:
            number_of_houses += 1
            been_to_houses.append(house_coordinate)

print(number_of_houses)
