#Question 1
import pandas as pd
import numpy as np

pd.set_option('display.max_columns',None)

cols = [
    'DepDelay', 'ArrDelay', 'Distance',
    'CarrierDelay', 'WeatherDelay',
    'DepTime', 'ArrTime', 'Diverted', 'AirTime'
]

col_types = {
    'DepDelay': 'float64',
    'ArrDelay': 'float64',
    'Distance': 'float64',
    'CarrierDelay': 'float64',
    'WeatherDelay': 'float64',
    'DepTime': 'float64',
    'ArrTime': 'float64',
    'Diverted': 'int64',
    'AirTime': 'float64'
}

df = pd.read_csv("/anvil/projects/tdm/data/flights/2014.csv", usecols=cols, dtype=col_types)
df.head()



#Question 2
# creating a mydelays numpy array
mydelays = df["DepDelay"].to_numpy()

print(f"The shape of mydelays is: {mydelays.shape}")
print(f"The data type in mydelays is: {mydelays.dtype}")

mydelaysClean = np.nan_to_num(mydelays, nan=0)
mydelaysClean.mean()

mydelaysPlus = np.nan_to_num(mydelays,nan=0)
for i in range(0,len(mydelaysPlus)):
    mydelaysPlus[i] +=15

mydelaysPlus.mean()

print(f"The average delayed departure time is: {mydelaysClean.mean()}")
print(f"The average delayed departure time after adding 15 minutes is: {mydelaysPlus.mean()}")



#Question 3
# creating arrival delay array
myarrival = df["ArrDelay"].to_numpy()
myarrivalClean = np.nan_to_num(myarrival,nan=0)
print(f"The maximum arrival delay is: {myarrivalClean.max()} minutes")
print(f"The minimum arrival delay is: {myarrivalClean.min()} minutes")



#Question 4
import time

# creating the delayed flights data frame and performing calculations
start_time = time.time()

delayed_flights = df[(df['DepDelay'] > 60) | (df['ArrDelay'] > 60)]

averageDistance = delayed_flights["Distance"].mean()

print(f"The average distance for the flights is: {averageDistance}") 

end_time = time.time()
print(f"Used time is {end_time - start_time}")



#Question 5
import time

start_time = time.time()

#Creating three arrays 
depDelays = df["DepDelay"].to_numpy()
arrDelays = df["ArrDelay"].to_numpy()
distArray = df["Distance"].to_numpy()

#Filtering the array by departure and arrival delays
filteredDistArry = distArray[(depDelays > 60) | (arrDelays > 60)]

#Finding the mean
averageDelayDist = filteredDistArry.mean()

#Printing the output
print(f"The average distance for the flights is: {averageDelayDist}") 

end_time = time.time()
print(f"Used time is {end_time - start_time}")