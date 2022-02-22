import socket
from _thread import *
import sys

server = "10.0.0.18"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # types of connections - iPV4 address


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4) # opens up the port - allows connections for a certain amount
print("waiting for a connection, Server started")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

# starting positions for our players
pos = [(0,0), (100, 100)]

def thread_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data


            #reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                # if were player1, send player 0's pos, if player 0, send player 1's position
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

    

currentPlayer = 0
while True:
    conn, addr = s.accept() # accepts any incoming connection & store it in conn (conn is an object storing whats connected, address is an ip address)
    print("Connected to:", addr)

    start_new_thread(thread_client, (conn, currentPlayer))
    currentPlayer += 1



