# standalone for making the printable sheet with the test images in the folder provided.
import os
from PIL import Image, ImageDraw
from zine_layout import create_zine_sheet, CELL_W, CELL_H
import glob
import numpy as np

def run_test():
    print("Uploading the test images from the folder...")
    path="./test-zine-imgs/*.png"
    img_list=[]

    for filename in glob.glob(path):
        img = Image.open(filename)
        img_list.append(img)
    
   #img_arr = np.array(img_list)
    img_arr = img_list

    print(f"number of images uploaded: {len(img_arr)}")#debug
    print(f"image name: {img_arr[0].filename}")#debug
    print(f"image name: {img_arr[1].filename}")#debug
    print(f"image name: {img_arr[2].filename}")#debug
    print(f"image name: {img_arr[3].filename}")#debug
    print(f"image name: {img_arr[4].filename}")#debug
    print(f"image name: {img_arr[5].filename}")#debug
    print(f"image name: {img_arr[6].filename}")#debug
    print(f"image name: {img_arr[7].filename}")#debug
    print("creating zine sheet with test images...")
    zine_sheet = create_zine_sheet(img_arr, fit_mode = "contain", draw_guides=True)

    output_path = "test_zine_sheet09.png"
    zine_sheet.save(output_path)
    print(f"Zine sheet saved as {output_path}")
    print(f"dimensions to check: {zine_sheet.size[0]}x{zine_sheet.size[1]} pixels")

if __name__ == "__main__":
    run_test()

