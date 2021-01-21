import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

df=pd.read_csv('E:/data/data science/data course/DATASET/googleplaystore3-1.csv',na_values='#')
#'''
df.describe(include="all")#Similar to summary in R
df.dtypes#similar to str function in R
df.head(3)#take the head of the dataframe (first three lines)
df.tail(3)#Gives the last 3 rows
df.shape#this gives you the dimension of the dataframe(like dim in R)
df.columns#This gives you the column names


df.isna()#Gives a matrix of true and false:true means the point is not availabe
df['Reviews']#This gives you the Reviews column
df.iloc[:,4]#Another way to get the Reviews column if you know the column number
df.loc[:,'Reviews']#Another way to get the column
df1=df.loc[:,['Rating','Reviews']]#Make a new dataframe with Rating and Reviews variables 
df1=df.iloc[:,[3,4]]#Same as above
df['Reviews'].isna()#Find the missing values in Reviews (a vector of True and False values)
sum(df['Reviews'].isna())#the # of missing values
#sum(Reviews.notna())
df['Type'].unique()#find the levels of variable Type

df.index[df['Reviews'].isna()]#Find the Reviews missing values
np.where(df['Reviews'].isna())
df.index[df['Rating']>4.9]#Find the rows with Ratings larger than 4.9
sum(df['Rating']>4.9)#Find the number of these Ratings
np.mean(df['Rating'].iloc[df.index[df['Rating']>4.9]])
np.mean(df['Reviews'].loc[df['Rating']==1])
np.std(df['Reviews'].loc[df['Rating']==1])
np.sum(df['Rating']==5)
Reviews=df.loc[df['Rating']>4.9,'Reviews']#Find the Reviews for apps with Rating larger than 4.9
#Find the number of available observations

Reviews_lowrate=df.loc[df['Rating']<3.5,'Reviews']#Find the Reveiews for Ratings less than 3.5
type(df)

df1=df.iloc[:,[3,4]]
df1.agg(np.mean,axis=0)#.agg(fun,axis) applies a function to rows or columns of a dataframe.Compute the mean of each variable (each column) 
df1.agg(np.sum,axis=1)#Computes the summation of Rating and Reviews for each row. axis=1 means than apply the function on each row (move columnwise)
df1.agg(['sum','min','max'])#Applies two functions on both variables 
df.agg({'Reviews':['sum','min'],'Rating':['mean','max']})#Applies various functions on different columns

df['Last.Updated']=df['Last.Updated'].agg(pd.Timestamp)#Change the Last.Updated column to dates 
df['Last.Updated'][0]-df['Last.Updated'][1]#Compute the differencesin days and hours
 #Get the date
df.loc[0,'Last.Updated'].day#Get the day
df.loc[0,'Last.Updated'].day_name()
df.loc[0,'Last.Updated'].dayofweek
df.loc[0,'Last.Updated'].month_name()
up=df.loc[0,'Last.Updated'].now()-df.loc[0,'Last.Updated']#Get the difference between today and and the first value in Last.Updated
up.days#Get the difference in days
'Write a function in python'
def interval(x):#This function computes the days from the last time the app was updated
    #x is the date taken from Last.Updated variable, like df.loc[0,'Last.Updated']
    x=pd.Timestamp(x)
    interval=(x.now()-x).days
    return(interval)
df['Updates']=df['Last.Updated'].agg(interval)#Add a column to the dateframe called "Updates"

'Group the dataframe'
df.loc[df['Type'].isna(),'Type']='Not Available'#Change the missing values to a category
np.unique(df['Type'])#Get the levels
df2=df.groupby('Type')#Group the data based on the variable Type
df2.count()
df2.agg({"Rating":['mean','std']})#Compute the mean and standard deviation of Rating for each level of variable Type
df3=df2.agg({"Rating":['mean','std'],"Reviews":['mean','std'],"Updates":['mean','std']})
df2.get_group('Free')


'Multi index dataframe'
df3.iloc[:,1]
df3.columns
df3.loc[:,('Reviews', 'std')]#Call one column using its name
df3.loc['Free',('Reviews', 'std')]#Call an element using its row and column names
df3.loc[:,[('Rating','mean'),('Reviews','std')]]


df.dropna(axis=0,inplace=True)#Delete the missing values (rows)
df4=df.unstack()#Vectorize the dataframe


df5=df.groupby('Category').agg({"Reviews":['mean'],'Rating':['mean']})#Group by categpry and compute the mean of Reviews and Rating 
df6=df5.sort_values(('Reviews','mean'),ascending=False)#sort the dataframe based on the Reviews
df6=df6.iloc[:10,:]


'plot a histogram for Rating' 
plt.hist(df['Rating'], 50, facecolor='g',edgecolor="r")

'Plot a pie chart for mean of reviews'
exp=np.zeros(10)
exp[0]=0.2
plt.pie(df6[('Reviews','mean')],labels=df6.index,explode=exp)

'Plot a viplinplot for Rating'
plt.violinplot(df['Rating'],showmedians=True)


'Plot a barchart for number of apps in a category'
df7=df.groupby('Category')#Group by app category
plt.bar(df7.count().index,df7.count().App)#A barplot for number of apps in categories
plt.xticks(np.arange(0,33),df7.count().index,rotation=90)#Rotate the text to make it vertical


'make a list of Rating for each category as a component in the list'
l=[]#Define the initial value for a list
for x in np.unique(df['Category']):#Repeat for each category
 l.append(df['Rating'].loc[df['Category']==x])#Add a component to the list l. The component is the vector of Ratings for category x 
plt.boxplot(l,notch=True)#Boxplots for Rating associated with each category
plt.xticks(np.arange(1,34),np.unique(df['Category']),rotation=90)#Add and rotate the text
plt.axhline(np.mean(df['Rating']),color='red')

plt.scatter(df['Reviews'],df['Rating'],marker="o",c="red")#Make a Scatter plot of Reviews and Rating
h=[]
for x in np.unique(df['Type']):#Repeat for each category
 h.append(df['Rating'].loc[df['Type']==x].dropna())#Add a component to the list l. The component is the vector of Ratings for category x 
plt.boxplot(h,notch=True)#Boxplots for Rating associated with each category
plt.xticks(np.arange(1,4),np.unique(df['Type']),rotation=90)#Add and rotate the text

I=[]
for x in np.unique(df['Type']):#Repeat for each category
 I.append(df['Reviews'].loc[df['Type']==x].dropna())#Add a component to the list l. The component is the vector of Ratings for category x 
plt.boxplot(I,notch=True)#Boxplots for Rreviews associated with each category
plt.xticks(np.arange(1,4),np.unique(df['Type']))#Add and rotate the text
plt.xlabel('Type')
plt.ylabel('Reviews')
#'''






