from letters_manager import LettersManager
from PIL import Image, ImageDraw, ImageFont
from util import change_contrast
import numpy as np

# LettersManager will be used to determine which
# letter to use for each pixel color
manager = LettersManager()

with Image.open("input.jpg") as image:
    width, height = image.size
    draw = ImageDraw.Draw(image)
    image = image.convert("L")
    image = change_contrast(image, 75)

font = ImageFont.truetype("arial")
support = Image.new("RGB", (width*10,height*10), "white")
pixels = np.array(image)
d = ImageDraw.Draw(support)

for i in range(height):
    for j in range(width):
        avg = pixels[i][j]
        char = manager.get_letter(avg)

        coords = [(j*10,i*10),((j+1)*10,(i+1)*10)]
        d.text((j*10+5,i*10+5), char, fill=(0,0,0),font=font, anchor="mm")

support.show()
