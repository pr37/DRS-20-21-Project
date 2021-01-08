# Client connects to server socket. It runs the main app and gets its data from it, then
# sends it out to server so that all client instances can be updated.
# HOW TO: Run -> Edit configuration -> Allow parallel run -> pokreni vise instanci

import sys
import socket, pickle
import selectors
import types
import time
from multiprocessing import Process
import threading
from GameVariables import *
from PyQt5.QtWidgets import QApplication
from SnakeGame import SnakeGame
import uuid


sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."] #this will be changed with data from the game
eventHappened = False
game = None
client_id = str(uuid.uuid4())

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print("starting connection", connid, "to", server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages),
            recv_total=0,
            messages=list(messages),
            outb=b"",
        )
        sel.register(sock, events, data=data)


def unpickle_data(recieved):
    global got_from_server      #TODO ovo gurni na Board
    got_from_server = pickle.loads(recieved)
    if got_from_server.client_id != client_id:
        game.sboard.updateGameState(got_from_server)

        print("PLAYERS NUM")
        print(got_from_server.numOfPlayers)
        print(got_from_server.snakeTurn)
        print(got_from_server.player1Snakes[0])
        print(got_from_server.player1Snakes[1])
        print(got_from_server.player1Snakes[2][0])
    else:
        print("It was my turn, will not send")


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(10000)  # Should be ready to read
        if recv_data:
            data.recv_total += len(recv_data)
            unpickle_data(recv_data)
    if mask & selectors.EVENT_WRITE:
        if game is not None:
            if game.sboard.eventHappened is True:
                fill_game_variables()
                sent = sock.send(pickle.dumps(game_data))
                print("SENT IN BYTES")
                print(sent)
                game.sboard.eventHappened = False


host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 65432  # Port to listen on (non-privileged ports are > 1023)
num_conns = 1
start_connections(host, int(port), int(num_conns))


def fill_game_variables():
    #game_data = GameVariables()
    game_data.client_id = client_id
    game_data.Grid = game.sboard.Grid
    game_data.playerTurn = game.sboard.turnPlayerIndex
    game_data.snakeTurn = game.sboard.Players[game_data.playerTurn].turnSnakeIndex
    game_data.numOfPlayers = game.sboard.numberOfPlayers
    game_data.foodPositions = []
    for val in game.sboard.Foods:
        game_data.foodPositions.append(val.position)
    game_data.player1Snakes = []
    for val in game.sboard.Players[0].Snakes:
        game_data.player1Snakes.append([val.snakePosition, val.direction])
    game_data.player2Snakes = []
    if (len(game.sboard.Players) == 2):
        for val in game.sboard.Players[1].Snakes:
            game_data.player2Snakes.append([val.snakePosition, val.direction])
    game_data.player3Snakes = []
    if (len(game.sboard.Players) == 3):
        for val in game.sboard.Players[2].Snakes:
            game_data.player3Snakes.append([val.snakePosition, val.direction])
    game_data.player4Snakes = []
    if (len(game.sboard.Players) == 4):
        for val in game.sboard.Players[3].Snakes:
            game_data.player4Snakes.append([val.snakePosition, val.direction])


def start_game():
    app = QApplication([])
    global game
    game = SnakeGame()
    sys.exit(app.exec_())


def connection_loop():
    try:
        while True:
            events = sel.select(timeout=1)
            if events:
                for key, mask in events:
                    service_connection(key, mask)
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sel.close()


if __name__ == '__main__':
    global game_data, game_data_bytes
    game_data = GameVariables()

    p = threading.Thread(target=start_game,)      # p = Process(target=start_game)
    s = threading.Thread(target=connection_loop, )
    p.start()
    s.start()
    p.join()
    s.join()