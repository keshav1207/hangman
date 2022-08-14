import random, english_words

word_list = list(english_words.english_words_lower_set)

word = (random.choice(word_list))
correct_guess = []

lives = 6
score = 0

while lives > 0 and score < len(word):
    display =[]
    for i in range(len(word)):
        if word[i] in correct_guess:
            display.append(word[i])

        else:
            display.append('-')

    print(''.join(display))
    print(f" Lives: {lives}")
    user_input = input('Enter a letter:   ').lower().strip()
    if not user_input.isalpha():
        print('Enter a valid letter')
        continue

    if user_input in word:
        score += 1
        correct_guess.append(user_input)

    else:
        lives -= 1

if lives == 0:
    print(f" You are Dead !  Game over !")

else:
    print(f"Congrats ! You guessed the word {''.join(word)} correctly.")

