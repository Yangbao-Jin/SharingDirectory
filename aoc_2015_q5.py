input = open('aoc_2015_q5_file', 'r').readlines()

nice_strings = 0
nice_strings_candidates = []

for i in input:
    i_list = list(i)
    print(i_list)
    twice_requirement = False
    banned_words_requirement = True

    said_characters = ['']
    for k2 in i_list:
        the_string = said_characters[-1] + k2
        if k2 == said_characters[-1]:
            twice_requirement = True
            said_characters.append(k2)

        elif the_string == "ab" or the_string == "cd" or the_string == "pq" or the_string == "xy":
            banned_words_requirement = False

        else:
            said_characters.append(k2)

    if twice_requirement == True and banned_words_requirement == True:
        nice_strings_candidates.append(i)

vowel_counts = []

for l in nice_strings_candidates:
    vowel_count = 0
    for s in l:
        if s == "a" or s == "e" or s == "i" or s == 'o' or s == "u":
            vowel_count += 1

    if vowel_count >= 3:
        nice_strings += 1

print(nice_strings)

