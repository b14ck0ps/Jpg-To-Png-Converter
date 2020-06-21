import sys
import os
from PIL import Image

try:
    # grab the first and secend args
    image_folder = sys.argv[1]
    output_folder = sys.argv[2]
except IndexError:
    image_folder = "./put your jpg here/"
    output_folder = "./converted png/"

# user define folder
choice = input(
    'Press Y if you want to use your own I\O or just press enter to skip: ')
if choice.upper() == 'Y':
    image_folder = input('Ener Full folder name for Input JPG: ')
    image_folder = f'./{image_folder}/'
    output_folder = input('Enter Full folder name To store Converted PNG: ')
    output_folder = f'./{output_folder}/'
else:
    print('\n\t\tDefault Folder I/O Used\n')

# chech if new/ exist . if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def converter():
    # loop through input folder
    print('\nConverting................')
    for filename in os.listdir(image_folder):
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        # conver images to png and save to a new folder
        img.save(f'{output_folder}{clean_name}.png', 'png')
        print(f'{filename} \t--->\t {clean_name}.png\t\tdone')
    if os.path.exists(output_folder):
        print('\nImages Coverted successfully\n')

if os.path.exists(image_folder):
    converter()
else:
    print('Input Folder does not exitst')
# python JpgToPngConverter.py ./put your jpg here/ ./converted png/
