N = input('')
t_count = 0
s_count = 0
for i in range(int(N)):
    user_input = input('')
    t_count = t_count + user_input.count('t') + user_input.count('T')
    s_count = s_count + user_input.count('s') + user_input.count('S')

print('English' if t_count > s_count else 'French')