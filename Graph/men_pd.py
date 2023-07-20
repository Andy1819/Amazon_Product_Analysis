import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def convert_to_dataframe():
    # Load data from CSV into a Pandas DataFrame
    data = pd.read_csv('./datasets/data_shirts.csv',error_bad_lines=False)
    data['Rating']=pd.to_numeric(data['Rating'],errors='coerce')
    data['Price']=pd.to_numeric(data['Price'],errors='coerce')
    return data

def graph_1(data,men):
    # Create a Word Cloud of the Brand column
    brand_text = " ".join(data['Brand'].dropna().tolist())
    shirt_mask = np.array(Image.open('./images/men_shirt.webp'))
    wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='tab20c',mask=shirt_mask).generate(brand_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Word Cloud of Brands')
    plt.tight_layout()

    # Convert the plot to a Tkinter widget and add it to the specified frame
    chart_type = FigureCanvasTkAgg(plt.gcf(), master=men)
    chart_type.draw()
    chart_type.get_tk_widget().grid(row=2, column=0, columnspan=4)
    

def graph_2(data,men):
    # Create a graph using Seaborn
    
    sns.set(style="darkgrid")
    plt.figure(figsize=(10, 5))  # Adjust the figsize as desired
    ax = sns.lineplot(x='Price', y='Rating', data=data)
    ax.set_title('Price vs Rating')
    ax.set_xlabel('Price')
    ax.set_ylabel('Rating')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=80)  # Rotate x-axis labels by 180 degrees
    plt.tight_layout()

    # Convert the plot to a Tkinter widget and add it to the specified frame
    chart_type = FigureCanvasTkAgg(plt.gcf(), master=men)
    chart_type.draw()
    chart_type.get_tk_widget().grid(row=3, column=0, columnspan=4)

def graph_3(data,men):
    # Create a graph using Seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    ax = sns.scatterplot(x='Brand', hue='Rating',y='Price', data=data, palette='rocket_r')
    ax.set_title('Brand vs Price')
    ax.set_xlabel('Brand')
    ax.set_ylabel('Price')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Convert the plot to a Tkinter widget and add it to the specified frame
    chart_type = FigureCanvasTkAgg(plt.gcf(), master=men)
    chart_type.draw()
    chart_type.get_tk_widget().grid(row=4, column=0, columnspan=4)

def show_graph(men):
    data = convert_to_dataframe()
    graph_1(data,men)
    graph_2(data,men)
    graph_3(data,men)
