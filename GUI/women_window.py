from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

from scipy.ndimage.measurements import label
from Graph import men_pd

def button_clicked(index,men):
    if(index==0):
        return 1
    elif(index==1):
        return 1
    elif(index==2):
        return 1

def WomenNotebook(women):
    women.pack(expand=True)