#Question 1
mydata = [("Anthony", 21, "Computer Science"),
          ("Jason", 19, "Mathematics"),
          ("Nick", 20, "Pyschology"),
          ("Alex", 19, "Computer Science"),
          ("Carson", 20, "Business"),
          ("Nico", 21, "Marketing")]

import pandas as pd
studentDF = pd.DataFrame(data=mydata, columns=['Name', 'Age', 'Major'])
print(studentDF.head())

print(studentDF.iloc[1])


#Question 2
import pandas as pd
myDF = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")

myDF.head()
myDF.tail()


#Question 3
print(myDF.shape)
print(myDF.columns)


#Question 4
len(myDF[myDF['price'] > 6000])

myDF['state'].unique()
len(myDF[myDF['state'] == 'tx'])  
len(myDF[myDF['state'] == 'in'])

myDF['region'].unique()
len(myDF['region'].unique())


#Question 5
subsetDF = myDF[myDF['price'] < 6000]
subsetDF.shape
stateDF = subsetDF.groupby('state').size()
stateDF

import matplotlib.pyplot as plt
stateDF.plot(kind='bar', figsize=(25,10))
plt.title('Number of Car Priced < 6000 per State')
plt.xlabel('State')
plt.ylabel('Number of Cars')