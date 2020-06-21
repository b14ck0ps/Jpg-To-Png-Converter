import sys
import os
from PIL import Image

#grab the first and secend args
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#chech if new/ exist . if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through poki folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    #conver images to png and save to a new folder
    img.save(f'{output_folder}{clean_name}.png','png')
    print(f'{filename} \t--->\t {clean_name}.png\t\tdone')


#python JpgToPngConverter.py ./'put your jpg here'/ ./'converted png'/
