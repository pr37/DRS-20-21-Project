# DRS-20-21-Project Documentation

# Introduction

This game is a variation of the classic Snake game by addition of multiple players with turn-based gameplay. Game is designed for competetive 2-4 player experiance. This project was developed for DRS2021 class.

# Arhitecture
deja 

# Components
nikola,uros

User interface:

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
nikola, uros
1.	Welcome_scene represents the initial scene which together with the other 3 builds the User Interface. In the main there is a logic for changing scenes.

2. 	Mode_scene – represents a scene in which the number of players is selected

3.  About_scene – represents short instructions to the user for playing the game, ie for controlling the movement of snakes.

4.	Win_scene – a scene that occurs when one of the players wins and tells which player is the winner.

# Networking
The networking of the application is realised in a server-client arhitecture. Server hosts on a specified IP address and openes a specified port. It then listens for connections. Once the connection with a client is established, server listens for read and write events that come trough and from the connected network socket. The communication relies on non blocking TCP protocol. The client is built with the main game, and with the start of the client, the main game is initialised and started. After starting the client and within the client the main game, some initial game data will be sent to server containing the client id, so that when the next client joins he will be aware that there are other clients connected already. After all clients are connected the game can begin. The client whose turn it is can move his assigned snakes and end the turn. When the turn ends, all other connected clients will be updated with the newest game state update. When the server gets data from one client, he broadcasts the data (game state update) to other clients so that each client can have the updated game state.

# Visuals
jpg and gifs (iz naseg projekta)
nikola,uros

If all the fields around the snake's head are filled, the snake dies.

![snake-captured](https://i.postimg.cc/XNdPqBkt/rsz-screenshot-106.png)      =======>    ![snake-died](https://i.postimg.cc/28T2LQb9/rsz-screenshot-107.png)


![snake-hungry](https://i.postimg.cc/hPxMMk5w/rsz-screenshot-110.png)

If a snake eats food, the snake grows

![snake-full](https://i.postimg.cc/L82kDnfY/rsz-screenshot-111.png)


![snake-beforeWall](https://i.postimg.cc/1tvCDD4K/rsz-screenshot-114.png)

If a snake hits a wall, the snake dies

![snake-hitTheWall](https://i.postimg.cc/XND1JKRj/rsz-screenshot-115.png)

# Usage
The objective of the game is to be the last player standing, ie. the only player with living snakes.
Each player have several snakes under his control. The snake that is currently "selected" (ready to be commanded with arrow keys) is marked with a red head. 

![selected-Snake](https://i.postimg.cc/mhw553b1/selected-Snake.png)

Notice the red head of the snake on the left, that is the snake that will respond to arrow key commands.

The turn player can cycle the selection of his snakes using "Next Snake" and "Previous Snake" buttons. Each snake can move several squares horizontally or vertically based on its lenght. As in classic Snake, picking up food increases snake lenght, and in so adds a extra move to the snake. Colliding with another snake or a wall kills the snake. The turn player can pass his turn with the "End Turn" button, or by his timer running down, allowing the next player to play. New food can spawn every turn and also move around. Randomly special golden apple can spawn as well, that will despawn in couple of turns. Picking up this golden apple may reward the player randomly with food-like behaviour or punish him by killing his snake. Also a snake can be captured and killed if the three squares; left, right and forward, relative to the snakes head, are occupied by either a snake or a wall.

![snake-Caputre](https://i.postimg.cc/6qTq3cPt/snake-Caputre.png)

If the yellow player moves the snake labeled with 1, snake number 2 would have squares left, forward and right of its head, (in absolute: squares below, left, and above the head) filled with snakes or walls, and in so trapping and killing snake 2.



