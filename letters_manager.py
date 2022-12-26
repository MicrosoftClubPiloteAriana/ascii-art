import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class LettersManager:
    LETTERS = "ك ل ا ش ئ ة ء".split()

    def __init__(self):
        self.brightnesses = None

        self.compute_brightnesses()

    def compute_brightnesses(self):
        brightnesses = list()

        for letter in LettersManager.LETTERS:
            image = self.generate_image(letter)
            brightness = self.compute_brightness_for_image(image)
            brightnesses.append(brightness)

        brightnesses = np.array(brightnesses)
        brightnesses = brightnesses - np.min(brightnesses)
        brightnesses = brightnesses * 255 / np.max(brightnesses)
        self.brightnesses = brightnesses

    @staticmethod
    def compute_brightness_for_image(image):
        array = np.array(image)
        return np.average(array)

    @staticmethod
    def generate_image(letter):
        image = Image.new(mode="L", size=(50, 50), color="white")
        drawing_tool = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial", size=50)
        drawing_tool.text((0, 0), letter, fill="black", font=font)
        return image

    def get_letter(self, color):
        array = abs(self.brightnesses - color)
        index = array.argmin()
        return LettersManager.LETTERS[index]
