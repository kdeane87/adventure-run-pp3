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

def forest_game():
    """
    Runs the forest themed game
    """

    answer = input('You find yourself at the edge of a dense forest. The entrance looks dark and mysterious.\nDo you:\na)Enter the forest\nb)Walk away and find a new adventure\n')
    if answer == 'a':
        answer = input('You enter the forest and walk along the winding path.\n The trees are tall and the leaves rustle in the wind.\n Suddenly you hear a loud grown.\nDo you:\na)Run away\nb)Investigate the source of the noise')
    else:
        print('You left the game\n')
    if answer == 'b':
        print('You follow the sound and find a wounded wolf. It looks at you with pleading eyes.\n Do you:\n a)Help the wolf \n b) Leave the wolf and continus on your journey')
    else:
        print('You ran away. Game over!!!')           

forest_game()    