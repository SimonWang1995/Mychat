import tkinter as tk
import argparse
from sql import Mysql
from server import Server
from client import Client
from LoginPage import LoginPage
from MainPage import MainPage

def main():
    mysql = Mysql(params['host'], user='root', database='mychat')
    myclient = Client(params['host'], params['port'])
    root = tk.Tk()
    root.title('Mychat')
    LoginPage(root, myclient, mysql)
    root.mainloop()



def getopt():
    parser = argparse.ArgumentParser()
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument('-s', '--server', action='store_true', help='running server')
    # group.add_argument('-H', '--host', default='localhost', help='server host ip')
    group = parser.add_argument_group('group')
    group.add_argument('-s', '--server', action='store_true', help='run server mode')
    group.add_argument('-n', '--num', default=5, type=int, help='Max listen number')
    # parser.add_argument('-s', '--server', action='store_true', help='run server mode')
    parser.add_argument('-p', '--port',  type=int, default=5555, help='server port(default 5555)')
    parser.add_argument('-H', '--host', default='localhost', help='server host ip(default 127.0.0.1)')
    args = parser.parse_args()
    return args.__dict__


if __name__ == '__main__':
    params = getopt()
    print(params)

    if params['server']:
        Server(params['host'], params['port'], params['num'])
    else:
        main()
