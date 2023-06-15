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
        shuffle_games()


# play_again()

def shuffle_games():
    """
    Shuffles through the games
    """
    game_list = [forest_game(), haunted_house_game(), city_game()]
    random.shuffle(game_list)
    print(game_list)


shuffle_games()


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
                answer = input(('You help the wolf and bandage its wounds. The wolf is greatful and leads you to a hidden clearing. In the center of the clearing, you see a chest.\n Do you: \n a)Open the chest\n b) Leave the chest and continue on your adventure\n'))
                if answer == 'a':
                    print('The chest was full of gold....You Won!')
                    exit(play_again())
                elif answer == 'b':
                    answer = input(
                        'You leave the wolf and chest behind and continue on your way. You come to a lake, there is a boat at the shore. Do you:\n a) Get into the boat \n b) Turn back \n')
                    if answer == 'a':
                        print('You get into the boat and start rowing out towards what appears to be an island. Suddenly a heavy fog closes in inparing your navigation. As you look over the sides of the boat you notice that theres 5 sharks circuling the boat. The boat begins to take on water and sinks. You are eaten by sharks.....Game over!')
                    elif answer == 'b':
                        answer = input(
                            'You turn around and head back along the path. The wolf is still waiting by the chest, he is gesturing again for you to open it. \n Do you: \n a)Open the chest \n b) Ignore the wolf and keep walking \n')
                        if answer == 'a':
                            print('The chest was full of gold....You Won!')
                            exit(play_again())
                        else:
                            print(
                                'You keep walking along the path until you fall through a trap door and die.....Game over!')
                            exit(play_again())
                answer = input(
                    'You continue along the path leaving the wolf behind. You come to a river with an old wooden bridge. do you:\n a) Cross the bridge \n b)Swim across the river?')
                if answer == 'a':
                    print(
                        'The bridge collapsed and you were eaten by alligators.....Game over!')
                    exit(play_again())
                else:
                    print(
                        'The river was full of alligators and you were eaten.....Game over!')
                    exit(play_again())

        else:
            print('You ran away, Game over!')

    else:
        print('You left the game\n')
        # run random game function when created
        exit(play_again())


# forest_game()


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


def crossroads_game():
    """
    Runs the crossroads game
    """
    answer = input('You find yourself standing at a crossroad, not knowing which path to take. You have two options: \n a)The mountain trail \n b) The coastal route \n')
    if answer == 'a':
        answer = input('Great choice! You decide to embark on the Mountain Trail. As you start your ascent, the air becomes crisper, and the scenery more breathtaking. The trail winds its way through dense pine forests and rocky terrain. After walking for a while, you stumble upon a fork in the path. You notice a signpost, but it is worn and difficult to read. There seem to be two options: \n a) The narrow pass \n b) The steep climb \n')
    elif answer == 'b':
        answer = input('')
