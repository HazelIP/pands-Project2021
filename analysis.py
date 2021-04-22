# This program stores the codes of outputing summary of variables to a text file, 
# save a histogram of each variable,
# output a scatter plot of each pair of variables
# Author: Ka Ling Ip

#import modules for data analysis and plots creation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import Iris dataset
df = pd.read_csv("iris.csv")

#summary of each variable
with open ("trial_summary.txt","wt") as f:  #ref[1]
    sys.stdout = f
    print("Basic information of the data set")
    print(df.info()) # info of the data set, including sample size, data types?
    print("Statistical infomation of the numeric variables")
    print(df.describe()) #show statistical info of data, including mean, std, min, max and quartiles 
    print("Count of Species")
    print(df['species'].value_counts())#show counts of @species
    print("Correlation among the variables")
    print(df.corr()) #show correlation between variables
    print(df.dtypes())

# creating scatter plot of sepal length and width based on the 3 species  
groups = df.groupby("species")
def sepal_scatter():
    for name, group in groups: 
        plt.plot(group["sepal_length"], group["sepal_width"], marker = "o", linestyle="", label = name)
    plt.title('Sepal width and length among the species')
    plt.legend() #show legend in the plot

    plt.text(4.5, 4.2,'Setosa',fontsize=10) #this put overlay text on plot
    plt.text(5.1, 2.1,'Versicolor', fontsize=10)
    plt.text(7.1, 3.4, 'Virginica', fontsize=10)
    plt.show()

# creating scatter plot of petal length and width based on the 3 species
def petal_scatter():
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

sepal_scatter()
petal_scatter()