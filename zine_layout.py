from PIL import Image, ImageOps,ImageDraw
from natsort import natsorted
#this is how the layout works in landscape:

ZINE_LAYOUT = [
    {"page": 1, "row": 0, "col": 0, "rotate": 180},
    {"page": 8, "row": 0, "col": 1, "rotate": 180},
    {"page": 7, "row": 0, "col": 2, "rotate": 180},
    {"page": 6, "row": 0, "col": 3, "rotate": 180},
    {"page": 2, "row": 1, "col": 0, "rotate": 0},
    {"page": 3, "row": 1, "col": 1, "rotate": 0},
    {"page": 4, "row": 1, "col": 2, "rotate": 0},
    {"page": 5, "row": 1, "col": 3, "rotate": 0},
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
    
    if mode == "cover": # this where image covers entire page cell and may be cropped
        return ImageOps.fit(
            img,
            (cell_w,cell_h),
            method = Image.Resampling.LANCZOS,
            centering=(0.5,0.5),
        )
    
    return img

def create_zine_sheet(page_images,fit_mode="contain", draw_guides = True):#takes pages and arranges them in zine layout
    canvas = Image.new("RGB", (SHEET_W, SHEET_H), "white")
    draw = ImageDraw.Draw(canvas)
    #to make sure we have 8 pages, any missing, will be blank:
    prepped_pages = {}# these pages have been rotated and arranged as needed
    for i in range(1,9):#goes through up to 8 uploaded images, fewer will be left blank hence the else
        if i<=len(page_images):
            #print("page name: "+page_images[i].filename)#debug
            #calls the other func to process each page/img
            prepped_pages[i] = fit_img_to_cell(page_images[i-1], CELL_W, CELL_H, mode=fit_mode)
        else:
            prepped_pages[i] = Image.new("RGB",(CELL_W,CELL_H),"white")

    #prepped_pages = natsorted(prepped_pages.items())#sorts the pages in natural order so they will be arranged correctly in the layout, and not just in order of how they were uploaded
    for item in ZINE_LAYOUT: #helps track what each page is where it goes on sheet
        #each feature of page to track
        page_num = item["page"]
        row = item["row"]
        col = item["col"]
        rotation = item["rotate"]

        #print("page index: "+str(page_num))#debug
        #print("page name: "+str(prepped_pages[page_num]))#debug
        page = prepped_pages[page_num]#the processed pages will use page number as the key to track where it will go in layout
        if rotation:
            page = page.rotate(rotation, expand=False)

        x = col * CELL_W
        y = row * CELL_H
        canvas.paste(page,(x,y))

    if draw_guides:#in case i want to add guides for folding/cutting on the printable final layout
        draw.rectangle(
            [x,y,x+ CELL_W, y+ CELL_H],
            outline = "lightgray",
            width = 3,
        )

    return canvas