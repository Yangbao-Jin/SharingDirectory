triangle = []

number_of_lines = 5

x = 1
while x <= number_of_lines:
    if x == 1:
        triangle.append(x)
    else:
        middle_number = 2 * x - 1
        number_list = []
        for i in range(x, middle_number):
            number_list.append(i)

        reverse_num_list = []
        for i in number_list[::-1]:
            reverse_num_list.append(i)

        string = ''
        for i in number_list:
            string += str(i)
        string += str(middle_number)
        for i in reverse_num_list:
            string += str(i)

        triangle.append(string)

    x += 1

print(triangle)

