# ADVENTURE run!

This game was created as part of my Full Stack Diploma course. It is a fully interactive adventure game with multiple endings. There are 2 seperate storylines. One story starts at the entrance of a forest, the other at a crossroads. The aim of the game is to choose your own path leading to a variety of endings. 

[HERE is the live game](https://adventure-game3-250fc2c720c9.herokuapp.com/)

![Responsive image](assets/images/Screenshot%202023-06-18%20054155.png)


## How to play



- Click on run program if game has not started automatically, or at any point to restart game.

- You will be prompted for your name. It is a requirement to enter a name.

- Once you input a username press enter.

- You will be presented with your first scenario.

- Choose between a or b and press enter.

- If you chose anything other than a or b you will recieve an error and will be asked to re-enter your answer.

- Depending on your choice you will be presented with a new scenario.

- The game will continue until you come to and ending.

- Once the game ends you will prompted on whether you wish to play again or not. Enter either yes or no.

- If you decide to play again the game will start over, randomly choosing between 2 possible games.



**Features**

- Random generation between two possible games.

- Colorized text for easier reading and a better experience

![Colorized text image](assets/images/Screenshot%202023-06-18%20053527.png)

- Choose between a variety of possible endings.

- Fully interactive game, with prompts and errors thrown to guide you, if incorrect input is inserted.


**Future Features**

- Add more games 

- Expand current storylines.


**Data Model**

 I Built each game using if/elif statements, nested and within functions. I used a while loop to get username and validate its input. I also used while loops for play again function, input validation and shuffle games function.


**Testing**

- Passed the code through a pep8 linter. 

- Manually went through the game in great detail testing that all error handling was working correctly.

- Tested in my local terminal and the Code Institute heroku terminal.


**Bugs/Problems/Fixes**

- Line too long errors showing. I kept it as compact as possible, the lines are text from the storyline, not code, so its not an issue regarding functioning or readibility.

![Errors found](assets/images/Screenshot%202023-06-18%20061421.png)


**Deployment**

This project was deployed using Code Institute's mock terminal for heroku.

- Steps for deployment.

- Fork or clone this repository.

- Create a new heroku app.

- Set the buildbacks to python and nodeJS in that order.

- Link the heroku app to the repository.

- Click on deploy.


**Credits**

- Code Institute for the deployment terminal.

- Code Institute for the README template.

- Chat gpt for the game storyline.

- assets/images/Screenshot 2023-06-18 054155.png for responsive image.

- assets/images/Screenshot 2023-06-18 054155.png for tutorial on how to install and use colorama.





