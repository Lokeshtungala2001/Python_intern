# Using the Pandas library, load a CSV file and perform basic data analysis tasks, such as calculating the average of a selected column.
# Additionally, use Matplotlib to create visualizations, including bar charts, scatter plots, and heatmaps, to analyze the data.
# Provide insights and observations based on the analysis and visualizations.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/USER/OneDrive/Documents/data.csv',sep='\t')

# Display First 5 records
print('First 5 rows of data:')
print(df.head())

#Basic information of data
print('\nData Information:')
print(df.info())

#Display Top 2 records
print('\nTop 2 Records:')
print(df.tail(2))

#Display stats-related information
print('\nstatistical information')
print(df.describe())

#Calculate average of price
average=df['Price'].mean()
print('\nAverage Price:',average)


#Create Bar Chart
# plt.figure(figsize=(10, 4))
# plt.subplot(1, 2, 1) # this lines code is used to display two charts at a time

df['Price'].head(8).plot(kind='bar',color='green')
plt.title('Bar Chart of Prices')
plt.xlabel('Index')
plt.ylabel('Price')
# plt.show()


#Create scatter plot
# plt.subplot(1, 2, 2) # this lines code is used to display two charts at a time

x=df['Size']
y=df['Price']
plt.scatter(x,y,color='skyblue')
plt.title('Scatter Plot : Size and Price')
plt.xlabel('Size')
plt.ylabel('Price')

# plt.tight_layout() # this lines code is used to display two charts at a time
# plt.show()


#create a Heatmap
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='coolwarm')
plt.title('Heatmaps of Correlations')
# plt.show()


#Observations
print('\nObservations:')
print('-Average Price of house is around :',round(average,2))
print('-Scatter plot shows how size affects price.')
print('-Heatmaps shows which columns are strongly related.')

plt.show()
