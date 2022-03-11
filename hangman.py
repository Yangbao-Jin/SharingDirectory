word = 'kookaburra'
guess_attempts = []

while True:
    user_input = input("Enter a letter: ")
    if user_input == "quit":
        break

    else:
        letter_count = 1
        for i in guess_attempts:
            if i == user_input:
                letter_count += 1

        guess_attempts.append(user_input)

        in_word = False
        for i in word:
            if i == user_input:
                in_word = True

        if in_word == True:
            print(f"The letter '{user_input}' is in the word.")

        else:
            print(f"The letter '{user_input}' is not in the word.")

        print(f"Number of times you have guessed letter '{user_input}': {letter_count}")



