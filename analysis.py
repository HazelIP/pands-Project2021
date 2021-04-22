# This program stores the codes of outputing summary of variables to a text file, 
# save a histogram of each variable,
# output a scatter plot of each pair of variables
# Author: Ka Ling Ip

#import modules for data analysis and plots creation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
#import Iris dataset
df = pd.read_csv("iris.csv")

#summary of each variable outputed to a text file
def summary():
    with open ("Summary of data.txt","wt") as f: #create a txt file
        sys.stdout = f #direct the output to text file instead of console, ref[1]
        print("Rows of data and number of variables")
        print(df.shape)
        print("First 10 rows of the data")
        print(df.head(10))
        print ("******************************************************")
        print("Basic information of the data set")
        print(df.info()) # info of the data set, including sample size, data types?
        print(df.dtypes)
        print ("******************************************************")
        print("Count of Species")
        print(df['species'].value_counts())#show counts of each species
        print ("******************************************************")
        print("Statistical infomation of the numeric columns")
        print(df.describe()) #show statistical info of data, including mean, std, min, max and quartiles 
        print ("******************************************************")
        print("Correlation among the features of flowers")
        print(df.corr()) #show correlation between 4 features
        print ("**************************************************************")
# plot the heatmap ref
#sns.heatmap(corr, xticklabels=corr.columns,yticklabels=corr.columns, annot=True, cbar=True)
#plt.show()
#ref: https://likegeeks.com/seaborn-heatmap-tutorial/

# HISTOGRAM of each variable
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
# this section creat 4 subplots of the variables, ref[4]
def simple_hist_subplot():
    fig,((ax0,ax1),(ax2,ax3)) = plt.subplots(nrows=2,ncols=2)

    ax0.set_title("Distribution of Sepal Width", c='g')
    ax0.hist(df.sepal_width, bins=20, color='r')
    ax0.set(xlabel='Sepal width in cm', ylabel='Frequency') #ref[5]

    ax1.set_title("Distribution of Sepal Length",c='g')
    ax1.hist(df.sepal_length, bins=20, color='y')
    ax1.set(xlabel='Sepal length in cm', ylabel='Frequency')

    ax2.set_title("Distribution of Petal Width",c='g')
    ax2.hist(df.petal_width, bins=20, color='b')
    ax2.set(xlabel='Petal width in cm', ylabel='Frequency')

    ax3.set_title("Distribution of Petal Length",c='g')
    ax3.hist(df.petal_length, bins=20, color='purple')
    ax3.set(xlabel='Petal length in cm', ylabel='Frequency')
    plt.show()
#this section is histogram of each feature group by 3 species, ref[4]
def grouped_sepalL(): #Sepal Length
    sl1=df.loc[df.species=='setosa','sepal_length']
    sl2=df.loc[df.species=='versicolor','sepal_length']
    sl3=df.loc[df.species=='virginica','sepal_length']
    kwargs = dict(alpha=0.5, bins=20, stacked=True)
    plt.hist(sl1, color='r', label="Setosa", **kwargs)
    plt.hist(sl2, color='y', label="Versicolor", **kwargs)
    plt.hist(sl3, color='b', label="virginica", **kwargs)
    plt.title('Sepal Length grouped by species')
    plt.xlabel('Sepal Length') #name of x-axis
    plt.ylabel('Count') #name of y-axis
    plt.legend()
    plt.savefig("grouped_hist_sepal_length.png")
    plt.show ()
def grouped_sepalW(): #Sepal Width
    sl1=df.loc[df.species=='setosa','sepal_width']
    sl2=df.loc[df.species=='versicolor','sepal_width']
    sl3=df.loc[df.species=='virginica','sepal_width']
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
    sl1=df.loc[df.species=='setosa','petal_length']
    sl2=df.loc[df.species=='versicolor','petal_length']
    sl3=df.loc[df.species=='virginica','petal_length']
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
    sl1=df.loc[df.species=='setosa','petal_width']
    sl2=df.loc[df.species=='versicolor','petal_width']
    sl3=df.loc[df.species=='virginica','petal_width']
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

# SCATTERPLOT
# creating scatter plot of sepal length and width based on the 3 species, ref[2]
def sepal_scatter(): 
    groups = df.groupby("species") 
    for name, group in groups: 
        plt.plot(group["sepal_length"], group["sepal_width"], marker = "o", linestyle="", label = name)
    plt.title('Sepal width and length among the species')
    plt.legend() #show legend in the plot
    plt.xlabel('Sepal Length') #name of x-axis
    plt.ylabel('Sepal Width') #name of y-axis
    plt.text(4.5, 4.2,'Setosa',fontsize=10) #this put overlay text on plot, ref[3]
    plt.text(5.1, 2.1,'Versicolor', fontsize=10)
    plt.text(7.1, 3.4, 'Virginica', fontsize=10)
    plt.show()

# creating scatter plot of petal length and width based on the 3 species, ref[2]
def petal_scatter():
    groups = df.groupby("species")
    for name, group in groups: 
        plt.plot(group["petal_length"], group["petal_width"], marker = "o", linestyle="", label = name)
    plt.title('Petal width and length among the species')
    plt.legend()
    plt.xlabel('Petal Length') #name of x-axis
    plt.ylabel('Petal Width') #name of y-axis
    plt.text(2.1, 0.3,'Setosa',fontsize=10) #this put overlay text on plot
    plt.text(3.2, 1.55,'Versicolor', fontsize=10)
    plt.text(4.15, 2.2, 'Virginica', fontsize=10)
    plt.show()





# References:
#ref[1] https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
#ref[2] https://www.kite.com/python/answers/how-to-color-a-scatter-plot-by-category-using-matplotlib-in-python
#ref[3] https://towardsdatascience.com/how-to-add-text-labels-to-scatterplot-in-matplotlib-seaborn-ec5df6afed7a
#ref[4] https://machinelearningknowledge.ai/matplotlib-histogram-complete-tutorial-for-beginners/#Example_6_Histogram_for_visualizing_categories
#ref[5] https://stackoverflow.com/questions/52056261/how-to-set-label-for-each-subplot-in-a-plot-in-matplotlib