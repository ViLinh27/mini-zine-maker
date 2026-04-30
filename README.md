# mini-zine-maker

This is a python project that will use streamlit as a frontend. I want to use this project to help learn the streamlit library and its application with the python language.

The goal is to allow users to upload images to turn into a one paper mini zine that they can print, fold, cut into a mini zine they can print out on one piece of paper. I thought it'd be a fun way to learn streamlit.

## The 4 layers of this app

### Uploading

- Let Users upload 1-8 images with optional reordering
- uses streamlit here

### Page prepping

- Reszie, crop, pad, rotate and normalize images (as needed)
- uses Pillow (for image manipulation)

### Zine Layout

- Places 8 pages into correct printable positions
- Uses Pillow
- Have the Option of using reportlab

### Exporting

- generate downloadable printable
- uses pdf via reportlab/ png via pillow
  - probablly gonna start with png first and see if pdf is doable later

## Stack Basics and why

### Streamlit

- has widgets users can interact with

### Pillow

- handles actual canvas drawing/ image manipulation

### Reportlab

- can convert final layout into proper pdf (optional)

## About the Image Fitting logic

Users are gonna upload images with different aspect ratios that may not always fit the aspect ratio of the mini zine page cell, so i have to consider how to handle that possibility. These are my potential options:

| Mode        | Behaviour                                       | Best for            |
| ----------- | ----------------------------------------------- | ------------------- |
| Fit/Contain | Entire img visible with white margins if needed | preserving art work |
| Fill/Crop.  | img fits in page cell, edges may be cropped.    | full bleed zines.   |
| Stretch.    | img distorted to fit cell exactly.              | not recommended.    |

### Recommended way to go:

- start with contain behaviour
- add fill/crop behaviour after everything works

## Project Structure

- Keep streamlit interface separate from layout logic to make sure nothing is brittle.
- Every file will have its own responsiblity basically.

### The files and what each do

#### app.py

- handles UI

#### zine_layout.py

- handles layout functions like fit_img_to_cell() or create_zine_sheet()
- arranges 8 pages and makes sure the placement and rotation is correct for printable

#### requirements.txt

- extra installations
- styling

#### Readme.md

- notes

## Testing

How to test the python before implementing streamlit with some test images

Start with the zine_latyout.py, since this is in charge of arranging images to make sure the layout is correct on the printable.

Make a test script to go along side the test images and make sure the scripts in the zine_layout.py works well.

If that works fine then I can move on to adding the streamlit part for user interactivity.

## Issues I've encountered.

I wasn't sure how to test the python (no streamlit yet) yet so had to look up some stuff to realize that I would need a standalone test script and some dummy images to make sure the zine_layout.py worked by itself. After getting the images to finally work the main issue I have so far is a Traceback (at least the images load fine).

```
Uploading the test images from the folder...
creating zine sheet with test images...
Traceback (most recent call last):
  File "/Users/vi-linhnguyen/python_miniprojects/mini-zine-maker/test.py", line 28, in <module>
    run_test()
  File "/Users/vi-linhnguyen/python_miniprojects/mini-zine-maker/test.py", line 20, in run_test
    zine_sheet = create_zine_sheet(img_arr, fit_mode = "contain", draw_guides=True)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/vi-linhnguyen/python_miniprojects/mini-zine-maker/zine_layout.py", line 49, in create_zine_sheet
    prepped_pages[i] = fit_img_to_cell(page_images[i-1], CELL_W, CELL_H, mode=fit_mode)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/vi-linhnguyen/python_miniprojects/mini-zine-maker/zine_layout.py", line 24, in fit_img_to_cell
    img = ImageOps.exif_transpose(img).convert("RGB")# automatically rotates/flips image to correct orientation based on its exif orientatition tag
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/PIL/ImageOps.py", line 699, in exif_transpose
    image.load()
    ^^^^^^^^^^
AttributeError: 'numpy.ndarray' object has no attribute 'load'
```
