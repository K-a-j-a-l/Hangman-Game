# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import time
import os

def play_again():
    question="Do you want to play again? Y/N\n"
    play_game=input(question)
    while play_game.lower() not in ['y','n']:
        play_game=input(question)
    if play_game.lower() == 'y':
        return True
    else:
        return False

def hangman(word):
    display='_'*len(word)
    count=0
    limit=5
    letters=list(word)
    guessed=[]
    while count<limit:
        guess=input(f'Hangman word: {display} Enter your Guess:\n').strip()
        while len(guess)==0 or len(guess)>1:
            print("Invalid input. Enter a single letter\n")
            guess=input(f'Hangman word: {display} Enter your Guess:\n').strip()
        if guess in guessed:
            print("Oops! You already tried that guess, try again")
            continue
        if guess in letters:
            letters.remove(guess)
            index=word.find(guess)
            display=display[:index]+guess+display[index+1:]
        else:
            guessed.append(guess)
            count += 1
            if count == 1:
                time.sleep(1)
                print('   _____ \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 2:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 3:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 4:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |      \n'
                      '  |      \n'
                      '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 5:
                time.sleep(1)
                print('   _____ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |    /|\ \n'
                      '  |    / \ \n'
                      '__|__\n')
                print('Wrong guess. You\'ve been hanged!!!\n')
                print(f'The word was: {word}')

        if display == word:
            print(f"Congrats! You have guessed the word \'{word}\' correctly")
            break

def play_hangman():
    print("\n Welcome to Hangman Game")
    name=input('Enter your name')
    print(f'Hello, {name}! Best of Luck!')
    time.sleep(1);
    print("The game is about to start!\n Lets play Hangman")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    words_to_guess=[
        'january', 'border', 'image', 'film', 'promise', 'kids',
        'lungs','doll','rhyme','damage','plants','hello','world'
    ]
    play=True
    while play:
        word=random.choice(words_to_guess)
        hangman(word)
        play=play_again()
    print("Thanks for Playing! We expect you back again!")
    exit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_hangman()
