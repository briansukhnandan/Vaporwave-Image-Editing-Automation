import sys, os
import imageproc
from tkinter import Tk
from tkinter.filedialog import askopenfilename

file_dir = os.path.dirname(__file__)
sys.path.append('src/imageproc.py')

def main():

    Tk().withdraw

    image = askopenfilename()
    print(image)


    image = imageproc.convert_Image(imageproc.open_image(image))
    imageproc.save_image(image, "images/output.png")


if __name__ == "__main__":

    main()