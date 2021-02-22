# MS5114 - Individual Assignment 3
# Student ID: 19230487   Student Name: Jayakarthi Boovendran



# 1. Import numpy and pandas on this document
import numpy as np
import pandas as pd
import math as math
import seaborn as sb

# 2. Write a NumPy program to generate a random number between 0 and 1
rand_numb=np.random.uniform(0,1)
print(rand_numb)
#Since size is default here, only single value is returned




# 3. Write a NumPy program to create a 3x3 identity matrix.
print('3x3 Identity Matrix:\n')
Imax = np.identity(3)
print(Imax)



# 4. Write a NumPy program to create an array of the integers from 30 to 70
print("Array of integers from 30 to 70:\n")
array=np.arange(30,71)
print(array)



# 5. Write a NumPy program to convert a given array into a list and then convert it into a list again.
print('Numpy Conversion\n')
array=np.arange(10,20)
print('Array : ',array)

temp_list=array.tolist()
print('\nList  : ',temp_list)

temp_array=np.asarray(temp_list)
print('\nArray : ',temp_array)




# 6. Write a Python program to find the maximum and minimum value of a given flattened array. Go to the editor
# Expected Output:
# Original flattened array:
# [[0 1]
# [2 3]]
# Maximum value of the above flattened array:
# 3
# Minimum value of the above flattened array:
# 0
array=np.array([[0,1], [2,3]])
print("Original flattened array:")
print(array)
print("Maximum value of the above flattened array:")
print(np.amax(array))
print("Minimum value of the above flattened array:")
print(np.amin(array))



# 7. Write a NumPy program to compute the median of flattened given array.
array = np.arange(11)
print("Original array:",array)
print("Median of given array:",np.median(array))



# 8. Write a NumPy program to compute the weighted average of a given array
# Sample Output:
# Original array:
# [0 1 2 3 4]
# weights: [1, 2, 3, 4, 5]
# Weighted average of the said array:
# 2.6666666666666665

array = np.arange(5)
print("Original array:",array)
weights = np.arange(1, 6)
print("weights:",weights.tolist())
print("Weighted average of the said array:")
print(np.average(array, weights=weights))




# 10. Write a NumPy program to compute the mean, standard deviation, and variance of a
# given array along the second axis.
# Sample output:
# Original array:
# [0 1 2 3 4 5]
# Mean: 2.5
# std: 1
# variance: 2.9166666666666665

array = np.arange(6)
print("Original array:")
print(array)
print("Mean: ",np.mean(array))

std=np.std(array,axis=0)
print("std: ",math.floor(std))

var=np.var(array)
assert np.allclose(var,np.mean((array - np.mean(array)) ** 2 ))
print("variance: ",var)




# 11. Open the given dataset using Pandas (Forbes Global 2000 - 2019.csv)
# Using NumPy and Pandas, answer the following questions from the given dataset:


# what is the The cumulative market value of each industry?
df = pd.read_csv("C:\\Users\\Jaya Karthi Booven\\Downloads\\Forbes_Global_2000_2019(1).csv") #the Forbes Global data is stored in a dataframe
print(df.groupby(['Industry'])['Market Value'].sum()) #Aggregate 'Market Value' is computed based on Industries



# Which industry is the most profitable (in terms of revenue, profits) and which hold the highest asset value?
                                                                                             #              Profit    Revenue
print(df.groupby(['Industry'])['Profits','Revenue'].sum().nlargest(1,['Profits','Revenue'])) #Major Banks : 443.6525  2425.803
print(df.groupby(['Industry'])['Assets'].sum().nlargest(1)) #Major Banks    60649.946
#The Highest asset value is computed by summing assets values under each industry.
#Similarly the industry with highest profit and revenue represents the consolidated values obtained by grouping the Industries


# Is there any correlation between profit and asset values?
# Pearson Correlation b/w fields of Dataframe and is mapped to a heat plot
pearsoncorr=df.corr(method='pearson')
sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)
#The correlation b/w the above data fields is represented as 'orange' -> representing strong positive correlation.(correlation coefficient>0.5)
#Where as very strong positive correlation is represented as dark-orange(correlation coefficient=1)

#Correlation specific to 'Profit' and 'Assests'
print('Correlation Coefficient b/w Profits and Assets:',df['Profits'].corr(df['Assets']))
#The Correlation coefficient value of 0.560699975897584 represents a strong positive correlation b/w 'Profit' and 'Assets'




# What are the Top 10 companies (names) that have
# a) highest profits as a % to assets; and
df.nlargest(10,['Profits as % of Assets'])['Company']   #Top 10 companies with highest profit % to assest is computed using nlargest() and the associated company names are displayed

# b) highest profits as a % to revenue.
df.nlargest(10,['Profits as % of Revenue'])['Company']  #Top 10 companies with highest profit % to revenue is computed using nlargest() and the associated company names are displayed

# Speculate what these might have in common, e.g. same industry, reside in same country, etc.
# An intersection operation is done using numpy to identify the common type of company among the Top 10 Companies with highest profits

Common_Company = np.intersect1d(df.nlargest(10,['Profits as % of Assets'])['Company'], df.nlargest(10,['Profits as % of Revenue'])['Company'])
print("Common high yiedling Companies are: ")
for Company in Common_Company:
       print(Company) 


#Sample Output:
#Common high yiedling Companies are: 
#Advanz Pharma
#Naspers


# An intersection operation is done using numpy to identify the common Country among the Top 10 Companies with highest profits
Common_Country = np.intersect1d(df.nlargest(10,['Profits as % of Assets'])['Country'], df.nlargest(10,['Profits as % of Revenue'])['Country'])
print("Common Countries are: ")
for Company in Common_Country:
       print(Company)

#Sample Output:
#Common Countries are: 
#Canada
#South Africa
#United States
