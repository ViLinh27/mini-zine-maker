from PIL import Image, ImageOps

#this is how the layout works in landscape:
ZINE_LAYOUT=[
    {"page":1,"row":0,"col":0,"rotate":180},
    {"page":8,"row":0,"col":1,"rotate":180},
    {"page":7,"row":0,"col":2,"rotate":180},
    {"page":6,"row":0,"col":3,"rotate":180},
    {"page":2,"row":1,"col":0,"rotate":0},
    {"page":3,"row":1,"col":1,"rotate":0},
    {"page":4,"row":1,"col":2,"rotate":0},
    {"page":5,"row":1,"col":3,"rotate":0},
]
#These are dimensions in landscape:
DPI = 300
SHEET_W = int(11*DPI)
SHEET_H = int(8.5*DPI)
#floor division will give us whole integers:
CELL_W = int(SHEET_W//4)
CELL_H = int(SHEET_H//2)

#helps prep each image for zine layout:
def fit_img_to_cell(img, cell_w, cell_h, mode="contain"):
    img = ImageOps.exif_transpose(img).convert("RGB")# automatically rotates/flips image to correct orientation based on its exif orientatition tag
    if mode == "contain":
        img.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)# resize image to fit cell width/height with original aspect ratio, and downscales if needed
        page = Image.new("RGB", (cell_w,cell_h), "white")
        x = (cell_w - img.width) // 2
        y = (cell_h - img.height) // 2
        page.paste(img, (x,y))# paste the resized image onto a white background
        return page
    
    if mode == "cover":
        return ImageOps.fit(
            img,
            (cell_w,cell_h),
            method = Image.Resampling.LANCZOS,
            centering=(0.5,0.5),
        )
    
def create_zine_sheet(page_images,fit_mode="contain", draw_guides = True):
    canvas = Image.new("RGB", (SHEET_W, SHEET_H), "white")
    draw = ImageDraw.Draw(canvas)
    #to make sure we have 8 pages, any missing, will be blank:
    prepped_pages = {}
    for i in range(1,9):
        if i<=len(page_images):
            prepped_pages[i] = fit_img_to_cell(page_images[i-1], CELL_W, CELL_H, mode=fit_mode)
        else:
            prepped_pages[i] = Image.new("RGB",(CELL_W,CELL_H),"white")