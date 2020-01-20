import tkinter as Tk
import src.imageproc as imageproc


class MainWindow:

    image = imageproc.open_image("../images/bliss.png")
    currently_editing_file_text = None
    new_img = image

    def __init__(self, master):

        self.master = master
        master.title("Vaporwave Image Editing Automation")

        self.label = Tk.Label(master, textvariable=self.currently_editing_file_text)
        self.label.pack()

        self.greet_button = Tk.Button(master, text="Save Image", command=self.save)
        self.greet_button.pack()

        self.greet_button = Tk.Button(master, text="Convert Image", command=self.convert_image)
        self.greet_button.pack()


    def convert_image(self):
        self.new_img = imageproc.convert_Image(imageproc.open_image(self.image))
        self.updateLabel()

    def save(self):
        print("Saving images to images/output/output.png")
        imageproc.save_image(self.new_img, "../images/output/output.png")

    def updateLabel(self):
        self.currently_editing_file_text = Tk.StringVar()
        self.currently_editing_file_text.set("test")