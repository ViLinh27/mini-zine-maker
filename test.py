# standalone for making the printable sheet with the test images in the folder provided.
import os
from PIL import Image, ImageDraw
from zine_layout import create_zine_sheet, CELL_W, CELL_H
import glob
import numpy as np

def run_test():
    print("Uploading the test images from the folder...")
    path="./test-zine-imgs/*png"
    img_list=[]

    for filename in glob.glob(path):
        img = Image.open(filename)
        img_list.append(np.array(img))
    
    img_arr = np.array(img_list)

    print("creating zine sheet with test images...")
    zine_sheet = create_zine_sheet(img_arr, fit_mode = "contain", draw_guides=True)

    output_path = "test_zine_sheet01.png"
    zine_sheet.save(output_path)
    print(f"Zine sheet saved as {output_path}")
    print(f"dimensions to check: {zine_sheet.size[0]}x{zine_sheet.size[1]} pixels")

if __name__ == "__main__":
    run_test()

