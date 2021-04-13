#show size of data
#show distribution
#show correlation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
print(df.head(10)) #a brief look of the data
print(df.info()) # more info of the data set
print(df.describe()) #show statistical info of data
print(df.shape) #show size of data
print(df.columns) #show names of column
print(df['species'].value_counts())#show counts of @species
print(df.corr()) #show correlation between variables

setosa = df.loc[df['species']=="setosa"]
versicolor = df.loc[df['species']=="versicolor"]
virginica = df.loc[df['species']=="virginica"]
print (setosa)