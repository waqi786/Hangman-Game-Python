# Hangman-Game-Python

This repository hosts my Python implementation of the classic hangman game. Players guess letters to uncover a word randomly chosen from a predefined list. The game continues until the word is guessed correctly or all lives are lost. Uploaded on 07/14/2024.

How to Play

1. Clone this repository to your local machine.
2. Run the hangman.py script using Python 3.x.
3. Input letters to guess the hidden word.
4. Win the game by correctly guessing all letters, or lose by depleting all lives.
   
Features

1. Random selection of words from a predefined list.
2. Interactive gameplay with visual feedback on guessed letters.
3. End-game conditions for both successful guesses and loss of all lives.
   
Example Gameplay

Welcome to Hangman!

_ _ _ _ _   (Initial display of the word to guess)

Enter a letter: a
_ a _ _ a _   (Updated display after correct guess)

Enter a letter: e
You guessed e, that's not in the word. You lose a life.

Remaining lives: 5

...

Enter a letter: h
_ a _ _ a _   (Display after another correct guess)

...

You guessed the word! You won.
