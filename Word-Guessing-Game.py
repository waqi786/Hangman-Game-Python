import random
word_list = ['waqar','abrar','bilal','rashid']
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in range(len(chosen_word)):
    display += "_"
lives = 6
end_game = False
while end_game == False:
    guess = input("enter a letter here: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print("You guessed {guess}, that's not in the word. You lose life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose")
    if "_" not in display:
       end_game = True
       print("You Won")