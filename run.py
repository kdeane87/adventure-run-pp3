import random


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


# play_again()

# def shuffle_games():
    """
    Shuffles through the games
    """


def forest_game():
    """
    Runs the forest themed game
    """

    answer = input('You find yourself at the edge of a dense forest. The entrance looks dark and mysterious.\n Do you:\n a)Enter the forest\n b)Walk away and find a new adventure\n')
    if answer == 'a':
        answer = input('You enter the forest and walk along the winding path.\n The trees are tall and the leaves rustle in the wind.\n Suddenly you hear a loud growl.\nDo you:\n a)Run away\n b)Investigate the source of the noise\n')
        if answer == 'b':
            answer = input(
                'You follow the sound and find a wounded wolf. It looks at you with pleading eyes.\n Do you:\n a)Help the wolf \n b) Leave the wolf and continus on your journey\n')
            if answer == 'a':
                answer = input(('You help the wolf and bandage its wounds. The wolf is greatful and leads you to a hidden clearing. In the center of the clearing, you see a chest.\n Do you: \n a)Open the chest\n b) Leave the chest and continueon your adventure\n'))
                if answer == 'a':
                    print('the chest blew up')
                else:
                    print('should have opened the chest')
            else:
                print('ah the poor wolf')

        else:
            print('you ran away')

    else:
        print('You left the game\n')
        # run random game function when created
        exit(play_again())


forest_game()


def haunted_house_game():
    """
    Runs the haunted house game
    """
    answer = input('You find yourself standing outside the foreboding Ravenwood Manor. The moon is full, casting an eerie glow on the dilapidated structure. As you approach the front door, it creaks open, beckoning you inside. Are you brave enough to step into the haunted house?/n a) Enter the manor.\n b) Turn back and leave.')
    if answer == 'a':
        a = """
        You gather your courage and step across the threshold of Ravenwood Manor. The door slams shut behind you, enveloping you in darkness. The air feels heavy, and a chill runs down your spine. You must find a way to uncover the secrets of this haunted house and escape its clutches.

        You find yourself in a dimly lit foyer. Cobwebs hang from the ceiling, and dust covers the old furniture. To your left, you notice a grand staircase leading to the upper floors. To your right, a corridor disappears into the darkness.\n a) Ascend the staircase.\n b) Explore the corridor.
            """
        print(a)
        answer
    else:
        a = """
        You chose to exit the game, thats probably a wise choice!!!
        """
        print(a)
        exit(play_again)

    if answer == 'a':
        a = """ 
        You cautiously make your way up the stairs, each step groaning beneath your weight. As you reach the top, you find yourself in a narrow corridor lined with closed doors. A faint draft rustles through the hallway, carrying whispers that echo through the air.\n a)Open the first door on the left.\n b) Open the last door on the right.   
            """
        print(a)
    else:
        a = """
        You walk down the corridor. You come to a left turn. Theres a man in the distance, he starts to approach you. Suddenly there is a flash.......GUNSHOT....... You have been Killed. the end!!!
        """
        print(a)
        exit(play_again)

# haunted_house_game()


def city_game():
    """
    Runs the city game
    """
    answer = input('Once upon a time, in the bustling city of Eldoria, there lived a brave and curious young woman named Maya. Maya had always been fascinated by legends of hidden treasures, and her heart yearned for adventure. One day, she stumbled upon an ancient map that depicted a mysterious island shrouded in legends and untold riches. Filled with excitement and determination, Maya decided to set sail in search of this legendary island.Maya gathers her supplies and sets sail. After days of navigating treacherous waters, a dense fog engulfs the ship, making it impossible to see the way forward.\n What should Maya do?\n a) Wait on the ship until the fog clears.\n b) Venture into the fog and try to find a way through.')
    if answer == 'a':
        a = """
         Maya decides to wait on the ship until the fog clears. She trusts that patience and caution are the keys to navigating unknown waters safely. As she waits, the fog slowly begins to dissipate, revealing the sight of a magnificent island in the distance.
          """
        print(a)
    else:
        a = """
        You chose to exit the game!!!
        """
        print(a)
        exit(play_again)
