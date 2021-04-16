# this is drafting of codes - scatter plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv") #importing file
groups = df.groupby("species") 
# sepal length and width
def sepal_scatter():
    for name, group in groups: #ref[1]
        plt.plot(group["sepal_length"], group["sepal_width"], marker = "o", linestyle="", label = name)
    plt.title('Sepal width and length among the species')
    plt.legend()
    #add text in plot, syntax:plt.text(x=x coordinate, y=y coordinate, s=string to be displayed) ref[2]
    plt.text(4.5, 4.2,'Setosa',fontsize=10) #this put overlay text on plot ref[]
    plt.text(5.1, 2.1,'Versicolor', fontsize=10)
    plt.text(7.1, 3.4, 'Virginica', fontsize=10)
    plt.show()

# petal length and width
def petal_scatter():
    for name, group in groups: 
        plt.plot(group["petal_length"], group["petal_width"], marker = "o", linestyle="", label = name)
    plt.title('Petal width and length among the species')
    plt.legend()
    plt.text(2.1, 0.3,'Setosa',fontsize=10) 
    plt.text(3.2, 1.55,'Versicolor', fontsize=10)
    plt.text(4.15, 2.2, 'Virginica', fontsize=10)
    plt.show()

sepal_scatter()
petal_scatter()
#REF:
#[1] https://www.kite.com/python/answers/how-to-color-a-scatter-plot-by-category-using-matplotlib-in-python
#[2] https://towardsdatascience.com/how-to-add-text-labels-to-scatterplot-in-matplotlib-seaborn-ec5df6afed7a
#[3] 