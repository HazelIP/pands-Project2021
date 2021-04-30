# Programing and Scripting 2021 -- Project
### Author: Ka Ling Ip (G00398581)
--------------------------------------------

This README is a summary of the exploratory analysis of Fishers' Iris Data Set. It contains background and summary of the dataset, analysis carried out with explaination of codes, as well as a brief conclusion of the analysis. 

## **Background of the Fisher Iris Dataset**
-----------------------------------------------
The Fisher's Iris data set is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in 1930s. It is sometimes called Anderson's Iris data set because Edgar Andersoncollected the data to quantify the morphologic variation of Iris flowers of three related species. [Ref 1]
This dataset consists of 50 records for each of three Iris species: Iris setosa, Iris virginica, and Iris versicolor. Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. The data set is well analyzed and used in the field of machine learning and data mining. The data set "iris.csv" was imported as a data frame for analysis.

## **Summary of dataset**
--------------------------
A function "summary()" generates summary of the data set and outputs it to a text  file, named “Summary of data.txt”. 
- Overview 
The command "df.head(10)" displays the first 10 rows of the data set, while "df.shape" shows there are 150 rows of data and 5 variables. 

- Information of dataset 
The function "df.info()" displays information of all the variables, including . There are 5 columns of variable, and 150 rows of data, no null value. There are 4 numeric columns namely data of sepal length, sepal width, petal length, and petal width, all measured in cm. The last variable is an object. The function "df['species'].value_counts()" denotes there are 3 Iris species in the dataset, namely Iris Setosa, Iris Versicolor, and Iris Virginica, 50 counts of sample for each species. 

- Statistical infomation of numeric variables
The function "df.describe()" displays statistical infomation including mean, minimum value, maximum value, standard deviation and percentiles of all of the numeric variables. 

- Correlation among the variables #ref[]
The function "df.corr()" generates a table of correlation among the 4 features. The table indicates there are strong positive correlations between (i) petal length and petal width, (ii) sepal length and petal length, (iii) sepal length and petal width. Visualization of the correlation will be showngb4 in a heatmap in the next section. 

## **Visualization of dataset**
--------------------------------
### 1. Histogram
The function "histogram()" generates histograms visualizing the distribution of all variables, incluing sepal length, sepal width, petal length, petal width and species. All the histograms generated are saved as a png file. 
```python
    def histogram():
        sepalL_hist()
        sepalW_hist()
        petalL_hist()
        petalW_hist()
        species()
```        
For sake of easier comparison, a subplot consists of all the above histograms is generated and saved as a png file by the function "hist_subplot()". 
```python       
    def hist_subplot():
        fig,((ax0,ax1),(ax2,ax3)) = plt.subplots(nrows=2,ncols=2)
        ax0.set_title("Distribution of Sepal Width", c='g')
        ax0.hist(df.sepal_width, bins=20, edgecolor='white',color='r')
        ax0.set(xlabel='Sepal width in cm', ylabel='Count') #ref[5]
        ax1.set_title("Distribution of Sepal Length",c='g')
        ax1.hist(df.sepal_length, bins=20, edgecolor='white',color='y')
        ax1.set(xlabel='Sepal length in cm', ylabel='Count')
        ax2.set_title("Distribution of Petal Width",c='g')
        ax2.hist(df.petal_width, bins=20, edgecolor='white',color='b')
        ax2.set(xlabel='Petal width in cm', ylabel='Count')
        ax3.set_title("Distribution of Petal Length",c='g')
        ax3.hist(df.petal_length, bins=20, edgecolor='white',color='purple')
        ax3.set(xlabel='Petal length in cm', ylabel='Count')
        plt.show()
```        
However, the above histograms do not give much insight of the data set. Another set of historgrams are generated by calling the function "group_hist()" for each variable with 3 species shown in different colors in the same plot. 
```python
    def group_hist():
        grouped_petalL()
        grouped_petalW()
        grouped_sepalL()
        grouped_sepalW()
```        
From this set of histograms, it seems that Iris Setosa is distinctively smaller than the other 2 species in both petal length and petal width, while Iris Versicolor and Iris Virginica are not as easy to differentiate based on the features in the dataset.  

### 2. Scatterplot
Scatterplot is a useful summary of a set of bivariate data, which normally used to observe and visually display the relationship between 2 variables [ref 2]. The function "scatterplot()" generates scatterplot which shows the relatopnship between pairs of variables.
```python        
    def scatterplot():
        scatter_petal()
        scatter_sepal()
        scatter_SL_PL()
        scatter_SL_PW()
        scatter_SW_PL()
        scatter_SW_PW()
```        
The above plots show there are linear correlations between (i)petal length and petal width, (ii) sepal length and petal length, (iii) sepal length and petal width.
Species was then introduced as a categorical third variable for plotting another set of scatterplots. The 3 species were indicated in different colors. 
```python       
    def group_scatterplot():
        gp_sepal_scatter()
        gp_petal_scatter()
        gp_SL_PL_scatter()
        gp_SL_PW_scatter()
```        
The plots further indicates Iris Setosa is distinct from the other 2 species, in both petal and sepal size, while Iris Versicolor and Iris Virginica are clustered together based on their species, but not distinctive from each other. 

### 3. Heatmap
A Heatmap helps to visualize the coorelation among the variables. By calling "heatmap()", a plot is generated with different colors and labels in the plot indicating the strength of correlation. 
```python        
    def heatmap()
        corr = df.corr()
        mask = np.triu(np.ones_like(corr(), dtype=np.bool))#masking the upper
        map = sns.heatmap (corr, mask=mask, vmin=-1, vmax=1, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cbar=True)
        map.set_title ("Correlation Heatmap of variables", fontdict={'fontsize':18}, pad=15)
        plt.show() )
```
It is clearly shown in the plot that (i)sepal length & petal length, (ii) sepal length & petal width, (iii) petal length & petal width are highly positively correlated. 

## **Conclusion**
------------------
1. The data set consist of 4 numeric variables which are the 4 features of Iris flowers, and 1 non-numberic variable which is the 3 species of Iris flowers. It is a balanced data set with 50 samples from each species. All features of all samples are present, with no null value.  

2. A set of histogram shows distribution of each variables. A set of grouped histograms indicates some distinctivenss of Iris Setosa from the other 2 Iris species. 

3. A set of scatterplot shows relationship between pairs of variables, indicating linear correlation between petal length and petal width. The scatterplot grouped by species further confirms Iris Setosa is distinct from the other 2 species in petal length and width.   

4. A heat map indicates 3 pairs of variables, namely (i)sepal length & petal length, (ii) sepal length & petal width, (iii) petal length & petal width are highly positively correlated. 


## **Reference**
------------------
[1] [Wikipedia - Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)\
[2] [Chartio - What is a scatterplot](https://chartio.com/learn/charts/what-is-a-scatter-plot/)\

### References used in analysis.py:
[3] [Stackabuse - writing to a file with pythons print function](https://stackabuse.com/writing-to-a-file-with-pythons-print-function/)\
[4] [Kite - how to color a scatterplot by category using matplotlib in python](https://www.kite.com/python/answers/how-to-color-a-scatter-plot-by-category-using-matplotlib-in-python)\
[5] [Toward Data Science](https://towardsdatascience.com/how-to-add-text-labels-to-scatterplot-in-matplotlib-seaborn-ec5df6afed7a)\
[6] [Machine Learning Knowledge](https://machinelearningknowledge.ai/matplotlib-histogram-complete-tutorial-for-beginners/#Example_6_Histogram_for_visualizing_categories)\
[7] [Stackoverflow - set label for subplot](https://stackoverflow.com/questions/52056261/how-to-set-label-for-each-subplot-in-a-plot-in-matplotlib)\
[8] [Real Python - Correlation](https://realpython.com/numpy-scipy-pandas-correlation-python/)\
[9] [Likegeeks - Seaborn heatmap](https://likegeeks.com/seaborn-heatmap-tutorial/)\
[10] [Seaborn - Correlation](https://seaborn.pydata.org/examples/many_pairwise_correlations.html)\
### Unquoted references
[10] [GitHub](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)\
[11] [Toward Data Science - Iris dataset](https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d)\ 
