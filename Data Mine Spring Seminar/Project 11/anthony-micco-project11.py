#Question 1
# creating flight class
class Flight:
    
    def __init__(self,flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay):
        
        self.flight_number = flight_number
        self.origin_airport_ID = origin_airport_ID
        self.destination_airport_ID = destination_airport_ID
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_delay = departure_delay
        self.arrival_delay = arrival_delay
        
    def getArrDelay(self):
        return self.arrival_delay


#Question 2
# specifying columns
cols = [ 'DepDelay', 'ArrDelay','Flight_Number_Reporting_Airline', 'Distance','CarrierDelay', 'WeatherDelay', 
        'DepTime', 'ArrTime', 'Origin','Dest', 'AirTime']

# creating column dictionary 
col_types = {'DepDelay': 'float64','ArrDelay': 'float64','Flight_Number_Reporting_Airline':'int64',
             'Distance': 'float64','CarrierDelay': 'float64','WeatherDelay': 'float64','Dest':'object',
             'Origin':'object','DepTime': 'float64','ArrTime': 'float64','AirTime': 'float64'}

import pandas as pd
import numpy as np

#creating dataframe
mydf = pd.read_csv("/anvil/projects/tdm/data/flights/2014.csv", usecols=cols, dtype=col_types, nrows=100)

#iterating through data frame to populate list
myListOfFlights = []

for index, row in mydf.iterrows():
    myflight = Flight(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_airport_ID = row['Origin'],
        destination_airport_ID = row['Dest'],
        departure_time = row['DepTime'],
        arrival_time = row['ArrTime'],
        departure_delay = row['DepDelay'],
        arrival_delay = row['ArrDelay']
    )
    myListOfFlights.append(myflight)
    
len(myListOfFlights)


#Question 3
#defining delays dictionary
delays_dest = {}

for myflights in myListOfFlights:
    if myflights.destination_airport_ID not in delays_dest:
        delays_dest[myflights.destination_airport_ID] = []
    delays_dest[myflights.destination_airport_ID].append(myflights.getArrDelay())

delays_dest

#defining average delays dictionary
average_delays = {myairport: sum(mydelays)/len(mydelays) for myairport, mydelays in delays_dest.items()}

average_delays


#Question 4
# creating average delays function
def arr_avg_delays(myFlightList):
    #Defining the destination delay dictionary
    delays_dest = {}
    
    #Iterating though the flight list to populate delays_dictionary
    for myflights in myFlightList:
        #if the Airport ID is not already in dictionary, then add it
        if myflights.destination_airport_ID not in delays_dest:
            delays_dest[myflights.destination_airport_ID] = []
        #Adding arrvival delay to the dictionary
        delays_dest[myflights.destination_airport_ID].append(myflights.getArrDelay())
    
    #Defining the average delay dictionary and calculating the average delay for each airport
    average_delays = {myairport: sum(mydelays)/len(mydelays) for myairport, mydelays in delays_dest.items()}
    
    return average_delays  

arr_avg_delays(myListOfFlights)


#Question 5
#updating Flight class
class Flight:
    
    def __init__(self,flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay):
        
        self.flight_number = flight_number
        self.origin_airport_ID = origin_airport_ID
        self.destination_airport_ID = destination_airport_ID
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_delay = departure_delay
        self.arrival_delay = arrival_delay
        
    def getArrDelay(self):
        return self.arrival_delay
    
    def getDepDelay(self):
        return self.departure_delay
    
#recreating myListOfFlights after class update
myListOfFlights = []

for index, row in mydf.iterrows():
    myflight = Flight(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_airport_ID = row['Origin'],
        destination_airport_ID = row['Dest'],
        departure_time = row['DepTime'],
        arrival_time = row['ArrTime'],
        departure_delay = row['DepDelay'],
        arrival_delay = row['ArrDelay']
    )
    myListOfFlights.append(myflight)

#creating average delays function for origin airport
def dep_avg_delays(myFlightList):
    #Defining the destination delay dictionary
    delays_origin = {}
    
    #Iterating though the flight list to populate delays_dictionary
    for myflights in myFlightList:
        #if the Airport ID is not already in dictionary, then add it
        if myflights.origin_airport_ID not in delays_origin:
            delays_origin[myflights.origin_airport_ID] = []
        #Adding arrvival delay to the dictionary
        delays_origin[myflights.origin_airport_ID].append(myflights.getDepDelay())
    
    #Defining the average delay dictionary and calculating the average delay for each airport
    average_delays = {myairport: sum(mydelays)/len(mydelays) for myairport, mydelays in delays_origin.items()}
    
    return average_delays  

dep_avg_delays(myListOfFlights)