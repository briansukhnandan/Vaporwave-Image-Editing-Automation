import sys, os
import src.imageproc as imageproc
import src.window_init as win_init
import tkinter as Tk

from tkinter.filedialog import askopenfile

file_dir = os.path.dirname(__file__)
sys.path.append('src/imageproc.py')
sys.path.append('src/window_init.py')

def main():

    root_window = Tk.Tk()

    root_window.geometry("800x600")

    gui_interface = win_init.MainWindow(root_window)


    root_window.filename = Tk.filedialog.askopenfilename()

    print(root_window.filename)
    gui_interface.currently_editing_file_text.set(root_window.filename)

    gui_interface.image = root_window.filename

    root_window.update()

    root_window.mainloop()


if __name__ == "__main__":

    main()