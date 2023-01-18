import os
import PIL.Image
from tkinter import *
from tkinter import filedialog

win = Tk()
win.geometry("500x250")
win.title("img2pdf")
win.option_add("*Font","맑은고딕 25")

# 파일 선택 함수
def open():
    global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    win.filelist = filedialog.askopenfilenames(initialdir='', title='파일선택', filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
    pdflist = []
    which_folder = os.getcwd()
    outfilename = win.filelist[0]+'.pdf'
    for file in win.filelist:
        print(file)
        if file.endswith((('.png','.jpg','.PNG','.JPG'))):
            image_full_directory = os.path.join(which_folder, file)
            image_converted = PIL.Image.open(image_full_directory).convert('RGB')
            pdflist.append(image_converted)
    try:
        pdflist[0].save(outfilename, save_all=True, append_images=pdflist[1:])
        alert_string = f'[Success] to generate pdf file: \n {outfilename}'
    except:
        alert_string = f'[Failed] to generate pdf file: \n {outfilename}'
    Label(win, text=alert_string).pack() # 파일경로 view
 

# 버튼 시작
importBtn = Button(win, text="Select images..")
importBtn.config(width=20, height=5)
importBtn.config(command=open)
importBtn.pack()

# 버튼 종료
win.mainloop()