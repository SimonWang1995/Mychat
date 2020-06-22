import tkinter as tk
from tkinter.messagebox import *
import socket
from threading import Thread



class Client(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((host, port))
        except ConnectionRefusedError:
            print("Server is closed!")

    def get_msg(self):
        try:
            msg = self.sock.recv(1024).decode()
            if msg:
                return msg
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')

    def send_msg(self, msg):
        if msg:
            try:
                self.sock.send(msg.encode())
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')












