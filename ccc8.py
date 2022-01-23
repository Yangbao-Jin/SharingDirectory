# Set up the file
file = open("ccc8_file", "r")
lines = file.readlines()

# Define variables
line = 0

while lines[line] != "\n":
    Rule1 = lines[line]
    Rule1_list = Rule1.split()
    break
line += 1

while lines[line] != "\n":
    Rule2 = lines[line]
    Rule2_list = Rule2.split()
    break
line += 1

while lines[line] != "\n":
    Rule3 = lines[line]
    Rule3_list = Rule3.split()
    break
line += 1

while lines[line] != "\n":
    line4_list = lines[line].split()
    break

steps_required = line4_list[0]
starting_letters = line4_list[1]
ending_letters = line4_list[2]

print(Rule1_list)
print(Rule2_list)
print(Rule3_list)
print(steps_required)
print(starting_letters)
print(ending_letters)

# Algorithm - Trial and Error

steps_taken = 0
try_rules = 1
time = 0

while True:
    if steps_taken > steps_required:
        try_rules += 1
        starting_letters = saved_letters

    else:
        if starting_letters.find(Rule1_list[0]) == -1 and starting_letters.find(Rule2_list[0]) == -1 and starting_letters.find(Rule3_list[0]) == -1:
            print("This puzzle have no solution")
            break

        elif starting_letters.find(Rule1_list[0]) != -1 and starting_letters.find(Rule2_list[0]) == -1 and starting_letters.find(Rule3_list[0]) == -1:
            starting_letters.replace(Rule1_list[0], Rule1_list[1])
            index = starting_letters.find(Rule1_list[0])
            print(f"1 {index} {starting_letters}")

            if starting_letters == ending_letters and steps_taken == steps_required:
                break

            else:
                steps_taken += 1

        elif starting_letters.find(Rule1_list[0]) == -1 and starting_letters.find(Rule2_list[0]) != -1 and starting_letters.find(Rule3_list[0]) == -1:
            starting_letters.replace(Rule1_list[0], Rule1_list[1])
            index = starting_letters.find(Rule1_list[0])
            print(f"2 {index} {starting_letters}")

            if starting_letters == ending_letters and steps_taken == steps_required:
                break

            else:
                steps_taken += 1

        elif starting_letters.find(Rule1_list[0]) == -1 and starting_letters.find(Rule2_list[0]) == -1 and starting_letters.find(Rule3_list[0]) != -1:
            starting_letters.replace(Rule1_list[0], Rule1_list[1])
            index = starting_letters.find(Rule1_list[0])
            print(f"3 {index} {starting_letters}")

            if starting_letters == ending_letters and steps_taken == steps_required:
                break

            else:
                steps_taken += 1

        elif starting_letters.find(Rule1_list[0]) != -1 and starting_letters.find(Rule2_list[0]) != -1 and starting_letters.find(Rule3_list[0]) == -1:
            if time == 0:
                saved_letters = starting_letters

            if try_rules == 1:
                starting_letters.replace(Rule1_list[0], Rule1_list[1])

                if starting_letters == ending_letters and steps_taken == steps_required:
                    index = starting_letters.find(Rule1_list[0])
                    print(f"1 {index} {starting_letters}")

            elif try_rules == 2:
                starting_letters.replace(Rule2_list[0], Rule2_list[1])

                if starting_letters == ending_letters and steps_taken == steps_required:
                    index = starting_letters.find(Rule2_list[0])
                    print(f"2 {index} {starting_letters}")

        elif starting_letters.find(Rule1_list[0]) != -1 and starting_letters.find(Rule2_list[0]) == -1 and starting_letters.find(Rule3_list[0]) != -1:
            if time == 0:
                saved_letters = starting_letters

            if try_rules == 1:
                starting_letters.replace(Rule1_list[0], Rule1_list[1])

                if starting_letters == ending_letters and steps_taken == steps_required:
                    index = starting_letters.find(Rule1_list[0])
                    print(f"1 {index} {starting_letters}")

            elif try_rules == 3:
                starting_letters.replace(Rule3_list[0], Rule3_list[1])

                if starting_letters == ending_letters and steps_taken == steps_required:
                    index = starting_letters.find(Rule3_list[0])
                    print(f"3 {index} {starting_letters}")