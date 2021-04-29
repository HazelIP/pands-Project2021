# This program stores the codes of outputing summary of variables to a text file, 
# save a histogram of each variable,
# output a scatter plot of each pair of variables
# Author: Ka Ling Ip

#import modules for data analysis and plots creation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
#import Iris dataset
df = pd.read_csv("iris.csv")

#summary of each variable outputed to a text file
def summary():
    with open ("Summary of data.txt","wt") as f: #create a txt file
        sys.stdout = f #direct the output to text file instead of console, ref[1]
        print("First 10 rows of the data")
        print(df.head(10))
        print ("***********************************************************************")
        print("Basic information of the data set")
        print(df.info()) # info of the data set, including sample size, data types
        print ("***********************************************************************")
        print("Count of Species")
        print(df['species'].value_counts())#show counts of each species
        print ("***********************************************************************")
        print("Statistical infomation of the numeric columns")
        print(df.describe()) #show statistical info of data, including mean, std, min, max and quartiles 
        print ("***********************************************************************")
        print("Correlation among the features of flowers")
        print(df.corr()) #show correlation between 4 features, ref[8]
        print ("***********************************************************************")

# the function shows the histogram of all variables
def histogram():
    sepalL_hist()
    sepalW_hist()
    petalL_hist()
    petalW_hist()
    species()

# HISTOGRAMs of each variable
def sepalL_hist(): #Histogram of sepal length distribution
    plt.hist(df.sepal_length,bins=15, edgecolor="white")
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length in cm")
    plt.ylabel("Count")
    plt.grid(axis="y")
    plt.savefig("hist_sepal_length.png")
    plt.show()
def sepalW_hist(): #Histogram of sepal width distribution
    plt.hist(df.sepal_width,bins=15, edgecolor="white")
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width in cm")
    plt.ylabel("Count")
    plt.grid(axis="y")
    plt.savefig("hist_sepal_width.png")
    plt.show()
def petalL_hist(): #Histogram of petal length distribution
    plt.hist(df.petal_length,bins=15, edgecolor="white")
    plt.title("Distribution of Petal Length")
    plt.xlabel("Petal Length in cm")
    plt.ylabel("Count")
    plt.grid(axis="y")
    plt.savefig("hist_petal_length.png")
    plt.show()
def petalW_hist(): #Histogram of petal width distribution
    plt.hist(df.sepal_length,bins=15, edgecolor="white")
    plt.title("Distribution of Petal Width")
    plt.xlabel("Petal Width in cm")
    plt.ylabel("Count")
    plt.grid(axis="y")
    plt.savefig("hist_petal_width.png")
    plt.show()
def species(): #Histogram of count of each species
    plt.hist(df['species'], bins=5, edgecolor="white")
    plt.title("Count of each species")
    plt.xlabel("Species")
    plt.ylabel("Count")
    plt.savefig("hist_species.png")
    plt.show()

# this function creates 4 subplots of the variables, ref[4]
def hist_subplot():
    fig,((ax0,ax1),(ax2,ax3)) = plt.subplots(nrows=2,ncols=2) # create a 2x2 subplot

    ax0.set_title("Distribution of Sepal Width", c='g') #position on top left, set title
    ax0.hist(df.sepal_width, bins=20, edgecolor='white', color='r') #extract data from sepal width column, make the bars red
    ax0.set(xlabel='Sepal width in cm', ylabel='Count') #ref[5] to set name of axis

    ax1.set_title("Distribution of Sepal Length",c='g') #position on top right, set title
    ax1.hist(df.sepal_length, bins=20, edgecolor='white', color='y') #extract data from sepal length column, make the bars yellow
    ax1.set(xlabel='Sepal length in cm', ylabel='Count')

    ax2.set_title("Distribution of Petal Width",c='g') #position on bottom left
    ax2.hist(df.petal_width, bins=20, edgecolor='white', color='b') #extract data from petal width, make the bars blue
    ax2.set(xlabel='Petal width in cm', ylabel='Count')

    ax3.set_title("Distribution of Petal Length",c='g') #position on bottom right
    ax3.hist(df.petal_length, bins=20, edgecolor='white', color='purple')#extract data from petal length, make the bars purple
    ax3.set(xlabel='Petal length in cm', ylabel='Count')
    plt.show()

#this section is histogram of each feature group by 3 species, ref[4]
def group_hist():
    grouped_petalL()
    grouped_petalW()
    grouped_sepalL()
    grouped_sepalW()

def grouped_sepalL(): #Sepal Length with 3 species indicated in different colors
    sl1=df.loc[df.species=='setosa','sepal_length'] #gp 1 as setosa, extract data from species column which = setosa and sepal length column
    sl2=df.loc[df.species=='versicolor','sepal_length']#gp 2 as versicolor
    sl3=df.loc[df.species=='virginica','sepal_length']#gp 3 as virginica
    kwargs = dict(alpha=0.5, bins=20, stacked=True) #setting of plot
    plt.hist(sl1, color='r', label="Setosa", **kwargs) #gp1 in red bars
    plt.hist(sl2, color='y', label="Versicolor", **kwargs) #gp2 in yellow bars
    plt.hist(sl3, color='b', label="virginica", **kwargs) #gp3 in blue bars
    plt.title('Sepal Length grouped by species')
    plt.xlabel('Sepal Length') #name of x-axis
    plt.ylabel('Count') #name of y-axis
    plt.legend()
    plt.savefig("grouped_hist_sepal_length.png")
    plt.show ()
def grouped_sepalW(): #Sepal Width with 3 species indicated in different colors
    sl1=df.loc[df.species=='setosa','sepal_width'] #gp 1 as setosa, extract data from species column which = setosa and sepal width column
    sl2=df.loc[df.species=='versicolor','sepal_width']#gp2 as versicolor
    sl3=df.loc[df.species=='virginica','sepal_width']#gp3 as virginica
    kwargs = dict(alpha=0.5, bins=20, stacked=True)
    plt.hist(sl1, color='r', label="Setosa", **kwargs)
    plt.hist(sl2, color='y', label="Versicolor", **kwargs)
    plt.hist(sl3, color='b', label="virginica", **kwargs)
    plt.title('Sepal Width grouped by species')
    plt.xlabel('Sepal Width') #name of x-axis
    plt.ylabel('Count') #name of y-axis
    plt.legend()
    plt.savefig("grouped_hist_sepal_width.png")
    plt.show ()
def grouped_petalL(): #Petal Width
    sl1=df.loc[df.species=='setosa','petal_length'] #gp 1 as setosa, extract data from species column which = setosa and petal length column
    sl2=df.loc[df.species=='versicolor','petal_length']#gp2 as versicolor
    sl3=df.loc[df.species=='virginica','petal_length']#gp3 as virginica
    kwargs = dict(alpha=0.5, bins=20, stacked=True)
    plt.hist(sl1, color='r', label="Setosa", **kwargs)
    plt.hist(sl2, color='y', label="Versicolor", **kwargs)
    plt.hist(sl3, color='b', label="virginica", **kwargs)
    plt.title('Petal Length grouped by species')
    plt.xlabel('Petal Length') #name of x-axis
    plt.ylabel('Count') #name of y-axis
    plt.legend()
    plt.savefig("grouped_hist_petal_length.png")
    plt.show ()
def grouped_petalW(): #Petal Width
    sl1=df.loc[df.species=='setosa','petal_width']#gp 1 as setosa, extract data from species column which = setosa and petal width column
    sl2=df.loc[df.species=='versicolor','petal_width']#gp2 as versicolor
    sl3=df.loc[df.species=='virginica','petal_width']#gp3 as virginica
    kwargs = dict(alpha=0.5, bins=20, stacked=True)
    plt.hist(sl1, color='r', label="Setosa", **kwargs)
    plt.hist(sl2, color='y', label="Versicolor", **kwargs)
    plt.hist(sl3, color='b', label="virginica", **kwargs)
    plt.title('Petal Width grouped by species')
    plt.xlabel('Petal Width') #name of x-axis
    plt.ylabel('Count') #name of y-axis
    plt.legend()
    plt.savefig("grouped_hist_petal_width.png")
    plt.show ()    

# SCATTERPLOT of all pairs of variables, 6 in total
def scatterplot():
    scatter_petal()
    scatter_sepal()
    scatter_SL_PL()
    scatter_SL_PW()
    scatter_SW_PL()
    scatter_SW_PW()
    
def scatter_petal(): #petal length+width pair
    plt.title('Relationship between petal width and length')
    plt.scatter(df['petal_length'], df['petal_width'], )
    plt.show()

def scatter_sepal():#sepal length+width pair
    plt.title('Relationship between sepal width and length')
    plt.scatter(df['sepal_length'], df['sepal_width'], )
    plt.show()

def scatter_SL_PL(): #sepal length+petal length pair
    plt.title('Relationship between sepal length and petal length')
    plt.scatter(df['sepal_length'], df['petal_length'], )
    plt.show()

def scatter_SL_PW(): #sepal length+petal width pair
    plt.title('Relationship between sepal length and petal width')
    plt.scatter(df['sepal_length'], df['petal_width'], )
    plt.show()

def scatter_SW_PL(): #sepal width+petal length pair
    plt.title('Relationship between sepal width and petal length')
    plt.scatter(df['sepal_width'], df['petal_length'], )
    plt.show()

def scatter_SW_PW(): ##sepal width+petal width pair
    plt.title('Relationship between sepal width and petal width')
    plt.scatter(df['sepal_width'], df['petal_width'], )
    plt.show()

# 4 scatterplots with pairs of variable indicated correlated 
def group_scatterplot():
    gp_sepal_scatter() #sepal length & width
    gp_petal_scatter() #petal length & width
    gp_SL_PL_scatter() #sepal length & petal length
    gp_SL_PW_scatter() #sepal length & petal width

# creating scatter plot of sepal length and width based on the 3 species, ref[2]
def gp_sepal_scatter(): 
    groups = df.groupby("species") #3 species defines as groups
    for name, group in groups:  
        plt.plot(group["sepal_length"], group["sepal_width"], marker = "o", linestyle="", label = name) #plot with SL & SW column
    plt.title('Sepal width and length among the species')
    plt.legend() #show legend in the plot
    plt.xlabel('Sepal Length') #name of x-axis
    plt.ylabel('Sepal Width') #name of y-axis
    plt.text(4.5, 4.2,'Setosa',fontsize=10) #this put overlay text on plot, ref[3]
    plt.text(5.1, 2.1,'Versicolor', fontsize=10)
    plt.text(7.1, 3.4, 'Virginica', fontsize=10)
    plt.show()

# creating scatter plot of petal length and width based on the 3 species, ref[2]
def gp_petal_scatter():
    groups = df.groupby("species")
    for name, group in groups: 
        plt.plot(group["petal_length"], group["petal_width"], marker = "o", linestyle="", label = name) #plot with PL & PW column
    plt.title('Petal width and length among the species')
    plt.legend()
    plt.xlabel('Petal Length') #name of x-axis
    plt.ylabel('Petal Width') #name of y-axis
    plt.text(2.1, 0.3,'Setosa',fontsize=10) #this put overlay text on plot
    plt.text(3.2, 1.55,'Versicolor', fontsize=10)
    plt.text(4.15, 2.2, 'Virginica', fontsize=10)
    plt.show()

#creating scatter plot of sepal length+petal Length
def gp_SL_PL_scatter():
    groups = df.groupby("species") 
    for name, group in groups: 
        plt.plot(group["sepal_length"], group["petal_length"], marker = "o", linestyle="", label = name) #plot with SL & PL
    plt.title('Sepal length and Petal length among the species')
    plt.legend() #show legend in the plot
    plt.xlabel('Sepal Length') #name of x-axis
    plt.ylabel('Petal Length') #name of y-axis
    plt.text(4.5, 2.2,'Setosa',fontsize=10) #this put overlay text on plot, ref[3]
    plt.text(5.0, 4.0,'Versicolor', fontsize=10)
    plt.text(7.0, 6.5, 'Virginica', fontsize=10)
    plt.show()
#creating scatter plot of sepal lenght +petal width
def gp_SL_PW_scatter():
    groups = df.groupby("species") 
    for name, group in groups: 
        plt.plot(group["sepal_length"], group["petal_width"], marker = "o", linestyle="", label = name) #plot with SL & PW
    plt.title('Sepal length and petal width among the species')
    plt.legend() #show legend in the plot
    plt.xlabel('Sepal Length') #name of x-axis
    plt.ylabel('Petal Width') #name of y-axis
    plt.text(4.5, 0.5,'Setosa',fontsize=10) #this put overlay text on plot, ref[3]
    plt.text(6.5, 1.0,'Versicolor', fontsize=10)
    plt.text(5.7, 2.1, 'Virginica', fontsize=10)
    plt.show()

def heatmap(): 
    corr = df.corr()
    #plot the heatmap, ref[9][10], with tick labels, color bar and correlation coefficient on plot
    sns.heatmap(corr, xticklabels=corr.columns,yticklabels=corr.columns, annot=True, cbar=True)
    plt.show()

'''References:
[3] https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
[4] https://www.kite.com/python/answers/how-to-color-a-scatter-plot-by-category-using-matplotlib-in-python
[5] https://towardsdatascience.com/how-to-add-text-labels-to-scatterplot-in-matplotlib-seaborn-ec5df6afed7a
[6] https://machinelearningknowledge.ai/matplotlib-histogram-complete-tutorial-for-beginners/#Example_6_Histogram_for_visualizing_categories
[7] https://stackoverflow.com/questions/52056261/how-to-set-label-for-each-subplot-in-a-plot-in-matplotlib
[8] https://realpython.com/numpy-scipy-pandas-correlation-python
[9] https://likegeeks.com/seaborn-heatmap-tutorial/
[10]http://seaborn.pydata.org/examples/many_pairwise_correlation.html'''
