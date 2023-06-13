def get_username():
    """
    Gets the players name
    """
    print('Hello')
    while True:
        username = input('Enter username:')
        if username == '':
            print('You must enter a username')
            continue    
        else:        
            print('Welcome', username, 'lets get started')
            break


get_username()


def play_again():
    """
    This is called after game is over and gives choice to play again
    """
    answer = input('Do you want to play again? \n yes or no \n')
    if answer == 'yes':
        print('Ok, lets play again')
    elif answer == 'no':
        print('Goodbye')



#bplay_again()


def forest_game():
    """
    Runs the forest themed game
    """

    answer = input('You find yourself at the edge of a dense forest. The entrance looks dark and mysterious.\n Do you:\n a)Enter the forest\n b)Walk away and find a new adventure\n')
    if answer == 'a':
        answer = input('You enter the forest and walk along the winding path.\n The trees are tall and the leaves rustle in the wind.\n Suddenly you hear a loud growl.\nDo you:\n a)Run away\n b)Investigate the source of the noise\n')
    else:
        print('You left the game\n')
        #run random game function when created
        exit(play_again())
        
    if answer == 'b':
        print('You follow the sound and find a wounded wolf. It looks at you with pleading eyes.\n Do you:\n a)Help the wolf \n b) Leave the wolf and continus on your journey')
    else:
        print('You ran away. Game over!!!')
        exit(play_again())

    if answer == 'a':
        print('You help the wolf and bandage its wounds. The wolf is greatful and leads you to a hidden clearing. In the center of the clearing, you see a chest.\n Do you: \n a)Open the chest\n b) Leave the chest and continueon your adventure')
    else:
        print('You leave the wolf behind and keep following the path ahead. As you continue you SUDDENLY fall through a trap door and plummet to your death!!!!\n')
        exit(play_again())


forest_game()    


def haunted_house_game():
    """
    Runs the haunted house game
    """
    