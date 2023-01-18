import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description="""
폴더 내의 이미지 파일들을 찾아 하나의 pdf 파일로 저장하는 파이썬 프로그램입니다.
""")
parser.add_argument('--outfilename', required=False, help="저장되는 pdf파일의 파일명을 지정합니다. 기본값은 out.pdf입니다.", default='out.pdf')
parser.add_argument('--which_folder',required=False, help="이미지 파일을 찾을 폴더를 지정합니다. 기본값은 현재 폴더입니다.",default='./')
args = parser.parse_args()

filelist = os.listdir(args.which_folder)
pdflist = []
for file in filelist:
    if file.endswith((('.png','.jpg'))):
        image_full_directory = os.path.join(args.which_folder, file)
        image_converted = Image.open(image_full_directory).convert('RGB')
        pdflist.append(image_converted)
try:
    pdflist[0].save(args.outfilename, save_all=True, append_images=pdflist[1:])
    print(f'[Success] to generate pdf file: {args.outfilename}')
except:
    print(f'[Failed] to generate pdf file: {args.outfilename}')