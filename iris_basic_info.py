#show size of data
#show distribution
#show correlation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
# print("A brief look of the data", df.head(10)) #a brief look of the data
print("Basic information of the data set")
print(df.info()) # info of the data set, including sample size, data types?
print("Statistical infomation of the variables")
print(df.describe()) #show statistical info of data, including mean, std, min, max and quartiles 
# print("size of data", df.shape) #show size of data, 150 sample and 5 variables
# print("names of column", df.columns) #show names of column
print("Count of Species")
print(df['species'].value_counts())#show counts of @species
print("Correlation among the variables")
print(df.corr()) #show correlation between variables

setosa = df.loc[df['species']=="setosa"]
versicolor = df.loc[df['species']=="versicolor"]
virginica = df.loc[df['species']=="virginica"]
# print (setosa) this print all data of species Setosa