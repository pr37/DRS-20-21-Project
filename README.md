# DRS-20-21-Project Documentation

# Introduction

This game is a variation of the classic Snake game by addition of multiple players with turn-based gameplay. Game is designed for competetive 2-4 player experiance. 
The goal of the game is for the user's snakes to remain the only survivors on the board. Each user has 3 venomous snakes. When hitting a wall, the user's snake dies, while hitting food increases the length of the snake by one field. with the body of the snake of another user, then that snake dies in the most severe torment. Each user is limited in time to 30 seconds. If he does not play a move in the given time, then he loses the right to it. If the user finishes the move, click move to the opponent. If the user does not want to play with the desired snake, the options Next Snake and Previous Snake are available, which transfers the control to the next or previous snake on the board.
This project was developed for DRS2021 class. 

# Arhitecture
Games arhitecture is comprised of main game and networking infrastructure which is server-client arhitecture. The main game is comprised of introductory scenes that welcome the player to the game, tell him information about the game and gives him the option of exiting. The main game is being run on the clients side. Each client will set up a main game for himself. After running the client and picking number of players from the introductory scene, the game will commence when all players are connected to the server. After they connect, an introductory packet data will be sent to the server so that the server knows which client has which id and whose turn it is. So to say, the game is comprised of three important entities: the server, the client and the main game. 
The main game relies on the 'Board' which is a class that holds all of the game state and information. It sets up the initial state and positions of player snakes, food and the walls. It handles logic for turning the player turn, spawning power up golden apples, updating the grid which holds the information of the positions of entities in the game.
The moving of the snakes is handled in the 'Movement' class and is also used in the 'Board' class. The Board is being initialised in the SnakeGame class which besides starting up the game also handles the games UI. The game entities that are condensed into separate classes are Food, GameObject, Player, PowerUp, Snake, Wall. All of these are being used by the Drawer class that will draw them onto the Board and handle draw events.


[![22.jpg](https://i.postimg.cc/852r1bhX/22.jpg)](https://postimg.cc/0MCNnDX7)


# User interface:

Start menu: 

![welcome-scene](https://i.postimg.cc/MKqFpDLj/rsz-screenshot-88.png)

There are 3 options on the User Interface:
  •	New Game – where the user selects the number of players to play
  
  ![mode-scene](https://i.postimg.cc/9fQ2w2NZ/rsz-screenshot-90.png)
  
  Play – by clicking on this button, the window for playing the game appears to the user (Previous and Next snake buttons give the user control over the previous / next snake, while pressing the End Turn button the user completes his round and lets the next player move)

  ![game](https://i.postimg.cc/nr9pcthZ/rsz-2screenshot-94.png)
  
  •	About Game – A window where the user is explained which commands are needed to move the snake in the game.
  
  ![about_scene](https://i.postimg.cc/wMsbR4ph/rsz-screenshot-92.png)
  
  

# Scenes
1.	Welcome_scene represents the initial scene which together with the other 3 builds the User Interface. In the main there is a logic for changing scenes.

2. 	Mode_scene – represents a scene in which the number of players is selected.The user can enter a minimum of 2 snakes for the game and a maximum of 4 snakes.

3.  About_scene – It presents a concise content of the Snake game as well as the way the game is played. The squares show the ways in which the user can move his snake in        the game.

4.	Win_scene – a scene that occurs when one of the players wins and tells which player is the winner.The text of the form "Player number x is the winner" is printed. Then the user has the opportunity to close the win window and turn off the game.

# Networking
The networking of the application is realised in a server-client arhitecture. Server hosts on a specified IP address and openes a specified port. It then listens for connections. Once the connection with a client is established, server listens for read and write events that come trough and from the connected network socket. The communication relies on non blocking TCP protocol. The client is built with the main game, and with the start of the client, the main game is initialised and started. After starting the client and within the client the main game, some initial game data will be sent to server containing the client id, so that when the next client joins he will be aware that there are other clients connected already. After all clients are connected the game can begin. The client whose turn it is can move his assigned snakes and end the turn. When the turn ends, all other connected clients will be updated with the newest game state update. When the server gets data from one client, he broadcasts the data (game state update) to other clients so that each client can have the updated game state.

# Visuals

If all the fields around the snake's head are filled, the snake dies.

![snake-captured](https://i.postimg.cc/XNdPqBkt/rsz-screenshot-106.png)      =======>    ![snake-died](https://i.postimg.cc/28T2LQb9/rsz-screenshot-107.png)


![snake-hungry](https://i.postimg.cc/hPxMMk5w/rsz-screenshot-110.png)

If a snake eats food, the snake grows.

![snake-full](https://i.postimg.cc/L82kDnfY/rsz-screenshot-111.png)


![snake-beforeWall](https://i.postimg.cc/1tvCDD4K/rsz-screenshot-114.png)

If a snake hits a wall, the snake dies.

![snake-hitTheWall](https://i.postimg.cc/XND1JKRj/rsz-screenshot-115.png)

# Usage
The objective of the game is to be the last player standing, ie. the only player with living snakes.
Each player have several snakes under his control. The snake that is currently "selected" (ready to be commanded with arrow keys) is marked with a red head. 

![selected-Snake](https://i.postimg.cc/mhw553b1/selected-Snake.png)

Notice the red head of the snake on the left, that is the snake that will respond to arrow key commands.

The turn player can cycle the selection of his snakes using "Next Snake" and "Previous Snake" buttons. Each snake can move several squares horizontally or vertically based on its lenght. As in classic Snake, picking up food increases snake lenght, and in so adds a extra move to the snake. Colliding with another snake or a wall kills the snake. The turn player can pass his turn with the "End Turn" button, or by his timer running down, allowing the next player to play. New food can spawn every turn and also move around. Randomly special golden apple can spawn as well, that will despawn in couple of turns. Picking up this golden apple may reward the player randomly with food-like behaviour or punish him by killing his snake. Also a snake can be captured and killed if the three squares; left, right and forward, relative to the snakes head, are occupied by either a snake or a wall.

![snake-Caputre](https://i.postimg.cc/6qTq3cPt/snake-Caputre.png)

If the yellow player moves the snake labeled with 1, snake number 2 would have squares left, forward and right of its head, (in absolute: squares below, left, and above the head) filled with snakes or walls, and in so trapping and killing snake 2.



