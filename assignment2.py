# -*- coding: utf-8 -*-
"""22l_7510(B)_ass2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yAMY8fbOfhy8NynMnIzJOKNfs5s2Bc5y
"""

import pandas as pd
df = pd.read_csv('Iris.csv')
preprocessed_df = pd.DataFrame()

for col in df.columns:
    if col not in ['Id', 'Species']:

        data_type = type(df[col])
        total_instances = len(df)
        number_of_nulls = df[col].isnull().sum()

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        number_of_outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()

        min_value = df[col].min()
        max_value = df[col].max()

        mode = df[col].mode()[0]
        mean = df[col].mean()
        median = df[col].median()
        variance = df[col].var()
        std_dev = df[col].std()

        preprocessed_df = preprocessed_df.append({
            'Dim': col,
            'Name': col,
            'Data Type': data_type,
            'Total Instances': total_instances,
            'Number of Nulls': number_of_nulls,
            'Number of Outliers': number_of_outliers,
            'Min. Value': min_value,
            'Max. Value': max_value,
            'Mode': mode,
            'Mean': mean,
            'Median': median,
            'Variance': variance,
            'Std. Dev': std_dev
        }, ignore_index=True)

# Print the preprocessed data
print(preprocessed_df.to_string())

import pandas as pd
import numpy as np

Iris = pd.read_csv("titanic.csv")

Iris=pd.DataFrame(Iris)
#print(Iris)

print("Data type of column: ")
print(Iris["Age"].dtype)
print(Iris["SibSp"].dtype)
print(Iris["Fare"].dtype)

print("\n The total instances are: ")
print(Iris["Age"].shape[0])
print(Iris["SibSp"].shape[0])
print(Iris["Fare"].shape[0])

print("\n The total number of nulls  are: ")
print(Iris["Age"].isnull().sum())
print(Iris["SibSp"].isnull().sum())
print(Iris["Fare"].isnull().sum())


print("The outliers are: ")
col="Age"
q1=Iris[col].quantile(0.25)
q3=Iris[col].quantile(0.75)
iqr=q3-q1
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)

outlier=Iris[(Iris[col]<lower) | (Iris[col]>upper)]
lenoutlier=len(outlier)
print(lenoutlier)



print("The outliers are: ")
col="SibSp"
q1=Iris[col].quantile(0.25)
q3=Iris[col].quantile(0.75)
iqr=q3-q1
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)

outlier=Iris[(Iris[col]<lower) | (Iris[col]>upper)]
lenoutlier=len(outlier)
print(lenoutlier)


print("The outliers are: ")
col="Fare"
q1=Iris[col].quantile(0.25)
q3=Iris[col].quantile(0.75)
iqr=q3-q1
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)

outlier=Iris[(Iris[col]<lower) | (Iris[col]>upper)]
lenoutlier=len(outlier)
print(lenoutlier)



print("The min of columns are:")
print(Iris["Age"].min())
print(Iris["SibSp"].min())
print(Iris["Fare"].min())

print("The max of columns are:")
print(Iris["Age"].max())
print(Iris["SibSp"].max())
print(Iris["Fare"].max())

print("The mode of columns are:")
print(Iris["Age"].mode().values[0])
print(Iris["SibSp"].mode().values[0])
print(Iris["Fare"].mode().values[0])

print("The mean of columns are:")
print(Iris["Age"].mean())
print(Iris["SibSp"].mean())
print(Iris["Fare"].mean())


print("The median  of columns are:")
print(Iris["Age"].median())
print(Iris["SibSp"].median())
print(Iris["Fare"].median())


print("The variance  of columns are:")
print(Iris["Age"].var())
print(Iris["SibSp"].var())
print(Iris["Fare"].var())


print("The standard deviation  of columns are:")
print(Iris["Age"].std())
print(Iris["SibSp"].std())
print(Iris["Fare"].std())

import pandas as pd
import numpy as np

Iris = pd.read_csv("Housing.csv")

Iris=pd.DataFrame(Iris)
#print(Iris)

print("Data type of column: ")
print(Iris["area"].dtype)
print(Iris["price"].dtype)
print(Iris["bedrooms"].dtype)

print("\n The total instances are: ")
print(Iris["area"].shape[0])
print(Iris["price"].shape[0])
print(Iris["bedrooms"].shape[0])

print("\n The total number of nulls  are: ")
print(Iris["area"].isnull().sum())
print(Iris["price"].isnull().sum())
print(Iris["bedrooms"].isnull().sum())


print("The outliers are: ")
col="area"
q1=Iris[col].quantile(0.25)
q3=Iris[col].quantile(0.75)
iqr=q3-q1
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)

outlier=Iris[(Iris[col]<lower) | (Iris[col]>upper)]
lenoutlier=len(outlier)
print(lenoutlier)



print("The outliers are: ")
col="price"
q1=Iris[col].quantile(0.25)
q3=Iris[col].quantile(0.75)
iqr=q3-q1
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)

outlier=Iris[(Iris[col]<lower) | (Iris[col]>upper)]
lenoutlier=len(outlier)
print(lenoutlier)


print("The outliers are: ")
col="bedrooms"
q1=Iris[col].quantile(0.25)
q3=Iris[col].quantile(0.75)
iqr=q3-q1
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)

outlier=Iris[(Iris[col]<lower) | (Iris[col]>upper)]
lenoutlier=len(outlier)
print(lenoutlier)



print("The min of columns are:")
print(Iris["area"].min())
print(Iris["price"].min())
print(Iris["bedrooms"].min())

print("The max of columns are:")
print(Iris["area"].max())
print(Iris["price"].max())
print(Iris["bedrooms"].max())

print("The mode of columns are:")
print(Iris["area"].mode().values[0])
print(Iris["price"].mode().values[0])
print(Iris["bedrooms"].mode().values[0])

print("The mean of columns are:")
print(Iris["area"].mean())
print(Iris["price"].mean())
print(Iris["bedrooms"].mean())


print("The median  of columns are:")
print(Iris["area"].median())
print(Iris["price"].median())
print(Iris["bedrooms"].median())


print("The variance  of columns are:")
print(Iris["area"].var())
print(Iris["price"].var())
print(Iris["bedrooms"].var())


print("The variance  of columns are:")
print(Iris["area"].std())
print(Iris["price"].std())
print(Iris["bedrooms"].std())

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df = pd.read_csv('Iris.csv')

# Plot the histogram
sns.histplot(df['SepalLengthCm'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Count')
plt.title('Histogram of Iris Sepal Length')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df = pd.read_csv('Iris.csv')

# Create a box plot
sns.boxplot(x='Species', y='SepalLengthCm', showmeans=True, data=df)
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.title('Box Plot of Iris Sepal Length')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df = pd.read_csv('Iris.csv')

# Plot the histogram
sns.histplot(df['SepalWidthCm'])
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')
plt.title('Histogram of Iris Sepal width')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df = pd.read_csv('Iris.csv')

# Create a box plot
sns.boxplot(x='Species', y='SepalWidthCm', showmeans=True, data=df)
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')
plt.title('Box Plot of Iris Sepal width')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Plot the histogram
sns.histplot(df['Age'])
plt.xlabel('Age (years)')
plt.ylabel('Count')
plt.title('Histogram of Titanic Age')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Create a box plot
sns.boxplot(x='Sex', y='Age', showmeans=True, data=df)
plt.xlabel('Sex')
plt.ylabel('Age (years)')
plt.title('Box Plot of Titanic Age')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Plot the histogram
sns.histplot(df['SibSp'])
plt.xlabel('Number of siblings/spouses aboard')
plt.ylabel('Count')
plt.title('Histogram of Titanic SibSp')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Create a box plot
sns.boxplot(x='Sex', y='SibSp', showmeans=True, data=df)
plt.xlabel('Sex')
plt.ylabel('Number of siblings/spouses aboard')
plt.title('Box Plot of Titanic SibSp')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Plot the histogram
sns.histplot(df['Fare'])
plt.xlabel('Fare (£)')
plt.ylabel('Count')
plt.title('Histogram of Titanic Fare')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Create a box plot
sns.boxplot(x='Sex', y='Fare', showmeans=True, data=df)
plt.xlabel('Sex')
plt.ylabel('Fare (£)')
plt.title('Box Plot of Titanic Fare')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the housing prices dataset
df = pd.read_csv('Housing.csv')

# Plot the histogram
sns.histplot(df['area'])
plt.xlabel('Area (sq ft)')
plt.ylabel('Count')
plt.title('Histogram of Housing Prices Area')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the housing prices dataset
df = pd.read_csv('Housing.csv')

# Create a box plot
sns.boxplot( y='area', showmeans=True, data=df)
plt.xlabel('frequency')
plt.ylabel('Area (sq ft)')
plt.title('Box Plot of Housing Prices Area')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the housing prices dataset
df = pd.read_csv('Housing.csv')

# Plot the histogram
sns.histplot(df['price'])
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.title('Histogram of Housing Prices Price')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the housing prices dataset
df = pd.read_csv('Housing.csv')

# Create a box plot
sns.boxplot( y='price', showmeans=True, data=df)
plt.xlabel('frequency')
plt.ylabel('Price ($)')
plt.title('Box Plot of Housing Prices Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Housing.csv')

# Create a box plot
plt.boxplot(data['bedrooms'])
plt.title('Box Plot of Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Count')
plt.show()

# Create a histogram
plt.hist(data['bedrooms'], bins=5)
plt.title('Histogram of Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Count')
plt.show()

import numpy as np
df = pd.read_csv('Housing.csv')
df=pd.DataFrame(df)


def findoutliers(column_name):
   q1 = df[column_name].quantile(0.25)
   q3 = df[column_name].quantile(0.75)
   iqr = q3 - q1
   lower_bound = q1 - 1.5 * iqr
   upper_bound = q3 + 1.5 * iqr
   outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]
   num_outliers = len(outliers)
   return num_outliers


def display(z,column_name):
    if z!=0:
      print("\n\nThe outliers are:")
      print(z)
      x = df[column_name].mean()
      df[column_name].fillna(x, inplace=True)
      print("Outliers replaced by mean")

        else:
            print("\nNo outliers in this column")


            column_name = "area"
            z=findoutliers(column_name)
            (display(z,column_name))

            column_name = "price"
            z=findoutliers(column_name)
            (display(z,column_name))

            column_name = "bedrooms"
            z=findoutliers(column_name)
            (display(z,column_name))

import numpy as np
df = pd.read_csv('Iris.csv')

df=pd.DataFrame(df)
print("\nNull in SepalLengthCm: ")

if df["SepalLengthCm"].isnull().sum() != 0:
    x = df["SepalLengthCm"].mean()
    df['SepalLengthCm'].fillna(x, inplace=True)
    print("\nNulls in SepalLengthCm replaced by mean")
else:
  print("\nNo nulls")


print("\nNull in PetalLengthCm: ")
if df["PetalLengthCm"].isnull().sum() != 0:
    x = df["PetalLengthCm"].mean()
    df['PetalLengthCm'].fillna(x, inplace=True)
    print("\nNulls in PetalLengthCm replaced by mean")
else:
  print("\nNo nulls")

print("\nNull in SepalWidthCm: ")


if df["SepalWidthCm"].isnull().sum() != 0:
    x = df["SepalWidthCm"].mean()
    df['SepalWidthCm'].fillna(x, inplace=True)
    print("\nNulls in SepalWidthCm replaced by mean")
else:
  print("\nNo nulls")