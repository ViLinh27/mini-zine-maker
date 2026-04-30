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

#### requirements.txt

- extra installations
- styling

#### Readme.md

- notes
