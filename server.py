import socket
import argparse
from threading import Thread

class Server(object):
    mydict = dict()
    mylist = list()
    def __init__(self, host, port, num):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(num)
        print("Server已经开启，等待客户端连接")
        while True:
            conn, addr = s.accept()
            print("Accept a new connection", conn.getsockname(), conn.fileno())
            try:
                conn.send("Please Enter a Nickname:".encode())
                thread = Thread(target=self.handle_client_in, args=(conn, conn.fileno()))
                thread.setDaemon(True)
                thread.start()
            except Exception as e:
                pass


    def tellOthers(self, connNum, msg):
        for conn in self.mylist:
            if conn.fileno() != connNum:
                try:
                    conn.send(msg.encode())
                except:
                    pass

    def handle_client_in(self, myconn, connNum):
        nickname = myconn.recv(1024).decode()
        self.mydict[connNum] = nickname
        self.mylist.append(myconn)
        print('connection '+str(connNum)+' has nickname '+nickname)
        self.tellOthers(connNum, "【系统提示：" + nickname + "加入聊天室】\n")
        while True:
            try:
                getmsg = myconn.recv(1024).decode()
                if getmsg:
                    print(self.mydict[connNum] + ":" + getmsg)
                    self.tellOthers(connNum, self.mydict[connNum] + ':\n' + getmsg)
            except (OSError, ConnectionResetError):
                self.mylist.remove(myconn)
                print(self.mydict[connNum], 'exit,', len(self.mylist), 'prosen left')
                self.tellOthers(connNum, "【系统提示:"+self.mydict[connNum]+"离开了聊天室】")
                myconn.close()
                return

def getopts():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port',  type=int, default=5555, help='server port(default 5555)')
    parser.add_argument('-H', '--host', default='localhost', help='server host ip(default 127.0.0.1)')
    parser.add_argument('-n', '--number', type=int, default=5, help='Max listen number')
    args = parser.parse_args()
    return args.__dict__

if __name__ == '__main__':

    params = getopts()
    Server(params['host'], params['port'], params['number'])