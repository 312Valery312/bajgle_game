#CHALLENGE: 100 DAYS WITH PYTHON 
#1 DAY - BAJGLE GAME
import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a logical deduction game. Author: Valery Hood | GitHub link here

I'm thinking of a {}-digit number with no repeated digits.
Try to guess it. Here are the clues:
When I say:    It means:
Pico          One digit is correct but in the wrong position.
Fermi         One digit is correct and in the right position.
Bagels        No digit is correct.
For example, if the secret number is 248 and you guess 843, the clue will be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        secret_number = ''.join(random.sample('0123456789', NUM_DIGITS))
        print('I am thinking of a number.')

        for guess_attempt in range(1, MAX_GUESSES + 1):
            guess = input(f'Guess #{guess_attempt}: ')
            if not guess.isdigit() or len(guess) != NUM_DIGITS:
                print(f'Please enter a {NUM_DIGITS}-digit number.')
                continue

            clues = get_clues(guess, secret_number)
            print(clues)

            if guess == secret_number:
                print(f'Congratulations! You guessed the number {secret_number} in {guess_attempt} attempts.')
                break
        else:
            print('You have exhausted all guesses.')
            print(f'The correct answer is: {secret_number}.')

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break
    print('Thank you for playing!')

def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'Success!'

    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')

    return ' '.join(clues) if clues else 'Bagels'

if __name__ == '__main__':
    main()
    
