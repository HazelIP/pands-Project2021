# Pands Project 2021
---------------------

## Programing and Scripting 2021 -- Project
## Author: Ka Ling Ip (G00398581)

This README is a summary of the exploratory analysis of Fishers' Iris Data Set. It contains background of the dataset, analysis carried out with explaination of codes, as well as a brief conclusion of the analysis. 

### Background of the Fisher Iris Dataset 

The Fisher's Iris data set is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in 1930s. It is sometimes called Anderson's Iris data set because Edgar Andersoncollected the data to quantify the morphologic variation of Iris flowers of three related species. [ref: https://en.wikipedia.org/wiki/Iris_flower_data_set]
This dataset consists of 50 records for each of three Iris species: Iris setosa, Iris virginica, and Iris versicolor. Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. The data set is well analyzed and used in the field of machine learning and data mining. The data set "iris.csv" was imported as a data frame for analysis.

### Summary of data (what are the code)

- the part of codes generated column, data types, statistical info
- A summary of the data is outputted to a text file, named “Summary of data.txt”. 

#### The part of code [“”, count of species ] shows basic information of the data set. 
The data set consists of 150 rows of data and 5 columns of variable. There are 4 numeric columns namely data of sepal length, sepal width, petal length, and petal width, all measured in cm. The last variable is an object which denotes 3 Iris species, namely Iris Setosa, Iris Versicolor, and Iris Virginica.  There are 50 samples from each of the three Iris species, adding up to 150 rows of data. There is no null value in the data set. 

Statistical information of the numeric columns [CODES]
Including mean, min, max and quartiles of each numeric column. 

#### Correlation of the variables
-	Code
-	Correlation plot,
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)
-	Insight: sepal length + petal length; sepal length + petal width; petal length + petal width highly positively correlated. 


### Histogram 
- codes ** generates histogram of each variable and help visualizing the distribution of data 
- save as a png file. 
- for sake of comparison, a subplots was also generated (“code”); 
- insight of hist: Distinctiveness 


### Scatter plot, what the code generates 
- level 1: mixed scatter plot: codes; doesn’t tell muchl;
- grouped by species: setosa is distinct from other 2
- insight of scatter


#### Conclusion
- from histogram, it's a balanced data set, distribution of each variables 
- from scatterplot which was grouped by speices, Setosa is distinct from other 2 species in petal length and width, while versicolor and virginca  
- from correlation, 

v.	Summary??
https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d 

https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d 
- simple logistic regression 

-	Linear regression vs logistic regression?

To-do list:
1.	Import data, and upload to git hub
2.	Writing summary of dataset, framing questions
3.	Histogram of 5 variables (codes)
4.  Scatterplot of pairs of variables (codes)
5.	Tidying ref and comments


Reference: 
Pands weekly task readme ref
https://github.com/andrewbeattycourseware/pands-problems/blob/master/README.md 
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

#ref[1] https://machinelearningknowledge.ai/matplotlib-histogram-complete-tutorial-for-beginners/#Example_6_Histogram_for_visualizing_categories
#ref[2] https://stackoverflow.com/questions/52056261/how-to-set-label-for-each-subplot-in-a-plot-in-matplotlib

Reference part
correlation plot: https://stackoverflow.com/questions/29432629/plot-correlation-matrix-using-pandas
[1]
[2]
