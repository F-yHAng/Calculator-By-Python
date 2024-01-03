# 从 Tkinter 导入所有内容
from tkinter import *
# 创建一个基本窗口
root = Tk()
# 定义窗口大小
root.geometry("500x500")
# 防止窗口调整大小
root.resizable(0, 0)
# 创建标题
root.title('Python Calculator')
# 创建页脚
Label(root,text = 'Hello World', font = 'arial 20 bold').pack(side=BOTTOM)


expression=""
# StringVar() 用于获取输入字段的实例
input_text = StringVar()

# Clear: 按键清除功能，该功能用于清楚输入栏
def btn_clear():
    global expression
    expression=""
    input_text.set("")

# Click: 按键单击功能，此功能会在您输入数字时不断更新输入字段
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Equal: 按键相等函数，该函数用于计算输入字段中存在的表达式
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=""


# 创建一个框架，用于容纳输入字段
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
# 将框架放置在顶部
input_frame.pack(side=TOP)
# 创建一个文本输入框，用于用户输入文本
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#000", bd=0, justify=RIGHT)
# 将输入字段放置在框架的第0行 第0列的位置
input_field.grid(row=0, column=0)
# 调整输入字段的高度，以增加输入框的高度
input_field.pack(ipady=10)


# 创建一个框架，用于容纳按钮
btns_frame = Frame(root, width=312, height=272.5, bg="grey")
# 将框架放置在窗口中，默认会根据需要自动调整
btns_frame.pack()

# first row
clear = Button(btns_frame, text = "CLEAR", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear())
clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1)

# second row
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# third row
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# fifth row
zero = Button(btns_frame, text = "0", fg = "black", width = 23, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()
