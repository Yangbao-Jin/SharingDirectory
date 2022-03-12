N = input("")

friends_data = []
for i in range(0, int(N)):
    user_input = input("")
    friends_data.append(user_input.split())

# 2
# 10 4 3
# 20 4 2

biggest_suitable_num = 0

for i in friends_data:
    if int(i[0]) - int(i[1]) > biggest_suitable_num:
        biggest_suitable_num = int(i[0]) - int(i[2])

smallest_suitable_num = biggest_suitable_num + 1

for i in friends_data:
    if int(i[0]) - int(i[1]) < smallest_suitable_num:
        smallest_suitable_num = int(i[0]) - int(i[2])

print(biggest_suitable_num)
print(smallest_suitable_num)

print(friends_data)

time_list = []

for c in range(smallest_suitable_num, biggest_suitable_num + 1):
    total_time = []
    for i in friends_data:

        if c < int(i[0]):
            distance = int(i[0]) - c
        elif c == int(i[0]):
            distance = 0
        else:
            distance = c - int(i[0])

        total_time = total_time + int(i[1]) * distance
        print(total_time)

    time_list.append(total_time)

print(time_list)
print(min(time_list))