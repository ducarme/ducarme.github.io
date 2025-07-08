# adapted from Aengus Patterson, July 2023
#c onverts from heic (or any other format) to webp.

import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ExifTags, ImageOps
from pillow_heif import register_heif_opener


pic_quality: int = 80
pic_maxsize: int = 800
large_pic_maxsize: int = 1000
initial_input_dir = 'images'
initial_output_dir = 'images/thumbnails'


register_heif_opener()
print("Select input files in dialog window...")
input_paths = filedialog.askopenfilenames(initialdir=initial_input_dir)


loss_less = False
if pic_quality == 100:
    loss_less = True
print("Select output directory in dialog window...")
output_dir = filedialog.askdirectory(initialdir=initial_output_dir)

print(f'Conversion in progress... ({len(input_paths)} files to process)')
nb_converted_images = 0
for input_path in input_paths:
    try:
        # Open the image using Pillow
        img = Image.open(input_path)
        img_large = Image.open(input_path)
        
        img = ImageOps.exif_transpose(img)
        img_large = ImageOps.exif_transpose(img_large)

        img_large.thumbnail((large_pic_maxsize, large_pic_maxsize))
        img_large.save(os.path.join(output_dir, 'large', os.path.basename(input_path)))

        img.thumbnail((pic_maxsize, pic_maxsize))
        img.save(os.path.join(output_dir, os.path.basename(input_path)))

        if img.mode != 'RGB':
            img = img.convert('RGB')

        filename = os.path.basename(input_path).split(".")[0]
        # output_filepath = os.path.join(output_dir, filename + '_' + str(pic_quality).zfill(3) + '.webp')
        output_filepath = os.path.join(output_dir, filename + '.webp')
        
        img.save(output_filepath, format='webp', method=6, lossless=loss_less, quality=pic_quality)
        nb_converted_images += 1
        print(f"\tprogress: {nb_converted_images}/{len(input_paths)} successfully converted...")
    except FileNotFoundError:
        print(f"Error: input file not found at '{input_path}'")
        continue
    except Exception as e:
        print(f"Error converting '{input_path}': {e}")
        continue

if len(input_paths) - nb_converted_images != 0:
    print (f"Finished! {len(input_paths) - nb_converted_images} files could not be converted.")
else:
    print (f"Finished! All selected images have been converted.")
