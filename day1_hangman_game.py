import random
words_ = [
    'pillow',
    'nepal',
    'india',
    'computer',
    'laptop',
    'simulation',
    'learning',
]
# extracting the word from random method
random_word = random.choice(words_)

# generating the total count for guess
lives = len(random_word)

# generates the list with blanks
blanks = ['_' for _ in random_word]
print(blanks)

won = False

# continue while loop until live counts
while not won:
    print(f"You're left with {lives} lives.")
    user_input = input("Please enter your word: ").lower()
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == user_input:
            blanks[position] = letter
    print(blanks)

    # for tracking lives
    if user_input not in random_word:
        lives = lives-1
        if lives<1:
            print("Sorry. You ran out of lives.")
            break

    # check whether there are any left blanks to fill by the user
    if "_" not in blanks:
        won = True
        print("Congrats. You've won the game")