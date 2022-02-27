line1 = input("")

inputs = list(line1)

def is_palindrome(string):
    reverse_string = string[::-1]
    if reverse_string == string:
        return True

    else:
        return False

print(inputs)
possible_palindromes = []

"""Attempt 3"""

x = 6
z = 0
for index, value in enumerate(inputs):
    y = 1
    while x != z:
        string = ""
        for k in inputs[index:y]:
            string += k

        print(string)

        if is_palindrome(string) == True:
            possible_palindromes.append(string)

        y += 1
        z += 1
    x -= 1

print(possible_palindromes)

print(possible_palindromes)

"""Attempt 2"""

# for i in inputs:
#     for index, value in enumerate(inputs[::-1]):
#         the_word = ""
#         for index2, value2 in enumerate(inputs[index:]):
#             if index == index2:
#                 the_word = the_word + value2
#                 break
#             else:
#                 the_word = the_word + value2
#
#         print(the_word)
#
#         if is_palindrome(the_word) == True:
#             possible_palindromes.append(the_word)
# print(possible_palindromes)

"""Attempt 1"""

# i = len(inputs) - 1
# k = 0
# f = 0
# f_target = 2
# i2 = i
#
# for index, value in enumerate(inputs):
#     string = ""
#     for i in inputs[index:i2]:
#         string = string + i
#     if is_palindrome(string) == True:
#         print(string)
#         break
#
#     k += 1
#     if f == f_target:
#         f_target = f_target + f_target + 1
#     f += 1
#     i2 += 1


