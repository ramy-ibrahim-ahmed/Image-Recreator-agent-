from PIL import Image
import re
import glob

frames = []
imgs = sorted(glob.glob("gif/*.png"))

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

imgs.sort(key=extract_number)

width = 880
height = 1018

for i in imgs:
    img = Image.open(i)
    resized_img = img.resize((width, height))
    frames.append(resized_img)


frames[0].save(
    "mona_lisa_.gif",
    format="GIF",
    append_images=frames[1:],
    save_all=True,
    duration=200,
    loop=0,
)