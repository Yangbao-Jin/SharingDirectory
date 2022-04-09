string = ''
num_string = ''

for i in string:
    if i == "I":
        num_string = num_string + '1' + "+"
    elif i == "V":
        num_string = num_string + '5' + "+"
    elif i == "X":
        num_string = num_string + '10' + "+"
    elif i == "L":
        num_string = num_string + '50' + "+"
    elif i == "C":
        num_string = num_string + '100' + "+"
    elif i == "D":
        num_string = num_string + '500' + "+"
    elif i == "M":
        num_string = num_string + '1000' + "+"
    else:
        num_string = num_string + i + " "

nums = num_string.split("+")
nums.pop()
for i in nums:
    i_list = i.split()

symbols, numbers = [], []
for index, value in enumerate(nums[:len(nums) - 1]):
    if int(value.split()[1]) >= int(nums[index+1].split()[1]):
        symbols.append("+")
    else:
        symbols.append("-")

    numbers.append(int(value.split()[0]) * int(value.split()[1]))
symbols.append("+")
numbers.append(int(nums[-1].split()[0]) * int(nums[-1].split()[1]))

number = 0
for i in range(len(symbols)):
    number = number + eval(f'{symbols[i]}{numbers[i]}')

print(number)
