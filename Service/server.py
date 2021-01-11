#STA SERVER CUVA: pozicije svih zmija, pozicije hrane, koji je igrac na redu, koja je zmija na
#                 redu ...
#1. new game -> sever instance init -> send server how many players
#2. listen for [how many players] connections. for every connection spawn snakes - init player
#3. when all are connected - > start game
#4. with every turn player sends information about his moves to server, server updates other players
#5. ???

import sys
import socket
import selectors
import types
import pickle

sel = selectors.DefaultSelector()
clients = set()


class clientMemo:
    def __init__(self):
        self.clientsToPlayers = []


client_memo = clientMemo()


def accept_wrapper(sock):
    global justSubscribed
    justSubscribed = True
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    clients.add(conn)


def unpickle_data(recieved):
    global game_data, justSubscribed
    game_data = pickle.loads(recieved)
    if game_data.client_id not in client_memo.clientsToPlayers:
        client_memo.clientsToPlayers.append(game_data.client_id)
    print("PLAYERS NUM")
    print(game_data.numOfPlayers)
    print(game_data.snakeTurn)
    print(game_data.player1Snakes[0])

def service_connection(key, mask):
    global justSubscribed
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(20000)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)

    if mask & selectors.EVENT_WRITE:
        if data.outb:  #TODO DA SALJE SVM IGRACIMA UPDATE
            #print("echoing", repr(data.outb), "to", data.addr)
            #sent = sock.send(data.outb)  # Should be ready to write
            unpickle_data(recv_data)
            game_data.clientsToPlayers = client_memo.clientsToPlayers
            print("cliToPl:"+str(len(game_data.clientsToPlayers)))
            pickled_data = pickle.dumps(game_data)
            if justSubscribed == False:
                for c in clients:
                    sent = c.send(pickled_data)  #data.outb
                    data.outb = data.outb[sent:]
            else:
                justSubscribed = False
                data.outb = b''


#
host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 65432  # Port to listen on (non-privileged ports are > 1023)

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("listening on", (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
