N = input("")

friends_data = []
for i in range(0, int(N)):
    user_input = input("")
    friends_data.append(user_input.split())

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
    total_time = 0
    for i in friends_data:
        distance = abs(c - int(i[0]))

        distance = distance - int(i[2])
        if distance == 0 or distance < 0:
            distance = 0

        time = int(i[1]) * distance
        total_time += time

    time_list.append(total_time)

print(time_list)
print(min(time_list))