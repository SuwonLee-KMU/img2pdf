import os
import PIL.Image
from tkinter import *
from tkinter import filedialog
import fitz

global which_folder
which_folder = os.getcwd()

win = Tk()
win.geometry("500x500")
win.title("img2pdf")
win.option_add("*Font","맑은고딕 25")

# 파일 선택 함수
def open():
    global which_folder 

    win.filelist = filedialog.askopenfilenames(initialdir='', title='파일선택', filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
    img2pdflist = []
    pdfmergelist = []
    pdfmergedfile = fitz.open()
    outfilename = win.filelist[0]+'.pdf'
    which_folder = os.path.dirname(outfilename)
    for file in win.filelist:
        print(file)
        if file.endswith((('.png','.jpg','.PNG','.JPG'))):
            image_full_directory = os.path.join(which_folder, file)
            image_converted = PIL.Image.open(image_full_directory).convert('RGB')
            img2pdflist.append(image_converted)
        if file.endswith((('.pdf','.PDF'))):
            pdfmergelist.append(os.path.join(which_folder, file))
    try:
        # image to pdf
        if len(img2pdflist) != 0:
            img2pdflist[0].save(outfilename, save_all=True, append_images=img2pdflist[1:])
            pdfmergelist.append(outfilename)
        # pdfs merge
        for pdf in pdfmergelist:
            with fitz.open(pdf) as mfile:
                pdfmergedfile.insert_pdf(mfile)
        pdfmergedfile.save(outfilename)
        alert_string = f'[Success] to generate pdf file: \n {outfilename}'
    except:
        alert_string = f'[Failed] to generate pdf file: \n {outfilename}'
    Label(win, text=alert_string).pack() # 파일경로 view
 
def open_output_folder():
    global which_folder
    os.startfile(which_folder)

# 버튼 시작
importBtn = Button(win, text="Select images..")
importBtn.config(width=20, height=5)
importBtn.config(command=open)
importBtn.pack()
openBtn = Button(win, text="Open output folder")
openBtn.config(width=20, height=5)
openBtn.config(command=open_output_folder)
openBtn.pack()

# 버튼 종료
win.mainloop()