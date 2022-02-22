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

def thread_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)
            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

    


while True:
    conn, addr = s.accept() # accepts any incoming connection & store it in conn (conn is an object storing whats connected, address is an ip address)
    print("Connected to:", addr)

    start_new_thread((thread_client, (conn,)))




