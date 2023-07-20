from tkinter import *
import tkinter as tk
from tkinter import Canvas, Label, Listbox, Scrollbar, ttk, font
from PIL import ImageTk,Image
# from typing import Text

from scipy.ndimage.measurements import label

from GUI import men_window

def Home(notebook):
    mainFrame=Frame(notebook,bg='black')
    notebook.add(mainFrame,text='Home')

    title_label = tk.Label(mainFrame, text="Amazon Product Analysis", font=("Courier", 44, "bold"), fg="gold", bg="black")
    title_label.pack(pady=20)

    image_original=Image.open('./images/amazon_img.jpeg')
    image_tk=ImageTk.PhotoImage(image_original)
    image_label = tk.Label(mainFrame, image=image_tk,bg="black")
    label.image=image_tk
    image_label.pack(padx=0,pady=0)

def Men(notebook):
    menFrame=Frame(notebook,bg="black")
    notebook.add(menFrame,text='Men')
    men=ttk.Notebook(menFrame)
    men_window.MenNotebook(men)

def Women(notebook):
    womenFrame=Frame(notebook)
    notebook.add(womenFrame,text='Women')
    women=ttk.Notebook(womenFrame)
    # women_shirts.MenNotebook(women)

def Kid(notebook):
    kidFrame=Frame(notebook)
    notebook.add(kidFrame,text='Kids')
    kid=ttk.Notebook(kidFrame)
    # kid_shirts.MenNotebook(kid)


def main():
    win=tk.Tk()
    win.title("Amazon Product Analysis")
    win.state("zoomed")
    # win.configure(bg="black")

    style = ttk.Style()
    style.theme_settings
    ("default",
     {"TNotebook.Tab": {"configure": {"padding": [0, 0]},
                        "map": {"background": [("active", "green"),
                                               ("!disabled", "orange")],
                                "fieldbackground": [("!disabled", "blue")],
                                "foreground": [("focus", "blue"),
                                               ("!disabled", "black"),
                                               ("active", 'red')],font:[("15")]}}})

    # Create a container frame to hold the notebook and scrollbar
    container = tk.Frame(win)
    container.pack(fill=tk.BOTH, expand=True)

    # Create a canvas to hold the notebook and provide scrolling
    canvas = tk.Canvas(container)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create the vertical scrollbar and attach it to the canvas
    vscrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)
    vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=vscrollbar.set)

    # Create the notebook and place it inside the canvas
    notebook = ttk.Notebook(canvas)
    canvas.create_window((0, 0), window=notebook, anchor=tk.NW)

    # Function to update the canvas scrolling region
    def update_canvas_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", update_canvas_scrollregion)
    notebook.bind("<Configure>", update_canvas_scrollregion)

    win.iconbitmap("./images/amazon_7228.ico")


    Home(notebook)
    Men(notebook)
    Women(notebook)
    Kid(notebook)

    win.mainloop()

if __name__== "__main__":
    main()