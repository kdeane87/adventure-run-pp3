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
        if answer == 'a':
            answer = input('You decide to take the Narrow Pass. The path becomes increasingly narrow and steep as you make your way through the rugged mountainside. The air feels cooler, and you can hear the sound of rushing water in the distance. As you continue, you encounter a fallen tree blocking the path. It seems like you will not be able to pass through it easily. What would you like to do? \n a) Attempt to climb over the fallen tree \n b) Look for an alternative route \n')
            if answer == 'a':
                answer = input('You decide to attempt to climb over the fallen tree. With careful steps and a bit of effort, you manage to scramble over the obstacle and continue along the Narrow Pass. The trail starts to descend gradually, and you can hear the sound of a nearby waterfall growing louder. As you approach the source of the sound, you come across a stunning waterfall cascading down a series of rocky cliffs. It is a breathtaking sight. However, the path ahead seems to split into two distinct routes: \n a) Follow the path leading closer to the waterfall \n b) Take the path that veers away from the waterfall')
                if answer == 'a':
                    answer = input('You choose to follow the path leading closer to the waterfall. The sound of rushing water becomes even more thunderous as you approach. The path becomes misty, and you can feel a refreshing spray on your face. The closer you get, the more mesmerizing the waterfall becomes, its powerful currents crashing against the rocks below. As you stand in awe, you notice a small cave tucked behind the waterfall. It is shrouded in mystery and beckons you to explore its depths. What would you like to do? \n a) Enter the cave and explore its secrets \n b) Continue along the path, leaving the cave behind \n')
                    if answer = 'a':
                        print('You decide to enter the cave and explore its secrets. With cautious steps, you make your way through the veil of the waterfall and enter the dark, damp cave. Inside, the sound of the waterfall is muffled, and a sense of mystery fills the air. As you venture deeper into the cave, you notice faint glimmers of light coming from an opening up ahead. Your curiosity drives you forward, and as you reach the opening, you find yourself in a hidden chamber adorned with sparkling crystals. The sight is truly awe-inspiring. However, as you marvel at the beauty around you, you unintentionally trigger a hidden mechanism. The chamber starts to rumble, and the entrance you came through begins to close. Panicking, you search for a way out but find yourself trapped. Unfortunately, this marks the end of your adventure. Remember, in the unpredictable world of exploration, every choice carries consequences. Feel free to start a new adventure, and may luck be on your side next time!')
                        exit(play_again)
                elif answer == 'b':
                    answer = input('')
            elif answer == 'b':
                answer = input('')
        elif answer == 'b':
            answer = input('')
    elif answer == 'b':
        answer = input('')
