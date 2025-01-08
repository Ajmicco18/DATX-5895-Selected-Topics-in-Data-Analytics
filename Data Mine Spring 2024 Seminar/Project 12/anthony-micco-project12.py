#Question 1
# imports and data frame options
import pandas as pd 
import numpy as np
pd.set_option('display.max_columns', None) 

#creating flight class
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
    
    
#creating ScheduledFlight subclass
class ScheduledFlight(Flight):
    
    def __init__(self, flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay, CRSDepTime, CRSArrTime):
        
        super().__init__(flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay)
        self.CRSDepTime = CRSDepTime
        self.CRSArrTime = CRSArrTime
    
    def isOnTime(self):
        if super().getArrDelay() <= 0 and super().getDepDelay() <= 0:
            return True
        else:
            return False


        
#Question 2
# columns to read in 
cols = [
    'DepDelay', 'ArrDelay', 'Flight_Number_Reporting_Airline', 'Distance',
    'CarrierDelay', 'WeatherDelay', 'CRSDepTime', 'CRSArrTime',
    'DepTime', 'ArrTime', 'Origin',
    'Dest', 'AirTime'
]

# column data types
col_types = {'DepDelay': 'float64','ArrDelay': 'float64','Flight_Number_Reporting_Airline':'int64',
             'Distance': 'float64','CarrierDelay': 'float64','WeatherDelay': 'float64', 'CRSDepTime': 'float64',
             'CRSArrTime':'float64','Dest':'object','Origin':'object','DepTime': 'float64',
             'ArrTime': 'float64','AirTime': 'float64'}

# creating mydf
mydf = pd.read_csv('/anvil/projects/tdm/data/flights/2014.csv', usecols=cols, dtype=col_types, nrows=100)
mydf.head()

# initating list of flights
flightList = []

for index, row in mydf.iterrows():
    myflight = ScheduledFlight(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_airport_ID = row['Origin'],
        destination_airport_ID = row['Dest'],
        departure_time = row['DepTime'],
        arrival_time = row['ArrTime'],
        departure_delay = row['DepDelay'],
        arrival_delay = row['ArrDelay'],
        CRSDepTime = row['CRSDepTime'],
        CRSArrTime = row['CRSArrTime']
    )

    flightList.append(myflight)

len(flightList)



#Question 3
# creating ontime_count dictionary
ontime_count = {}

for myflights in flightList:
    if myflights.destination_airport_ID not in ontime_count:
        ontime_count[myflights.destination_airport_ID] = []
    
    if(myflights.isOnTime()):
        ontime_count[myflights.destination_airport_ID].append(myflights.isOnTime())
        
ontime_count

# Calculating the amount of flights on time
ontimeCount = {myairport : sum(isontime) for myairport, isontime in ontime_count.items()}
ontimeCount



#Question 4
# updated class
class ScheduledFlight(Flight):
    
    def __init__(self, flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay, CRSDepTime, CRSArrTime):
        
        super().__init__(flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay)
        self.CRSDepTime = CRSDepTime
        self.CRSArrTime = CRSArrTime
    
    def isOnTime(self):
        if super().getArrDelay() <= 0 and super().getDepDelay() <= 0:
            return True
        else:
            return False
        
    def isDelayed(self):
        if super().getArrDelay() > 0 and super().getDepDelay() > 0:
            return True
        else:
            return False

# reinitating list of flights after update
flightList = []

for index, row in mydf.iterrows():
    myflight = ScheduledFlight(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_airport_ID = row['Origin'],
        destination_airport_ID = row['Dest'],
        departure_time = row['DepTime'],
        arrival_time = row['ArrTime'],
        departure_delay = row['DepDelay'],
        arrival_delay = row['ArrDelay'],
        CRSDepTime = row['CRSDepTime'],
        CRSArrTime = row['CRSArrTime']
    )

    flightList.append(myflight)
    
# creating delayed_count dictionary
delayed_count = {}

for myflights in flightList:
    if myflights.destination_airport_ID not in delayed_count:
        delayed_count[myflights.destination_airport_ID] = []
    
    if(myflights.isDelayed()):
        delayed_count[myflights.destination_airport_ID].append(myflights.isDelayed())
        
# Calculating the amount of flights delayed
delayedCount = {myairport : sum(isdelayed) for myairport, isdelayed in delayed_count.items()}
delayedCount



#Question 5
#df to determine what values I want to use
testdf = pd.read_csv('/anvil/projects/tdm/data/flights/2014.csv', nrows=100)
testdf.head()

# defining my own subclass
class FlightLength(Flight):
    
    def __init__(self,flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay, elasped_time):
            super().__init__(flight_number, origin_airport_ID, destination_airport_ID, departure_time, arrival_time, departure_delay, arrival_delay)
            self.elapsed_time = elasped_time
                             
    def getElapsedTime(self):
        return self.elapsed_time 
    
# columns to read in
cols = [
    'DepDelay', 'ArrDelay', 'Flight_Number_Reporting_Airline', 'Distance',
    'CarrierDelay', 'WeatherDelay', 'ActualElapsedTime',
    'DepTime', 'ArrTime', 'Origin',
    'Dest', 'AirTime'
]

# column data types
col_types = {'DepDelay': 'float64','ArrDelay': 'float64','Flight_Number_Reporting_Airline':'int64',
             'Distance': 'float64','CarrierDelay': 'float64','WeatherDelay': 'float64',
             'ActualElapsedTime':'float64','Dest':'object','Origin':'object','DepTime': 'float64',
             'ArrTime': 'float64','AirTime': 'float64'}

# creating elapsed time df
elapsedDF = pd.read_csv('/anvil/projects/tdm/data/flights/2014.csv', usecols= cols, dtype=col_types, nrows=100)
elapsedDF.head()

#Creating list of flights
flightList = []

for index, row in elapsedDF.iterrows():
    myflight = FlightLength(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_airport_ID = row['Origin'],
        destination_airport_ID = row['Dest'],
        departure_time = row['DepTime'],
        arrival_time = row['ArrTime'],
        departure_delay = row['DepDelay'],
        arrival_delay = row['ArrDelay'],
        elasped_time = row['ActualElapsedTime']
    )
    
    flightList.append(myflight)
    
# Creating clapsed time count dictionary
elapsed_count = {}

for myflights in flightList:
    if myflights.destination_airport_ID not in elapsed_count:
        elapsed_count[myflights.destination_airport_ID] = []
    
    elapsed_count[myflights.destination_airport_ID].append(myflights.getElapsedTime())

elapsed_count

# finding the average elapsed time for each airport destination
average_elapsed_time = {myairport: sum(elapsedtime)/len(elapsedtime) for myairport,elapsedtime in elapsed_count.items()}
average_elapsed_time