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


sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."] #this will be changed with data from the game
eventHappened = False
game = None

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


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print("received", repr(recv_data), "from connection", data.connid)
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print("closing connection", data.connid)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if game is not None:
            if game.sboard.eventHappened is True:
                sent = sock.send(bytes(pickle.dumps(game_data)))


# call the main app here

host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 65432  # Port to listen on (non-privileged ports are > 1023)
num_conns = 2  # This is supposed to be equal to number of players !!!!!!!!!!!!!!!!!!!!!!
start_connections(host, int(port), int(num_conns))


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