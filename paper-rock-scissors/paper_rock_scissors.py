# A Python program for the Rock, Paper, Scissors game.
import random


def rock_paper_scissors():

    print()
    game_len = int(input('How many points does it take to win? '))

    round_n = 1
    user_score = 0
    com_score = 0

    # loop for rounds to be played
    while (user_score < game_len) and (com_score < game_len):

        com_choice = (random.randint(1, 3))

        print()
        print('********************* ROUND #',
              round_n, ' *********************')
        print()
        round_n += 1

        # choices to be picked
        print()
        user_choice = input(
            ('Pick your throw: [r]ock, [p]aper, or [s]cissors? '))

        if user_choice == 'r':
            user_choice = 1

        elif user_choice == 'p':
            user_choice = 2

        elif user_choice == 's':
            user_choice = 3

        if com_choice == 1:
            choice = 'rock'

        elif com_choice == 2:
            choice = 'paper'

        elif com_choice == 3:
            choice = 'scissors'

        # possible outcomes
        if user_choice == com_choice:
            print('Tie!')

        # if user wins the round
        elif (user_choice == 1 and com_choice == 3) or (user_choice == 3 and com_choice == 2) or (user_choice == 2 and com_choice == 1):
            print('Computer threw', choice+', you win!')
            user_score += 1

            print()
            print('Your score: ', user_score)
            print('Computer\'s score: ', com_score)

        # if computer wins the round
        else:
            print('Computer threw', choice+', you lose!')
            com_score += 1

            print()
            print('Your score: ', user_score)
            print('Computer\'s score: ', com_score)

    # if user wins the game
    if user_score == game_len:
        print()
        print('********************* GAME OVER ********************')
        print()
        print('You Win!')

    # if computer wins the game
    else:
        print()
        print('********************* GAME OVER ********************')
        print()
        print('You lose!')


# main function
def main():
    print('ROCK PAPER SCISSORS in Python')
    print()
    print('Rules: 1) Rock wins over Scissors.')
    print('       2) Scissors wins over Paper.')
    print('       3) Paper wins over Rock.')

    rock_paper_scissors()


main()
