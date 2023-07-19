from tkinter import *
import tkinter as tk
from tkinter import Canvas, Label, Listbox, Scrollbar, ttk, font
from PIL import ImageTk,Image
from typing import Text

from scipy.ndimage.measurements import label
from Graph import men_pd

def button_clicked(index,men):
    if(index==0):
        return men_pd.show_graph(men)
    elif(index==1):
        return 1
    elif(index==2):
        return 1

def MenNotebook(men):
    men.pack(expand=True)

    labels = []
    buttons = []
    list=["Shirts","T-Shirts","Jeans"]

    # Load images
    image_paths = ["./images/men_shirt.webp", "./images/men_tshirt.webp", "./images/men_jeans.webp"]
    images = [Image.open(path).resize((400,400)) for path in image_paths]
    photo_images = [ImageTk.PhotoImage(image) for image in images]

    for i in range(3):
        label = tk.Label(men, image=photo_images[i],bd=5,relief=SUNKEN)
        label.image=photo_images[i]
        labels.append(label)
        label.grid(row=0, column=i,padx=50,pady=20)

        button = tk.Button(men,font=("Courier",16,"bold"),bg="gold", text="Analyse " + list[i].format(i+1),command=lambda index=i: button_clicked(index,men),bd=5, relief=RAISED)
        # button = tk.Button(men, text="Analyse {}".format(i+1), command=lambda index=i: button_clicked(index))
        buttons.append(button)
        button.grid(row=1, column=i)
