import random as r

def intro():
    '''This function introduces the game to the player'''

    print("Welcome to the Rock-Paper-Scissors game, Player!!!")
    print("Rules of the game!!! You have three turns to determine the winner\n \
         If Rock vs Paper: Then Paper wins!\n \
         If Rock vs Scissors: Then Rock wins\n \
         If paper vs scissor: Then scissors wins \n")
    
    
def choice_check():
    '''Function takes user input'''

    print("Input your choice")
    print("Note:\n R stands for Rock\n P stands for Paper\n S stands for Scissors...")
    player_choice = input("Please input your choice from 'R', 'P, or 'S':")
    player_choice = player_choice.upper()
    choice_list = ['R', 'P', 'S']

    turns = 3

    if player_choice not in choice_list:
        print("You entered the wrong choice")
        choice_check()

    else:
        cpu_choice = r.choice(choice_list)
        if cpu_choice == player_choice:
            print("We have a tie")
            choice_check()
        
        elif cpu_choice == 'R' and player_choice == 'S':
            print('Player(Scissors) : CPU(Rock)')
            print('CPU wins!!!')

        elif cpu_choice == 'P' and player_choice == 'S':
            print('Player(Scissors) : CPU(Paper)')
            print('You win!!!')

        elif cpu_choice == 'P' and player_choice == 'R':
            print('Player(Scissors) : CPU(Paper)')
            print('You win!!!')

        elif cpu_choice == 'S' and player_choice == 'P':
            print('Player(Player) : CPU(Scissors)')
            print('CPU wins!!!')

        elif cpu_choice == 'S' and player_choice == 'R':
            print('Player(Rock) : CPU(Scissors)')
            print('You win!!!')

        elif cpu_choice == 'R' and player_choice == 'P':
            print('Player(Paper) : CPU(Rock)')
            print('CPU wins!!!')


        
def play_again():
    print('Do you wish to play again? Y/N')
    play_again = input('Enter your choice here: ')

    if play_again == 'Y' or play_again == 'y':
        choice_check()
    else:
        print('Thank you for playing')


intro()
choice_check()
