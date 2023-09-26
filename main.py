from tkinter import Tk,font
from tkinter import StringVar, Entry, Button
from tkinter.ttk import Style
import math

class calculator:
    def __init__(self):
        window = Tk()
        window.title('您的科学计算器')
        window.configure(background="white")
        self.string = StringVar()
        self.value = 0

        font_size = 16
        font_weight = "bold"
        custom_font  = font.Font(size = font_size,weight = font_weight)

        entry = Entry(window, textvariable=self.string,width = 30,font = custom_font)
        entry.grid(row=0, column=0,columnspan = 6,sticky = "NSEW")
        entry.configure(background="white")
        entry.focus()

        window.grid_rowconfigure(0,weight = 1)
        window.grid_columnconfigure(0,weight =1)

        values = ["(", ")", "%","C", "DEL",
                  "sqrt",  "pow","e","pi", "/",
                  "cos", "7", "8", "9", "*",
                  "tan", "4", "5", "6", "-",
                   "sin","1", "2", "3", "+",
                  "log",  "0", ".", "="]

        text = 1
        i = 0
        row = 1
        col = 0

        for txt in values:
            padx = 15
            pady = 15
            if (i == 5):
                row = 2
                col = 0
            if (i == 10):
                row = 3
                col = 0
            if (i == 15):
                row = 4
                col = 0
            if (i == 20):
                row = 5
                col = 0
            if (i == 25):
                row = 6
                col = 0
            if (txt == '='):
                style = Style()
                style.configure('Tbutton',borderwidth = 0,bodercolor = "Orange",relief = 'flat',borderradius = 100)
                btn = Button(window, height=2, width=4, padx=48, pady=5, text=txt,
                             command=lambda txt=txt: self.equals(),font = ("Arial",16),bd =2,highlightthickness = 2)
                btn.config(highlightcolor = "grey")
                btn.grid(row=row, column=col, columnspan=3, padx=0, pady=0)
                btn.configure(background="Orange")

            elif (txt == 'DEL'):
                btn = Button(window, height=2, width=4, padx=10, pady=5, text=txt,
                             command=lambda txt=txt: self.delete(),font = ("Arial",16),bd = 2,highlightthickness = 2)
                btn.config(highlightcolor="grey")
                btn.grid(row=row, column=col, padx=0, pady=0)
                btn.configure(background="grey")

            elif (txt == 'C'):
                btn = Button(window, height=2, width=4, padx=10, pady=5, text=txt,
                             command=lambda txt=txt: self.clearall(),font = ("Arial",16),bd = 2,highlightthickness = 2)
                btn.config(highlightcolor="grey")
                btn.grid(row=row, column=col, padx=0, pady=0)
                btn.configure(background="grey")

            elif(txt == '7' or txt =='8' or txt == '9' or txt == '4' or txt == '5' or txt == '6'or txt == '1' or txt == '2' or txt == '3' or txt == 'abs' or txt == '0' or txt == '.'):
                btn = Button(window, height=2, width=4, padx=10, pady=5, text=txt,
                             command=lambda txt=txt: self.addChar(txt),font = ("Arial",16),bd = 2,highlightthickness = 2)
                btn.config(highlightcolor = "grey")
                btn.grid(row=row, column=col, padx=0, pady=0)
                btn.configure(background="Snow")

            #加减乘除已经OK了
            elif( txt == '+' or txt == '-' or txt == '*' or txt =='/'):
                style = Style()
                style.configure('Tbutton', borderwidth=0, bodercolor="Orange", relief='flat', borderradius=100)
                btn = Button(window, height=2, width=4, padx=10, pady=5, text=txt,
                             command=lambda txt=txt: self.addChar(txt), font=("Arial", 16), bd=2, highlightthickness=2)
                btn.config(highlightcolor="grey")
                btn.grid(row=row, column=col, columnspan=3, padx=0, pady=0)
                btn.configure(background="Orange")

            else:
                btn = Button(window, height=2, width=4, padx=10, pady=5, text=txt,
                             command=lambda txt=txt: self.addChar(txt),font = ("Arial",16),bd = 2,highlightthickness = 2)
                btn.config(highlightcolor = "grey")
                btn.grid(row=row, column=col, padx=0, pady=0)
                btn.configure(background="LightGrey")

            col = col + 1
            i = i + 1
        window.mainloop()

    def clearall(self):
        self.string.set("")


    def equals(self):
        result = ""
        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "无效输入"
        self.string.set(result)
        self.value = 0


    def addChar(self, char):

        if char == "sin":
            try:
                angle = float(self.string.get())
                self.value = math.sin(math.radians(angle))
                self.string.set(self.value)
            except ValueError:
                self.string.set("无效输入")
        elif char == "cos":
            try:
                angle = float(self.string.get())
                self.value = math.cos(math.radians(angle))
                self.string.set(self.value)
            except ValueError:
                self.string.set("无效输入")
        elif char == "tan":
            try:#这里可能存在精度问题
                angle = float(self.string.get())
                self.value = math.tan(math.radians(angle))
                self.string.set(self.value)
            except ValueError:
                self.string.set("无效输入")
        elif char == "log":
            try:
                angle = float(self.string.get())
                self.value = math.log(angle,10)
                self.string.set(self.value)
            except ValueError:
                self.string.set("无效输入")
        elif char == "e":
            try:
                self.string.set(2.7182818284590)
            except ValueError:
                self.string.set("无效输入")
        elif char == "pi":
            try:
                self.string.set(3.1415926535)
            except ValueError:
                self.string.set("无效输入")
        elif char == "sqrt":
            try:
                angle = float(self.string.get())
                self.value = math.sqrt(angle)
                self.string.set(self.value)
            except ValueError:
                self.string.set("无效输入")

        elif char == "pow":
            try:
                angle = float(self.string.get())
                self.value = math.pow(angle,2)
                self.string.set(self.value)
            except ValueError:
                self.string.set("无效输入")
        else:
            self.string.set(self.string.get() + str(char))


    def delete(self):
        self.string.set(self.string.get()[0:-1])

def main():
    P = calculator()
    P()

main()
