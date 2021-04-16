# some codes for trial of histograms
# 1 histogram @ variable (sepal l & w, petal l & w, species count)
# or i can do 4 subplots
# or 4 plots each with 3 bars representing 3 species 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")
#this section is simply 4 bar charts of 4 variables
def simple_hist(): 
    plt.hist(df.sepal_length,bins=20)
    plt.title("Histogram showing Sepal Length of the whole sample")
    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.savefig("simple_hist_sepal_length.png")
    plt.show()
#this section is 3 bars of sepal length of 3 species, ref[1]
def grouped_hist():
    sl1=df.loc[df.species=='setosa','sepal_length']
    sl2=df.loc[df.species=='versicolor','sepal_length']
    sl3=df.loc[df.species=='virginica','sepal_length']
    kwargs = dict(alpha=0.5, bins=20, stacked=True)
    plt.hist(sl1, color='r', label="Setosa", **kwargs)
    plt.hist(sl2, color='y', label="Versicolor", **kwargs)
    plt.hist(sl3, color='b', label="virginica", **kwargs)
    plt.title('Sepal Length grouped by species')
    plt.xlabel('Sepal Length') #name of x-axis
    plt.ylabel('Frequency') #name of y-axis
    plt.legend()
    plt.savefig("grouped_hist_sepal_length.png")
    plt.show ()



#use subplot to show 4 histograms
#fig, axes = plt.subplots(2, 2, figsize=(16,9))
#axes[0,0].set_title("Distribution of Sepal Width")
#axes[0,0].hist(iris_df['sepal_width'], bins=5);
#axes[0,1].set_title("Distribution of Sepal Length")
#axes[0,1].hist(iris_df['sepal_length'], bins=7);
#axes[1,0].set_title("Distribution of Petal Width")
#axes[1,0].hist(iris_df['petal_width'], bins=5);
#axes[1,1].set_title("Distribution of Petal Length")
#axes[1,1].hist(iris_df['petal_length'], bins=6);

#ref[1] https://machinelearningknowledge.ai/matplotlib-histogram-complete-tutorial-for-beginners/#Example_6_Histogram_for_visualizing_categories