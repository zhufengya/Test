from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from config_parser import *
import os
import json
LARGE_FONT = ("Helvetica", 20)
MID_FONT = ("Helvetica", 16)



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #置中
        self.wm_title("Menu")
        x = self.winfo_screenheight()
        y = self.winfo_screenwidth()
        x_ = 500
        yy = 700
        x1 = (y - x_) / 2
        y1 = (x - yy) / 2
        self.geometry("%dx%d+%d+%d" % (x_, yy, x1, y1))  # 设置窗口大小
        container = tk.Frame(self)
        container.pack(padx=25, pady=10)


        self.frames = {}
        # 循环功能界面
        for F in (StartPage, A, Subpage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处

    def show_frame1(self, cont, st):   #st:click the bottom跳转新页面的存储各个选项的文件名
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处


    def read_json(self, file_name):
        try:
            f = open(file_name, 'r')
            module_list = json.loads(f.read())["name"]
            return module_list
        except:
            raise Exception("fail to open file %s" % file_name)

    def read_file(self, file_name):
        try:
            res = []
            with open(file_name, 'r') as f:
                for line in f:
                    res.append(line.strip('\n'))
            return res
        except:
            raise Exception("fail to read file %s" % file_name)

    def submit(self, chosen_list):
        res = []
        for li in chosen_list:
            if li[0].get():
                res.append(li[1])
        print(res)

    def sub_submit(self, lb):
        res = []
        index = lb.curselection()
        for i in index:
            res.append(lb.get(i))
        print(res)


class StartPage(tk.Frame):  #主页面
    def __init__(self, parent, root):
        super().__init__(parent)
        ft2 = tkFont.Font(size=16)

        for ele in MAIN_CHOICE:
            Button(self, text=ele, font=ft2, command=lambda: root.show_frame(A), width=20, height=3, fg="black", bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self, text='EXIT', height=3, font=ft2, width=20, command=root.destroy, fg='black',bg='red',activebackground='black',activeforeground='white').pack()


class A(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        ft2 = tkFont.Font(size=16)

        choice_list = []
        y_value = 150
        for element in CHOICE_LIST:    #, width=20    width=20,
            label_module = Label(self, text=element + ':', justify=tk.RIGHT)
            label_module.place(x=10, y=y_value, height=20)
            choice = IntVar(value=1)
            radioYes = Radiobutton(self, variable=choice, value=1)
            radioYes.place(x=100, y=y_value, height=20)  # width=20,
            radioNo = Radiobutton(self, variable=choice, value=0)
            radioNo.place(x=150, y=y_value, height=20)   # width=20,
            choice_list.append([choice, element])
            bt = Button(self, text="look", height=3, font=ft2, command=lambda: root.show_frame1(Subpage, element), fg = 'black', bg = 'blue')
            bt.place(x=190, y=y_value, height=20, width=50)
            y_value += 30
        Button(self, text="submit", height=3, font=ft2, width=20, command=lambda: root.submit(choice_list), fg='black', bg='gray').pack(side = tk.BOTTOM)
        Button(self, text="back", height=3, font=ft2, width=20, command=lambda: root.show_frame(StartPage), fg='black', bg='red').pack(side = tk.BOTTOM)


class Subpage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        ft2 = tkFont.Font(size=20)
        file_name = "abcdefghi.txt"   #先从文件中读出file_name
        choices = root.read_file(file_name)

        Button(self, text="submit", height=3, font=ft2, width=20, command=lambda: root.sub_submit(listbox), fg='black', bg='gray').pack(side=tk.BOTTOM,anchor='sw')
        Button(self, text="back", height=3, font= ft2, width=20, command=lambda: root.show_frame(A), fg='black', bg='gray').pack(side=tk.BOTTOM,anchor='sw')
        sc = tk.Scrollbar(self)
        sc.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, yscrollcommand=sc.set)
        for ch in choices:
            listbox.insert(tk.END, ch)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=50)  #
        sc.config(command=listbox.yview)





if __name__ == '__main__':


    #test()
    # 实例化Application
    app = Application()
    app.show_frame(StartPage)
    # 主消息循环:
    app.mainloop()
