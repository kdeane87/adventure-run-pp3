"""Imports random used for shuffle_games and colorama for text color"""
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def get_username():
    """
    Gets the players name
    """
    print('Hello')
    while True:
        username = input('Enter username:').strip()
        if username == '':
            print(Fore.RED + 'You must enter a username')
            continue
        elif len(username) > 15:
            print('Error! Only 15 characters allowed!')
            continue
        else:
            print(Fore.BLUE + 'Welcome', Fore.GREEN +
                  username, Fore.BLUE + 'lets get started')
            break

    shuffle_games()

    return get_username


def input_validation(prompt, options):
    '''
    Validates the users input
    '''
    while True:
        print()
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input

        else:
            print(Fore.RED + "invalid input. Please try again.")

    return input_validation


def play_again():
    '''
    This is called after game is over and gives choice to play again
    '''
    valid_characters = ('yes', 'no')

    while True:
        print(Fore.GREEN +
              'Do you want to play again? \n yes or no')
        user_input = input('')

        if user_input not in valid_characters:
            print(Fore.RED + 'INVALID: Enter either yes or no!')

        elif user_input == 'no':
            print(f'You entered {user_input}, Goodbye!')
            break

        else:
            shuffle_games()

    return play_again


def crossroads_game():
    """
    Runs the crossroads game
    """

    print(Fore.WHITE +
          'You find yourself standing at a crossroad,\n'
          'not knowing which path to take.\n'
          )
    answer = input_validation(Fore.BLUE +
                              'You have two options:\n'
                              'a)The mountain trail\n'
                              'b) The coastal route \n', ['a', 'b'])
    if answer == 'a':
        print(Fore.WHITE +
              'Great choice! You decide to embark on the Mountain Trail.\n'
              'As you start your ascent, the air becomes crisper,\n'
              'and the scenery more breathtaking.\n'
              'The trail winds its way through dense pine forests\n'
              'and rocky terrain.\n'
              'After walking for a while,\n'
              'you stumble upon a fork in the path.\n'
              'You notice a signpost, but it is worn and difficult to read.\n'
              )
        answer = input_validation(Fore.BLUE +
                                  'There seem to be two options:\n'
                                  'a) The narrow pass\nb) The steep climb\n', ['a', 'b'])
        if answer == 'a':
            print(Fore.WHITE +
                  'You decide to take the Narrow Pass.\n'
                  'The path becomes increasingly narrow and\n'
                  'steep as you make your way through the rugged mountainside.\n'
                  'The air feels cooler, and you can hear the sound\n'
                  'of rushing water in the distance.\n'
                  'As you continue,\n'
                  'you encounter a fallen tree blocking the path.\n'
                  'It seems like you will not be able to pass through it easily.\n'
                  )
            answer = input_validation(Fore.BLUE +
                                      'What would you like to do?\n'
                                      'a) Attempt to climb over the fallen tree \n'
                                      'b) Look for an alternative route \n', ['a', 'b'])
            if answer == 'a':
                print(Fore.WHITE +
                      'You decide to attempt to climb over the fallen tree.\n'
                      'With careful steps and a bit of effort,\n'
                      'you manage to scramble over the obstacle and\n'
                      'continue along the Narrow Pass.\n'
                      'The trail starts to descend gradually,\n'
                      'and you can hear the sound of a nearby waterfall growing louder.\n'
                      'As you approach the source of the sound,\n'
                      'you come across a stunning waterfall cascading down a series of rocky cliffs.\n'
                      'It is a breathtaking sight.\n'
                      'However, the path ahead seems to split into two distinct routes:\n'
                      'a) Follow the path leading closer to the waterfall\n'
                      'b) Take the path that veers away from the waterfall\n')
                answer = input_validation(Fore.BLUE +
                                          'However, the path ahead seems to split into two distinct routes:\n'
                                          'a) Follow the path leading closer to the waterfall\n'
                                          'b) Take the path that veers away from the waterfall\n', ['a', 'b'])
                if answer == 'a':
                    print(Fore.WHITE +
                          'You choose to follow the path leading closer to the waterfall.\n'
                          'The sound of rushing water becomes even more thunderous as you approach.\n'
                          'The path becomes misty, and you can feel a refreshing spray on your face.\n'
                          'The closer you get, the more mesmerizing the waterfall becomes,\n'
                          'its powerful currents crashing against the rocks below.\n'
                          'As you stand in awe, you notice a small cave tucked behind the waterfall.\n'
                          'It is shrouded in mystery and beckons you to explore its depths.\n'
                          )
                    answer = input_validation(Fore.BLUE +
                                              'What would you like to do?\n'
                                              'a) Enter the cave and explore its secrets\n'
                                              'b) Continue along the path, leaving the cave behind \n', ['a', 'b'])
                    if answer == 'a':
                        print(Fore.WHITE +
                              'You decide to enter the cave and explore its secrets.\n'
                              'With cautious steps, you make your way through the\n'
                              'veil of the waterfall and enter the dark, damp cave.\n'
                              'Inside, the sound of the waterfall is muffled,\n'
                              'and a sense of mystery fills the air.\n'
                              'As you venture deeper into the cave,\n'
                              'you notice faint glimmers of light coming from an opening up ahead.\n'
                              'Your curiosity drives you forward, and as you reach the opening,\n'
                              'you find yourself in a hidden chamber adorned with sparkling crystals.\n'
                              'The sight is truly awe-inspiring. However,\n'
                              'as you marvel at the beauty around you, you unintentionally trigger a hidden mechanism.\n'
                              'The chamber starts to rumble,\n'
                              'and the entrance you came through begins to close.\n'
                              'Panicking, you search for a way out but find yourself trapped.\n'
                              'Unfortunately, this marks the end of your adventure.\n'
                              'Remember, in the unpredictable world of exploration,\n'
                              'every choice carries consequences.\n'
                              'Feel free to start a new adventure,\n'
                              'and may luck be on your side next time!\n')
                        exit(play_again())
                    elif answer == 'b':
                        print(Fore.WHITE +
                              'You decide to continue along the path, leaving the cave behind.\n'
                              'As you proceed, the trail begins to wind its way down the mountain,\n'
                              'gradually leading you back to lower elevations.\n'
                              'The scenery changes as you descend,\n'
                              'transitioning from rocky cliffs to lush greenery and\n'
                              'vibrant wildflowers.\n'
                              'After a while, you reach the end of the Mountain Trail.\n'
                              'Congratulations! You have successfully completed your adventure\n'
                              'through the mountains, experiencing its challenges and beauty.\n'
                              'Take a moment to appreciate the journey you have had and\n'
                              'the memories you have made.\n'
                              'Thank you for playing the interactive adventure game!\n'
                              'If you would like to embark on another adventure\n'
                              'or explore a different path, feel free to start a new game.\n')
                        exit(play_again())
                elif answer == 'b':
                    print(Fore.WHITE +
                          'You decide to take the path that veers away from the waterfall.\n'
                          'As you move away from the captivating sight of the waterfall,\n'
                          'the trail leads you deeper into the mountainous terrain.\n'
                          'The path gradually becomes steeper and more challenging to navigate.\n'
                          'After a while, you stumble upon an ancient stone bridge spanning a deep ravine.\n'
                          'The bridge appears old and weathered,\n'
                          'with some missing stones and cracks.\n'
                          'It looks risky too cross.\n'
                          )
                    answer = input_validation(Fore.BLUE +
                                              'What would you like to do?\n'
                                              'a) Take a leap of faith and try to cross the bridge\n'
                                              'b) Look for an alternative route to bypass the bridge\n', ['a', 'b'])
                    if answer == 'a':
                        print(Fore.WHITE +
                              'You gather your courage and decide to take a leap of faith,\n'
                              'attempting to cross the old stone bridge.\n'
                              'Each step feels precarious as you carefully navigate\n'
                              'the missing stones and gaps.\n'
                              'The ravine below sends shivers down your spine,\n'
                              'but you push forward, determined to reach the other side.\n'
                              'Midway across the bridge, you hear a loud crack,\n'
                              'and the bridge gives way beneath your weight.\n'
                              'You desperately try to grab onto something, but it is too late.\n'
                              'You plummet into the ravine, unable to escape the fall.\n'
                              'Unfortunately, your journey ends here.\n'
                              'Thank you for playing the interactive adventure game.\n'
                              'Would you like to start again?\n')
                        exit(play_again())
                    elif answer == 'b':
                        print(Fore.WHITE +
                              'You decide to look for an alternative route to bypass the bridge.\n'
                              'Carefully scanning the surroundings,\n'
                              'you notice a narrow trail leading down the ravine.\n'
                              'It seems like a challenging but possible route to continue your journey.\n'
                              'As you descend down the narrow trail,\n'
                              'the terrain becomes increasingly treacherous.\n'
                              'Loose rocks and slippery slopes make it difficult to maintain your footing.\n'
                              'However, your determination pushes you forward.\n'
                              'Eventually, you reach the bottom of the ravine,\n'
                              'where you find a hidden cave entrance.\n'
                              'Curiosity piques your interest,\n'
                              'and you decide to explore it further.\n'
                              'Inside the cave, you discover a hidden treasure trove\n'
                              'filled with precious gems and ancient artifacts.\n'
                              'Congratulations! You have successfully found the hidden treasure\n'
                              'and completed your adventure.\n'
                              'You can now revel in your newfound riches\n'
                              'and relish the memories of your daring mountain trail journey.\n'
                              'Well done!\n')
                        exit(play_again())
            elif answer == 'b':
                print(Fore.WHITE +
                      'You choose to look for an alternate route around the fallen tree.\n'
                      'After carefully scouting the area,\n'
                      'you spot a narrow path that veers off to the side, bypassing the obstacle.\n'
                      'You navigate through the path,\n'
                      'squeezing between rocks and shrubs until you successfully circumvent the fallen tree.\n'
                      'As you continue on the Narrow Pass,\n'
                      'the terrain becomes even more treacherous.\n'
                      'The path narrows to a mere ledge with a sheer drop on one side.\n'
                      'The winds pick up, making it challenging to maintain your balance.\n'
                      'Suddenly, a heavy fog rolls in, reducing visibility to almost zero.\n'
                      'You find yourself disoriented and unsure of which direction to proceed.\n'
                      'Every step feels uncertain,\n'
                      'and the danger of slipping off the edge becomes even more real.\n'
                      'With no clear path forward and the risks escalating,\n'
                      'you decide it is best to turn back and find an alternative route.\n'
                      'You carefully retrace your steps, keeping close to the mountain wall for safety.\n'
                      'You make it back to the fork in the path\n'
                      'and decide to choose a different option on your next adventure.\n'
                      'Thank you for playing!\n'
                      'If you would like to try again or explore a different path,\n'
                      'feel free to start a new game.\n')
                exit(play_again())
        elif answer == 'b':
            print(Fore.WHITE +
                  'You decide to take on the Steep Climb.\n'
                  'As you begin your ascent, the trail becomes steeper and more challenging.\n'
                  'The path zigzags up the mountainside,\n'
                  'and you find yourself using your hands to scramble over rocks at some points.\n'
                  'As you near the top, you encounter a small cave entrance hidden among the rocks.\n'
                  'It piques your curiosity.\n'
                  )
            answer = input_validation(Fore.BLUE +
                                      'Will you enter the cave or continue on the trail?\n'
                                      'a) Enter the cave\n'
                                      'b) Continue on the trail\n', ['a', 'b'])
            if answer == 'a':
                print(Fore.WHITE +
                      'You bravely decide to enter the cave,\n'
                      'intrigued by what secrets it might hold.\n'
                      'The inside of the cave is dimly lit,\n'
                      'and you can hear the sound of dripping water echoing through the chamber.\n'
                      'As you cautiously make your way deeper into the cave,\n'
                      'you stumble upon a hidden treasure chest resting on a stone pedestal.\n'
                      'You approach the chest with a mix of excitement and trepidation.\n'
                      'With trembling hands, you slowly lift the lid,\n'
                      'and to your amazement, it reveals a dazzling array of jewels,\n'
                      'gold coins, and ancient artifacts.\n'
                      'You have stumbled upon a long-lost treasure!\n'
                      'Overwhelmed by your discovery, you realize that\n'
                      'this adventure has come to a fortunate end.\n'
                      'With the treasure in your possession,\n'
                      'you exit the cave and make your way back down the mountain,\n'
                      'carrying the memories of this incredible journey with you.\n'
                      'Congratulations on completing the adventure!\n'
                      'Thank you for playing.\n'
                      'If you would like to embark on another adventure,\n'
                      'feel free to start a new game.\n')
                exit(play_again())
            elif answer == 'b':
                print(Fore.WHITE +
                      'You decide to continue on the trail, leaving the cave behind for now.\n'
                      'The path becomes less steep,\n'
                      'and you can see the magnificent view opening up before you.\n'
                      'The sun shines brightly,\n'
                      'casting a golden glow on the surrounding peaks and valleys.\n'
                      'As you hike further,\n'
                      'you notice a peculiar object glinting in the distance.\n'
                      'As you approach,\n'
                      'you realize it is a weathered treasure chest half-buried in the ground.\n'
                      'It seems like a relic from a bygone era.\n'
                      )
                answer = input_validation(Fore.BLUE +
                                          'What will you do?\n'
                                          'a) Open the treasure chest\n'
                                          'b) Leave the treasure chest and continue on the trail\n', ['a', 'b'])
                if answer == 'a':
                    print(Fore.WHITE +
                          'You cannot resist the allure of the treasure chest and decide to open it.\n'
                          'With a creak, the lid swings open,\n'
                          'revealing a sparkling collection of jewels,\n'
                          'gold coins, and ancient artifacts.\n'
                          'You have stumbled upon a treasure trove!\n'
                          'Congratulations!\n'
                          'You have successfully completed the adventure by finding the hidden treasure.\n'
                          'You can now bask in your newfound wealth\n'
                          'and enjoy the rest of your journey knowing that you have had a truly remarkable adventure.\n')
                    exit(play_again())
                elif answer == 'b':
                    print(Fore.WHITE +
                          'Oh no!\n'
                          'As you decide to leave the treasure chest behind and continue on the trail,\n'
                          'an unexpected turn of events occurs.\n'
                          'Without warning, the ground beneath you gives way,\n'
                          'and you find yourself falling into a hidden crevice.\n'
                          'The fall proves fatal, and your adventure comes to an untimely end.\n'
                          'Thank you for playing the interactive adventure game!\n'
                          'If you would like to try again or explore a different path,\n'
                          'feel free to start a new game.\n')
                    exit(play_again())
    elif answer == 'b':
        print(Fore.WHITE +
              'You decide to take the Coastal Route.\n'
              'As you walk along the path,\n'
              'the sound of crashing waves fills the air,\n'
              'and a refreshing sea breeze brushes against your face.\n'
              'The path winds its way along rugged cliffs,\n'
              'offering breathtaking views of the sparkling ocean below.\n'
              'After walking for a while, you come across a small fishing village.\n'
              'The villagers are friendly and offer you a warm welcome.\n'
              'They tell you about a legendary treasure hidden on a nearby island\n'
              'but warn you about the dangerous sea creatures that guard it.\n'
              )
        answer = input_validation(Fore.BLUE +
                                  'You have two choices:\n'
                                  'a) Embark on a boat to search for the hidden treasure\n'
                                  'b) Explore the village and interact with the villagers\n', ['a', 'b'])
        if answer == 'a':
            print(Fore.WHITE +
                  'Excited by the prospect of finding the hidden treasure,\n'
                  'you decide to embark on a boat and set off on your adventure.\n'
                  'The villagers provide you with a sturdy vessel\n'
                  'and a map that marks the location of the island where\n'
                  'the treasure is said to be hidden.\n'
                  'As you row further away from the village,\n'
                  'the sea becomes rougher, and dark clouds gather in the sky.\n'
                  'The waves crash against the sides of the boat,\n'
                  'testing your determination.\n'
                  'But you push forward, fueled by the allure of the treasure.\n'
                  'After what feels like an eternity of battling the elements,\n'
                  'you finally spot the island on the horizon.\n'
                  'It is surrounded by treacherous rocks and strong currents.\n'
                  'As you approach,\n'
                  'you notice a cave entrance that seems to lead deeper into the island.\n'
                  )
            answer = input_validation(Fore.BLUE +
                                      'You have two choices:\n'
                                      'a) Navigate through the treacherous rocks and currents to reach the cave entrance\n'
                                      'b) Anchor the boat and explore the shoreline of the island\n', ['a', 'b'])
            if answer == 'a':
                print(Fore.WHITE +
                      'With determination in your heart,\n'
                      'you carefully navigate through the treacherous rocks and currents,\n'
                      'steering the boat towards the cave entrance.\n'
                      'The waves crash against the sides of the vessel,\n'
                      'challenging your skill as a sailor.\n'
                      'After a heart-pounding journey, you successfully enter the cave.\n'
                      'Inside, you find yourself surrounded by darkness,\n'
                      'the only source of light coming from a small opening above.\n'
                      'As you explore deeper, the cave starts to reveal its secrets.\n'
                      'You stumble upon a series of puzzles\n'
                      'and challenges that guard the path to the treasure.\n'
                      'It seems the ancient guardians of the treasure have set up these obstacles\n'
                      'to protect it from intruders like yourself.\n'
                      )
                answer = input_validation(Fore.BLUE +
                                          'You have two choices:\n'
                                          'a) Take on the puzzles and challenges head-on,\n'
                                          'solving each one as you progress deeper into the cave\n'
                                          'b) Retreat from the cave and explore the islands shoreline instead\n', ['a', 'b'])
                if answer == 'a':
                    print(Fore.WHITE +
                          'Oh no!\n'
                          'As you bravely take on the puzzles and challenges,\n'
                          'you encounter a particularly tricky one that triggers a trap.\n'
                          'Suddenly, the ground beneath you gives way,\n'
                          'and you plummet into a deep chasm.\n'
                          'Your adventure comes to an unfortunate end\n'
                          'as you meet your demise\n')
                    exit(play_again())
                elif answer == 'b':
                    print(Fore.WHITE +
                          'Deciding to take a break from the puzzles and challenges in the cave,\n'
                          'you retreat back to the shoreline of the island.\n'
                          'As you explore, you come across a secluded beach\n'
                          'with shimmering golden sand.\n'
                          'The soothing sound of the waves crashing against the shore\n'
                          'relaxes your mind.\n'
                          'While walking along the beach, you notice an old,\n'
                          'weathered map half-buried in the sand.\n'
                          'Curiosity piqued, you pick it up and examine it closely.\n'
                          'It appears to be a treasure map,\n'
                          'indicating the location of another hidden treasure somewhere on the island.\n'
                          )
                    answer = input_validation(Fore.BLUE +
                                              'You have two choices:\n'
                                              'a) Follow the clues on the map and embark on a new treasure hunt\n'
                                              'b) Return to the cave and resume tackling the puzzles and challenges\n', ['a', 'b'])
                    if answer == 'a':
                        print(Fore.WHITE +
                              'Oh no!\n'
                              'As you follow the clues on the map,\n'
                              'you find yourself in a dense jungle,\n'
                              'filled with unknown dangers and obstacles.\n'
                              'The path becomes increasingly treacherous,\n'
                              'and you accidentally trigger a hidden trap.\n'
                              'Suddenly, a spiked net falls from above,\n'
                              'trapping you and causing severe injuries.\n'
                              'With no one around to help, your adventure sadly comes to an abrupt end.\n')
                        exit(play_again())
                    elif answer == 'b':
                        print(Fore.WHITE +
                              'As you make your way back to the cave,\n'
                              'ready to face the puzzles and challenges once again,\n'
                              'a sudden and unexpected event occurs.\n'
                              'The ground beneath you starts to shake violently,\n'
                              'and the walls of the cave begin to crumble.\n'
                              'Rocks and debris rain down, blocking your path and trapping you inside.\n'
                              'Despite your best efforts to escape,\n'
                              'the collapsing cave proves to be too dangerous.\n'
                              'Tragically, you are unable to find a way out,\n'
                              'and the adventure comes to an unfortunate end.\n')
                        exit(play_again())
            elif answer == 'b':
                print(Fore.WHITE +
                      'Congratulations!\n'
                      'You choose to anchor the boat and explore the shoreline of the island.\n'
                      'As you step onto the sandy beach,\n'
                      'you feel a sense of anticipation and wonder.\n'
                      'The island is lush and vibrant,\n'
                      'with exotic plants and colorful flowers adorning the landscape.\n'
                      'As you venture further inland,\n'
                      'you stumble upon a hidden path that leads you to a series of ancient ruins.\n'
                      'The ruins are overrun with vegetation,\n'
                      'but you can still see traces of intricate carvings and faded murals on the walls.\n'
                      'Curiosity fuels your desire to uncover the secrets of this forgotten civilization.\n'
                      'You explore the ruins, carefully navigating through crumbling corridors and chambers.\n'
                      'Finally, you come across a hidden chamber at the heart of the ruins.\n'
                      'Inside, you discover a pedestal adorned with ancient symbols.\n'
                      'At the center of the pedestal lies a magnificent gemstone,\n'
                      'glowing with an otherworldly brilliance.\n'
                      'You have found the legendary treasure!\n'
                      'As you reach out to grasp the gemstone,\n'
                      'a surge of energy courses through your body.\n'
                      'The treasure is said to possess mystical powers,\n'
                      'and you can feel its magic enveloping you.\n'
                      'You have achieved what many adventurers have dreamed of.\n'
                      'With the treasure in your possession,\n'
                      'you make your way back to the village.\n'
                      'The villagers celebrate your triumph\n'
                      'and express their gratitude for bringing back a piece of their islands history.\n'
                      'You have successfully completed your adventure,\n'
                      'and your name will be forever etched in the annals of treasure hunters.\n'
                      'Well done, and thank you for playing!\n'
                      'If you would like to embark on another adventure, feel free to start again.\n')
                exit(play_again())

        elif answer == 'b':
            print(Fore.WHITE +
                  'You decide to explore the village and interact with the villagers.\n'
                  'As you engage in conversations and\n'
                  'learn more about their way of life,\n'
                  'you start to feel a sense of belonging and\n'
                  'decide to stay in the village for a while.\n'
                  'You enjoy the peaceful atmosphere,\n'
                  'savoring delicious seafood and listening to the stories of the villagers.\n'
                  'Days turn into weeks, and before you know it,\n'
                  'months have passed.\n'
                  'While you have found contentment in the village,\n'
                  'you cannot help but wonder about the hidden treasure\n'
                  'that was mentioned earlier.\n'
                  'Regretfully, you realize that you may have missed out on a great\n'
                  'adventure.\n'
                  'However, life in the village brings its own joys and experiences,\n'
                  'and you find happiness in the simple pleasures it offers.\n'
                  'Congratulations!\n'
                  'Though you did not embark on a treasure hunt,\n'
                  'you found fulfillment in the village and\n'
                  'forged connections with its residents.\n'
                  'Remember, every choice in an adventure game leads to a unique outcome.\n'
                  'If you would like, we can start a new adventure.\n'
                  'Let me know if you are ready to try again!\n')
            exit(play_again())

    return crossroads_game


def forest_game():
    """
    Runs the forest themed game
    """
    print(Fore.WHITE +
          'You find yourself at the edge of a dense forest.\n'
          'The entrance looks dark and mysterious.\n'
          )
    answer = input_validation(Fore.BLUE +
                              'Do you:\n'
                              'a)Enter the forest\n'
                              'b)Walk away and find a new adventure\n', ['a', 'b'])
    if answer == 'a':
        print(Fore.WHITE +
              'You enter the forest and walk along the winding path.\n'
              'The trees are tall and the leaves rustle in the wind.\n'
              'Suddenly you hear a loud growl.\n'
              )
        answer = input_validation(Fore.BLUE +
                                  'Do you:\n'
                                  'a)Run away\n'
                                  'b)Investigate the source of the noise\n', ['a', 'b'])
        if answer == 'b':
            print(Fore.WHITE +
                  'You follow the sound and find a wounded wolf.\n'
                  'It looks at you with pleading eyes.\n'
                  )
            answer = input_validation(Fore.BLUE +
                                      'Do you:\n'
                                      'a)Help the wolf \n'
                                      'b) Leave the wolf and continus on your journey\n', ['a', 'b'])
            if answer == 'a':
                print(Fore.WHITE +
                      'You help the wolf and bandage its wounds.\n'
                      'The wolf is greatful and leads you to a hidden clearing.\n'
                      'In the center of the clearing, you see a chest.\n'
                      )
                answer = input_validation(Fore.BLUE +
                                          'Do you:\n'
                                          'a)Open the chest\n'
                                          'b) Leave the chest and continue on your adventure\n', ['a', 'b'])
                if answer == 'a':
                    print(Fore.WHITE + 'The chest was full of gold....You Won!')
                    exit(play_again())
                elif answer == 'b':
                    print(Fore.WHITE +
                          'You leave the wolf and chest behind and continue on your way.\n'
                          'You come to a lake, there is a boat at the shore.\n'
                          )
                    answer = input_validation(Fore.BLUE +
                                              'Do you:\n'
                                              'a) Get into the boat\n'
                                              'b) Turn back \n', ['a', 'b'])
                    if answer == 'a':
                        print(Fore.WHITE +
                              'You get into the boat and start rowing out towards what appears to be an island.\n'
                              'Suddenly a heavy fog closes in inparing your navigation.\n'
                              'As you look over the sides of the boat you notice that\n'
                              'theres 5 sharks circuling the boat.\n'
                              'The boat begins to take on water and sinks.\n'
                              'You are eaten by sharks.....Game over!\n')
                        exit(play_again())
                    elif answer == 'b':
                        print(Fore.WHITE +
                              'You turn around and head back along the path.\n'
                              'The wolf is still waiting by the chest,\n'
                              'he is gesturing again for you to open it.\n'
                              )
                        answer = input_validation(Fore.BLUE +
                                                  'Do you:\n'
                                                  'a)Open the chest\n'
                                                  'b) Ignore the wolf and keep walking \n', ['a', 'b'])
                        if answer == 'a':
                            print(Fore.WHITE +
                                  'The chest was full of gold....You Won!')
                            exit(play_again())
                        elif answer == 'b':
                            print(Fore.WHITE +
                                  'You keep walking along the path until you fall through a trap door and die.....Game over!')
                        exit(play_again())
                    print(Fore.WHITE +
                          'You continue along the path leaving the wolf behind.\n'
                          'You come to a river with an old wooden bridge.\n'
                          )
                    answer = input_validation(Fore.BLUE +
                                              'Do you:\n'
                                              'a) Cross the bridge \n'
                                              'b)Swim across the river?\n', ['a', 'b'])
                if answer == 'a':
                    print(Fore.WHITE +
                          'The bridge collapsed and you were eaten by alligators.....Game over!')
                    exit(play_again())
                elif answer == 'b':
                    print(Fore.WHITE +
                          'The river was full of alligators and you were eaten.....Game over!')
                    exit(play_again())
        elif answer == 'a':
            print(Fore.WHITE + 'You ran away, Game over!')
            exit(play_again())
    elif answer == 'b':
        print(Fore.WHITE + 'You left the game\n')
        exit(play_again())

    return forest_game


def shuffle_games():
    """
    shuffles through the games
    """
    games_list = [crossroads_game, forest_game]

    while games_list:
        random_game = random.choice(games_list)
        random_game()
        games_list.remove(random_game)

    return shuffle_games


def main():
    """
    Main function that calls all functions
    """
    get_username()
    play_again()

    return main


main()
