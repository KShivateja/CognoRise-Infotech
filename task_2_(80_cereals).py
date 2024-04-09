# -*- coding: utf-8 -*-
"""Task 2 (80 CEREALS).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11_dh4aj9JcXpHdLlqnpegBLEHiyyz7ZI

# **Task 2 80 CEREALS**
"""

from PIL import Image
from IPython.display import display

# Upload the image file directly to Colab
from google.colab import files
uploaded = files.upload()

# Once the upload is done, you can use the file name to open and display the image
image_path = "Screenshot 2024-04-05 145435.png"  # Replace with the name of your uploaded image

# Open the image
image = Image.open(image_path)

# Display the image
display(image)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.metrics import mean_squared_error
import plotly.express as px
import plotly.graph_objects as go

"""# To read the data"""

from google.colab import files
import pandas as pd

# Upload the CSV file
uploaded = files.upload()

# Extract the filename from the uploaded dictionary
filename = list(uploaded.keys())[0]

# Read the CSV file into a DataFrame
import io
Cereals = pd.read_csv(io.BytesIO(uploaded[filename]))

"""# Display the first few rows of the DataFrame"""

Cereals.head()

Cereals

"""# To view the data"""

Cereals.info()

"""#Display the last few rows of the DataFrame"""

Cereals.tail()

"""#To Know the shape"""

Cereals.shape

"""#To know the size of the dataframe"""

Cereals.size

"""#To get Column Names"""

Cereals.columns

Cereals.dtypes

Cereals.describe()

"""#Checking for Nulls"""

Cereals.isnull().sum()

"""#Instead of changing the data type of manufacturing company column we will rename it as it would be easy for us for visualization"""

mfg = {'A':'American Home Food Products','G':'General Mills','K':'Kelloggs',
       'N':'Nabisco','P':'Post','Q':'Quaker Oats','R':'Ralston Purina'}
Cereals['mfr'] = Cereals['mfr'].replace(mfg)

"""# Checking top 5 cereal from different manufacturers having highest customer rating"""

top_5_rating = Cereals.sort_values(by='rating' ,ascending=False).reset_index(drop=True).head()
top_5_rating

"""# Lets check which cereals are kept on shelf's"""

shelf = Cereals.shelf.unique()
for i in range(0,len(shelf)):
    print('shelf number: ',shelf[i])
    print('_'*50)
    print(Cereals.loc[Cereals['shelf'] == shelf[i]].reset_index(drop=True).head())
    print('_'*50)

"""# Lets calculate top 5 cereal from unique manufacturers"""

all_manufacturer = Cereals.mfr.unique()

# Using for loop
for i in range(0,len(all_manufacturer)):
    print(all_manufacturer[i])
    print('_'*50)
    print(Cereals.loc[Cereals['mfr'] == all_manufacturer[i]].reset_index(drop=True).head())
    print('_'*50)

"""#Exploratory Data Analysis"""

Cereals.describe()

"""#Data Visualization

#Lets findout Average Ratings of Manufacturers
"""

plt.figure(figsize=(10,10))
Cereals.groupby('mfr')['rating'].mean().plot.bar(color='b')
plt.title('Average Ratings of Manufacturers')
plt.show()

"""We have,

A = American Home Food Products

G = General Mills

K = Kelloggs

N = Nabisco

P = Post

Q = Quaker Oats

R = Ralston Purina

Nabisco has the highest rating while General Mills the lowest. On average, the ratings among manufacturers follows a uniform distribution.

#Ratings of cereals over their names, with different colors for different manufacturers.
"""

fig = px.line(Cereals, x='name', y='rating', color='mfr', markers=True)
fig.show()

"""#Distribution of products based on manufacturers"""

# You're counting the occurrences of each manufacturer in the 'mfr' column
Cereals1 = Cereals['mfr'].value_counts().to_frame().reset_index()

# Creating a pie chart using Plotly Express
fig = px.pie(Cereals1,
             values='mfr',  # Values for the pie chart (number of products)
             names=Cereals1.index,  # Use the index directly for names
             title='Percentage of products as per manufacturer',  # Title of the plot
             color_discrete_sequence=px.colors.sequential.RdBu  # Color sequence for the slices
            )

# Display the pie chart
fig.show()

"""# categorize cereals based on their ratings into different ranges"""

rating_between_0_to_25 = Cereals.loc[Cereals['rating'] < 25]
rating_between_25_to_50 = Cereals[(Cereals['rating'] >25.0) & (Cereals['rating']<50.0)]
rating_between_50_to_75 = Cereals[(Cereals['rating'] >50.0) & (Cereals['rating']<75.0)]
rating_between_75_to_100 = Cereals[(Cereals['rating'] >75.0) & (Cereals['rating']<100.0)]

def rating(shelf):
    fig = px.scatter(shelf, x="rating", y="calories",
                     size="fiber", color="name",
                     hover_name="mfr", size_max=60)
    fig.show()
rating(rating_between_0_to_25)
rating(rating_between_25_to_50)
rating(rating_between_50_to_75)
rating(rating_between_75_to_100)

"""#Top 5 cereal as per their rating from consumers"""

Smfr_names = Cereals.mfr.unique()
mfr_names
def top_5(data):
    for i in range(0,len(mfr_names)):
        name = mfr_names[i]
        plotting_data = data.loc[data['mfr'] == name].sort_values(by='rating',ascending=False).head()
        print("Top 5 cereal of %s as per their rating from consumers"%name)
        fig = px.bar(plotting_data, x='name', y='rating' ,
                    hover_name="name")
        fig.show()
top_5(Cereals)