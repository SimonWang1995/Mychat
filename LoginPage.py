import tkinter as tk
from tkinter.messagebox import *
from MainPage import MainPage

class LoginPage(object):
    def __init__(self, master, sock, mysql):
        self.root = master
        self.mysock = sock
        self.mysql = mysql
        self.user = tk.StringVar()
        self.passwd = tk.StringVar()
        self.root.geometry("%dx%d" % (300, 180))
        self.initpage()

    def initpage(self):
        self.page = tk.Frame(self.root)  # 创建Frame
        self.page.pack()
        tk.Label(self.page).grid(row=0, stick=tk.W)
        tk.Label(self.page, text='账户: ').grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.user).grid(row=1, column=1, stick=tk.E)
        tk.Label(self.page, text='密码: ').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.passwd, show='*').grid(row=2, column=1, stick=tk.E)
        tk.Button(self.page, text='登陆', command=self.chklogin).grid(row=3, stick=tk.W, pady=10)
        tk.Button(self.page, text='注册', command=self.apply).grid(row=3, column=1, stick=tk.E)


    def apply(self):
        pass

    def chklogin(self):
        if self.user.get() and self.passwd.get():
            try:
                sql = "select * from userinfo where name='%s'" % self.user.get()
                print(sql)
                self.mysql.runsql(sql)
                res = self.mysql.fechone()
                print("res:",res)
                if res:
                    if res[2] == self.passwd.get():
                        self.page.destroy()
                        MainPage(self.root, self.mysock)
                    else:
                        showinfo(title='错误', message='账号或密码错误！')
                else:
                    showinfo(title='错误', message='账号不存在')
            except:
                print('login fail!!!')



if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()