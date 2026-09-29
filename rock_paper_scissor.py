import random

Emojis={'r':'🪨','p':'📃','s':'✂️'}
Choices=('r','p','s')

def get_user_choice():
    while True:
        user_choice=input('Rock ,paper, or scissors? (r/p/s)').lower()
        if user_choice  in Choices:
            return user_choice
        else:
            print('Invalid choice')

def display_choices(user_choice,Computer_choice):
    print(f'You choose {Emojis[user_choice]}')
    print(f'Computer choose {Emojis[Computer_choice]}')
        
def determine_winner(user_choice,Computer_choice):
    if user_choice==Computer_choice:
        print('Tie')
    elif( 
        (user_choice=='r' and Computer_choice=='s')or
        (user_choice=='p' and Computer_choice=='r')or
        (user_choice=='s' and Computer_choice=='p')):
        print("You win")
    
    elif(
        (user_choice=='s' and Computer_choice=='r')or
        (user_choice=='r' and Computer_choice=='p')or
        (user_choice=='p' and Computer_choice=='s')):
        print("Computer wins")
def play_game():
    while True:
        user_choice=get_user_choice()
        Computer_choice=random.choice(Choices)
        display_choices(user_choice,Computer_choice)
        determine_winner(user_choice,Computer_choice)    
        Should_Continue =input('Continue? (y/n)').lower()
        if Should_Continue=='n':
            break
play_game()


    
    

    
