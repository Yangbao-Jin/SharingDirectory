input = open("aoc_2015_q3_file", "r").read()

santa_x = 0
santa_y = 0

robo_x = 0
robo_y = 0

index = 0

input_list = list(input)

been_to_houses = []
number_of_houses = 0

for i in input_list:
    if index % 2 == 0:
        if i == "^":
            santa_y += 1
            been_to = False
            house_coordinate = [santa_x, santa_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

        elif i == "v":
            santa_y -= 1
            been_to = False
            house_coordinate = [santa_x, santa_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

        elif i == ">":
            santa_x += 1
            been_to = False
            house_coordinate = [santa_x, santa_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

        elif i == "<":
            santa_x -= 1
            been_to = False
            house_coordinate = [santa_x, santa_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

    else:
        if i == "^":
            robo_y += 1
            been_to = False
            house_coordinate = [robo_x, robo_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

        elif i == "v":
            robo_y -= 1
            been_to = False
            house_coordinate = [robo_x, robo_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

        elif i == ">":
            robo_x += 1
            been_to = False
            house_coordinate = [robo_x, robo_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

        elif i == "<":
            robo_x -= 1
            been_to = False
            house_coordinate = [robo_x, robo_y]
            for k in been_to_houses:
                if k == house_coordinate:
                    been_to = True
                    break

            if been_to == False:
                number_of_houses += 1
                been_to_houses.append(house_coordinate)

    index += 1

print(number_of_houses)