from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

from scipy.ndimage.measurements import label
# from Graph import kid_pd

# def button_clicked(index,kid):
#     if(index==0):
#         return kid_pd.show_graph(kid,index)
#     elif(index==1):
#         return kid_pd.show_graph(kid,index)
#     elif(index==2):
#         return kid_pd.show_graph(kid,index)

def MenNotebook(kid):
    kid.pack(expand=True)

    labels = []
    buttons = []
    list=["Shirts","T-Shirts","Jeans"]

    image_paths = ["./images/men_shirt.webp", "./images/men_tshirt.webp", "./images/men_jeans.webp"]
    images = [Image.open(path).resize((400,400)) for path in image_paths]
    photo_images = [ImageTk.PhotoImage(image) for image in images]

    for i in range(3):
        label = tk.Label(kid, image=photo_images[i],bd=5,relief=SUNKEN)
        label.image=photo_images[i]
        labels.append(label)
        label.grid(row=0, column=i,padx=50,pady=20)

        # button = tk.Button(kid,font=("Courier",16,"bold"),bg="gold", text="Analyse " + list[i].format(i+1),command=lambda index=i: button_clicked(index,kid),bd=5, relief=RAISED)
        # buttons.append(button)
        # button.grid(row=1, column=i)