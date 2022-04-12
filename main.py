import random

with open("words.txt") as f:
    words = f.read().splitlines()
    answer = words[random.randint(0, len(words))]

correct_guesses = []
incorrect_guesses = []


def lose():
    print("You lost.\nThe word was " + answer)
    quit()


def win():
    print("You won.")
    quit()


def draw_func(wrong_guesses):
    print(' +---+')

    if wrong_guesses >= 1:
        print(' 0   |')
    else:
        print('     |')

    if wrong_guesses == 2:
        print(' |   |')
    elif wrong_guesses == 3:
        print('/|   |')
    elif wrong_guesses >= 4:
        print('/|\  |')
    else:
        print('     |')

    if wrong_guesses == 5:
        print('/    |')
    elif wrong_guesses >= 6:
        print('/ \  |')
        lose()
    else:
        print('     |')

    print('   =====')
    print("Incorrect guesses: " + str(incorrect_guesses))

    s = []
    for i in answer:
        if i in correct_guesses:
            s.append(i)
    guessed = ''
    for i in answer:
        if i in s:
            guessed += i
        else:
            guessed += '_'
    print(guessed)


game_is_running = True
while game_is_running:
    draw_func(len(incorrect_guesses))

    c = 0
    for i in answer:
        if i in correct_guesses:
            c += 1
    if c == len(answer):
        win()

    guess = input("Guess a letter: ")
    if len(guess) > 1:
        print("You may only guess a single letter.")
    elif guess in correct_guesses or guess in incorrect_guesses:
        print("You have already guessed this letter")
    elif guess in answer:
        correct_guesses.append(guess)
    else:
        incorrect_guesses.append(guess)
