from tkinter import *

win = Tk()
win.geometry("600x600")
win.title("Chobo_coding")
win.option_add("*Font","맑은고딕 25")
# 라벨 시작
lab = Label(win)
lab.config(text="레이블")
lab.pack()

# 입력창 시작
ent = Entry(win)
ent.pack()

# 함수
def alert():
    print('버튼이 눌림')

# 버튼 시작
btn = Button(win, text="버튼")
btn.config(width=10, height=5)
btn.config(command=alert)
btn.pack()
# 버튼 종료
win.mainloop()
