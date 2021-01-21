# Client connects to server socket. It runs the main app and gets its data from it, then
# sends it out to server so that all client instances can be updated.
# HOW TO: Run -> Edit configuration -> Allow parallel run -> pokreni vise instanci

import sys
import socket, pickle
import selectors
import types
import threading
import uuid
import time
from GameVariables import *
from PyQt5.QtWidgets import QApplication
from Game.SnakeGame import SnakeGame
from main import MainWindow


sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."] #this will be changed with data from the game
eventHappened = False
game = None
mw = None
client_id = str(uuid.uuid4())
skip_event = False
#global subscribed  #prvi put mora da se prijavi kod servera kao klijent
#subscribed = None

def start_connections(host, port, num_conns):
    global subscribed, turnOrder
    subscribed = False
    turnOrder = False
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


def unpickle_data(recieved,game):
    global got_from_server, turnOrder, game_data     #TODO ovo gurni na Board
    got_from_server = pickle.loads(recieved)
    game.sboard.clientsToPlayers = got_from_server.clientsToPlayers
    if turnOrder == False:
        if len(game.sboard.clientsToPlayers) >= 1:
            game.sboard.clientTurn = game.sboard.clientsToPlayers[0]
        turnOrder = True
    if got_from_server.turnItVar == True and game.sboard.clientTurn == client_id:
        game.sboard.nextPlayerTurn()
        game.sboard.turnIt = False
        got_from_server.turnItVar = False
        print("trenutno igra: sa zmijom:")
        print("clientTurn:"+game.sboard.clientTurn)
        print("ja:" + client_id)
        print(game.sboard.turnPlayerIndex)
        print(game.sboard.turnPlayer.turnSnakeIndex)
    if got_from_server != game_data:
        if got_from_server.client_id != client_id:
            game.sboard.updateGameState(got_from_server)
            print("PLAYERS NUM")
            print(got_from_server.numOfPlayers)
            print(got_from_server.snakeTurn)
            print(got_from_server.player1Snakes[0])
        else:
            print("will not send to myself")
    else:
        print("Irrelevant event, will not update")


def service_connection(key, mask):
    global subscribed, got_from_server, sock, mw
    sock = key.fileobj
    data = key.data
    if mw is not None:
        if mw.game is not None:
            game = mw.game
            if game.sboard.turnIt == True:
                change_turn(game)

            if mask & selectors.EVENT_READ:
                recv_data = sock.recv(20000)  # Should be ready to read
                if recv_data:
                    data.recv_total += len(recv_data)
                    unpickle_data(recv_data,game)
            if mask & selectors.EVENT_WRITE:
                if game is not None:
                    if subscribed == False:
                        set_game_init(game,mw)
                        if len(game.sboard.clientsToPlayers) >= 1:
                            game.sboard.clientTurn = game.sboard.clientsToPlayers[0] #podesi updejtovanu lisu klijenata da bude turn prvog igraca
                    if game.sboard.eventHappened is True or subscribed == False:
                        if game.sboard.clientTurn == client_id or subscribed == False:
                                fill_game_variables(game)
                                sent = sock.send(pickle.dumps(game_data))
                                print("SENT IN BYTES")
                                print(sent)
                                game.sboard.eventHappened = False
                                subscribed = True
                        else:
                            print("Its not my turn, shall not send")


def change_turn(game):
    fill_game_variables(game)
    sent = sock.send(pickle.dumps(game_data))
    game.sboard.turnIt = False


host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 65432  # Port to listen on (non-privileged ports are > 1023)
num_conns = 1
start_connections(host, int(port), int(num_conns))


def fill_game_variables(game):
    game_data.client_id = client_id
    game_data.Grid = game.sboard.Grid
    game_data.playerTurn = game.sboard.turnPlayerIndex
    game_data.snakeTurn = game.sboard.Players[game_data.playerTurn].turnSnakeIndex
    game_data.numOfPlayers = game.sboard.numberOfPlayers1
    game_data.foodPositions = []
    for val in game.sboard.Foods:
        game_data.foodPositions.append(val.position)
    game_data.player1Snakes = []
    for val in game.sboard.Players[0].Snakes:
        game_data.player1Snakes.append([val.snakePosition,val.direction])
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
    if game.sboard.turnIt == True:
        #game_data.nextClientTurn = game.sboard.clientsToPlayers[game.sboard.turnPlayerIndex]
        game.sboard.turnIt = False
        game_data.turnItVar = True


def start_game():
    app = QApplication([])
    global game, mw
    game = None
    mw = MainWindow()
    game = mw.game
    #game.sboard.clientsToPlayers.append(client_id) #ovo treba npr u server da se cuva
    #if len(game.sboard.clientsToPlayers) >= 1:
    #    game.sboard.clientTurn = game.sboard.clientsToPlayers[0]
    #elif (game.sboard.clientTurn == ''):
    #    game.sboard.clientTurn = client_id
    sys.exit(app.exec_())


def set_game_init(game,mw):
    if (mw.game_started == True):
        game.sboard.clientsToPlayers.append(client_id)  # ovo treba npr u server da se cuva
        if len(game.sboard.clientsToPlayers) >= 1:
            game.sboard.clientTurn = game.sboard.clientsToPlayers[0]
        elif (game.sboard.clientTurn == ''):
            game.sboard.clientTurn = client_id


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
    global game_data, game_data_bytes, subscribed
    game_data = GameVariables()

    p = threading.Thread(target=start_game,)      # p = Process(target=start_game)
    s = threading.Thread(target=connection_loop, )
    p.start()
    s.start()
    p.join()
    s.join()