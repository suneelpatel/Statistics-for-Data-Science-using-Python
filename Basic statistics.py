#Basic Statistics, Graphs and Reports
#Taking a random sample 
import pandas as pd
#view all the names(functions) in a module on pd
dir(pd)

####################Sampling in R#############################
#Taking a random sample 
import pandas as pd

Online_Retail=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Online Retail Sales Data\\Online Retail.csv", encoding = "ISO-8859-1")
Online_Retail.shape

sample_data=Online_Retail.sample(n=1000)
sample_data.shape
print(sample_data.head())

#Regenerating same sample again

sample_data1=Online_Retail.sample(n=1000 , random_state=12 )
sample_data1.shape
print(sample_data1.head())

#####################LAB: Sampling in python#############################

#Import “Census Income Data/Income_data.csv”
Income=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Census Income Data\\Income_data.csv")
Income.shape
Income.head()
Income.tail(3)
 #Sample size 5000
Sample_income=Income.sample(n=5000)
Sample_income.shape

#####################Descriptive statistics#####################
#Import “Census Income Data/Income_data.csv”
Income=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Census Income Data\\Income_data.csv")

Income.columns.values

#Mean and Median on python
gain_mean=Income["capital-gain"].mean()
gain_mean

gain_median=Income["capital-gain"].median()
gain_median

#####################LAB: Mean and Median on python#####################

Online_Retail=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Online_Retail_Sales_Data\\Online Retail.csv", encoding = "ISO-8859-1")
Online_Retail.shape
Online_Retail.columns.values

#Mean and median of 'UnitPrice' in Online Retail data
up_mean=Online_Retail['UnitPrice'].mean()
up_mean

up_median=Online_Retail['UnitPrice'].median()
up_median

#Mean of "Quantity" in Online Retail data
Quantity_mean=Online_Retail['Quantity'].mean()
Quantity_mean

Quantity_median=Online_Retail['Quantity'].median()
Quantity_median

#####################Dispersion Measures#####################

#####################Variance and Standard deviation#####################
usa_income=Income[Income["native-country"]==' United-States']
usa_income.shape

other_income=Income[Income["native-country"]!=' United-States']
other_income.shape

#Var and SD for USA
var_usa=usa_income["education-num"].var()
var_usa

std_usa=usa_income["education-num"].std()
std_usa

var_other=other_income["education-num"].var()
var_other

std_other=other_income["education-num"].std()
std_other 

#####################LAB: Variance and Standard deviation#####################
##var and sd UnitPrice
var_UnitPrice=Online_Retail['UnitPrice'].var()
var_UnitPrice

std_UnitPrice=Online_Retail['UnitPrice'].std()
std_UnitPrice 

#variance and sd of Quantity
var_UnitPrice=Online_Retail['Quantity'].var()
var_UnitPrice

std_UnitPrice=Online_Retail['Quantity'].std()
std_UnitPrice 

######################Percentiles & Quartiles #####################

Income["capital-gain"].describe()

#Finding the percentile & quantile by using .quantile()
Income['capital-gain'].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
Income['capital-loss'].quantile([0, 0.1, 0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
Income['hours-per-week'].quantile([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.98,1])

######################LAB: Percentiles & quartiles in python######################
bank=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Bank Tele Marketing\\bank_market.csv",encoding = "ISO-8859-1")
bank.shape

#Get the summary of the balance variable
#we can find the summary of the balance variable by using .describe()
summary_bala=bank["balance"].describe()
summary_bala

#Get relevant percentiles and see their distribution.
bank['balance'].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

#Get the summary of the age variable
summary_age=bank['age'].describe()
summary_age

#Get relevant percentiles and see their distribution
bank['age'].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

######################LAB: Box plots and outlier detection######################
#Do you suspect any outliers in balance
bank=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Bank Tele Marketing\\bank_market.csv",encoding = "ISO-8859-1")
bank.shape

import matplotlib.pyplot as plt

#Basic plot of boxplot by importing the matplot.pyplot as plt ("plt.boxplot())
plt.boxplot(bank.balance)

#Get relevant percentiles and see their distribution
bank['balance'].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,0.95, 1])
#Do you suspect any outliers in balance
# outlier are present in balance variable

#Do you suspect any outliers in age
#detect the ouliers in age variable by plt.boxplot()
plt.boxplot(bank.age)
#No outliers are present
#Get relevant percentiles and see their distribution
bank['age'].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95,1])
#Do you suspect any outliers in age
#outliers are not present in age variable


######################Creating Graphs ################################

##Scatter Plot:

cars=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Cars Data\\Cars.csv",encoding = "ISO-8859-1")
cars.shape
cars.columns.values

cars['Horsepower'].describe()
cars['MPG_City'].describe()

import matplotlib.pyplot as plt
plt.scatter(cars.Horsepower,cars.MPG_City)


######################LAB:Creating Graphs ################################

import matplotlib.pyplot as plt


#Sports data
sports_data=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Sporting_goods_sales\\Sporting_goods_sales.csv")
sports_data.head(10)

#Draw a scatter plot between Average_Income and Sales. Is there any relation between two variables
plt.scatter(sports_data.Average_Income,sports_data.Sales)

import numpy as np
np.corrcoef(sports_data.Average_Income,sports_data.Sales)

#Draw a scatter plot between Under35_Population_pect and Sales. Is there any relation between two
plt.scatter(sports_data.Under35_Population_pect,sports_data.Sales,color="red")
np.corrcoef(sports_data.Under35_Population_pect,sports_data.Sales)

######################Bar Chart######################
#Bar charts used to summarize the categorical variables

import pandas as pd

cars=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Cars Data\\Cars.csv",encoding = "ISO-8859-1")
cars.shape
cars.columns.values

freq=cars.Cylinders.value_counts()
freq.values
freq.index

import matplotlib.pyplot as plt
plt.bar(freq.index,freq.values)
######################LAB: Bar Chart######################

freq=sports_data.Avg_family_size.value_counts()
freq.values
freq.index

import matplotlib.pyplot as plt
plt.bar(freq.index,freq.values)
plt.bar(freq.index,freq.values, align="center")
plt.bar(freq.index,freq.values, align="center",tick_label=freq.index)


######################Trend Chart######################

AirPassengers=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Air Travel Data\\Air_travel.csv", encoding = "ISO-8859-1")
AirPassengers.head()
AirPassengers.dtypes
AirPassengers.columns.values

import matplotlib.pyplot as plt
plt.plot(AirPassengers.AIR)


#X axis lable
#Format the date to DD-MM-YYYY before importing 
AirPassengers['new_time']=pd.to_datetime(AirPassengers['DATE'],format='%d-%m-%Y')
plt.plot(AirPassengers.new_time,AirPassengers.AIR)

# Any single array will give time series plot
plt.plot(sports_data.Avg_family_size)
#Formatted col


################################
## Used defined Functions

def mydistance(x1=1,y1=1,x2=1,y2=1):
    import math
    dist=math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
    print(dist)
    return;
   
mydistance(x1=0,y1=0,x2=2,y2=2)
mydistance(x1=1,y1=0,x2=0,y2=1)
mydistance(x1=4,y1=6,x2=1,y2=2)
mydistance(4,6,1,2)

##The Absolute percentage difference 

x=1
y=1

def abspe(x=1,y=1):
    abpe=abs((x-y)/y)    
    print(abpe)
    return;
   
abspe(x=5,y=9)
abspe(10,100)

###Sum of squares functions

def sumsquares(*inputnums):  
     s = 0  
     for n in inputnums:  
           s =s + pow(n,2)
           print(s)
     return s;
     

sumsquares (1,1,1,1,1)  
sumsquares (1,2,5,8,-1)  

###Function for summary
import pandas as pd
column_names = ["Name","Mean", "Median", "Variance","S.D", "p5", 
"p10", "p20", "p25", "p30", "p50", "p75", "p80", "p90", "p95", "p97", "p99"]
summary_df=pd.DataFrame(columns=column_names)

def allsummary(df):  
    i=1
    for f in df.columns.values:
        summary_df.set_value(i,"Name",f)
        summary_df.set_value(i, "Mean",df[f].mean())
        summary_df.set_value(i, "Median",df[f].median())
        summary_df.set_value(i, "Variance",df[f].var())
        summary_df.set_value(i, "S.D",df[f].std())
        summary_df.set_value(i, "p5",pd.notnull(df[f]).quantile(0.1))
        summary_df.set_value(i, "p10",df[f].dropna(axis=0).quantile(0.1))
        summary_df.set_value(i, "p20",df[f].dropna(axis=0).quantile(0.2))
        summary_df.set_value(i, "p25",df[f].dropna(axis=0).quantile(0.25))
        summary_df.set_value(i, "p30",df[f].dropna(axis=0).quantile(0.3))
        summary_df.set_value(i, "p50",df[f].dropna(axis=0).quantile(0.5))
        summary_df.set_value(i, "p75",df[f].dropna(axis=0).quantile(0.75))
        summary_df.set_value(i, "p80",df[f].dropna(axis=0).quantile(0.8))
        summary_df.set_value(i, "p90",df[f].dropna(axis=0).quantile(0.9))
        summary_df.set_value(i, "p95",df[f].dropna(axis=0).quantile(0.95))
        summary_df.set_value(i, "p97",df[f].dropna(axis=0).quantile(0.97))
        summary_df.set_value(i, "p99",df[f].dropna(axis=0).quantile(0.99))
        i=i+1;
    print(summary_df)
    
credit_risk=pd.read_csv("E:\\Larning\\hadoop\\Data Science\\001_Python\\Class Files Python\\Class Files Python\\1.Python Programming\\3.Basic Statistics and Reporting in Python\\datasets\\Give me some Credit\\cs-training.csv", encoding = "ISO-8859-1")

allsummary(credit_risk)   

###How dropna(axis=0) works
###dropna expects a dataframe as input.
### Axis=1 drops coloumns with NA values
### Axis=0 drops rows with NA values

import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), columns=['one', 'two', 'three'])
df1=df.reindex([0,1,2,3,4,5,6,7])
df1["colfour"]=4

print(df1)

df1[["one","colfour"]]
df1[["one","colfour"]].dropna(axis=0) 

df1[["one","colfour"]]
df1[["one","colfour"]].dropna(axis=1) 