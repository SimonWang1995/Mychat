import tkinter as tk
from threading import Thread


class MainPage(object):
    def __init__(self, master, mysock):
        self.root = master
        self.root.geometry("%dx%d+800+100" % (250, 120))
        self.root.resizable(0, 0)
        self.mysock = mysock
        self.nick = tk.StringVar()
        welcome = self.mysock.get_msg()
        print(welcome)
        tk.Label(self.root, text='Welcome to server', font=('楷体', 12)).place(relx=0.2, rely=0.1)
        tk.Label(self.root, text="NickName:", font=('楷体', 12)).place(relx=0.05, rely=0.4)
        tk.Entry(self.root, textvariable=self.nick).place(relx=0.4, rely=0.4, relwidth=0.5)
        tk.Button(self.root, text='退出', command=self.root.quit).place(relx=0.05, rely=0.7, relwidth=0.2)
        tk.Button(self.root, text='确认', command=self.check_nick).place(relx=0.75, rely=0.7, relwidth=0.2)

    def check_nick(self):
        nickname = self.nick.get()
        if nickname:
            self.mysock.send_msg(self.nick.get())
            self.initpage()

    def initpage(self):
        self.root.geometry("%dx%d" % (500, 600))
        self.measge_text = tk.Text(self.root)
        self.measge_text.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.6)
        thread = Thread(target=self.get_msg)
        thread.setDaemon(True)
        thread.start()
        self.input_text = tk.Text(self.root)
        self.input_text.place(relx=0.05, rely=0.63, relwidth=0.9, relheight=0.3)
        button = tk.Button(self.root, text="发送", command=self.send_msg)
        button.place(relx=0.85, rely=0.94, relwidth=0.08, relheight=0.05)

    def send_msg(self):
        msg = self.input_text.get('0.0', 'end')
        msglist = msg.split('\n')
        print(msglist)
        for msg in msglist:
        # if msg != '\n':
            try:
                print(msg)
                self.mysock.send_msg(msg)
                self.measge_text.insert('end', ' '*(63-len(msg))+msg+'\n')
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')
            self.input_text.delete('0.0', 'end')

    def get_msg(self):
        while True:
            msg = self.mysock.get_msg()
            self.measge_text.insert('end', msg+'\n')

if __name__ == '__main__':
    import socket
    from client import Client
    mysock = Client(host='127.0.0.1', port=5555)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    root = tk.Tk()
    MainPage(root, mysock)
    root.mainloop()