#Question 1
import pandas as pd
myDF =pd.read_csv('/anvil/projects/tdm/data/noaa/2018.csv', header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
avgTemp = myDF[(myDF["date"] >= 20180101  ) & (myDF["date"]<= 20180115) & (myDF["element_code"] == "TAVG")]["value"].mean()
print(avgTemp)

def avg_aggreg_temp(file_location, column_title_list, start_date, end_date, test_element_code):
    #Define the data frame with file_location and column_title _list
    df = pd.read_csv(file_location, header=None, names=column_title_list)
    #Define average temp with the parameters of start_date, end_date and element_code
    avgTemp= df[(df['date'] >= start_date) & (df['date']<= end_date) & (df['element_code']==test_element_code)['value'].mean()
    #Return the avgTemp value
    return avgTemp

avg_aggreg_temp('/anvil/projects/tdm/data/noaa/2018.csv',["id","date","element_code","value","mflag","qflag","sflag","obstime"], 20180101,20180115,'TAVG') 


                
#Question 2
year_dict = {}
for year in range(1880,1884):
    file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myDF = pd.read_csv(file, header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    result = myDF[(myDF["element_code"] == "TAVG")]["value"].mean()
    year_dict[year]=result

print(year_dict)
                

from pathlib import Path
def avg_year_dict(years_list, column_title_list, test_element_code):
    #Define your year dictionary
    year_dict = {}
    
    #Iterate through the year list passed as a parameter
    for year in years_list:
        #Define the file you intend to use for the specific year
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        #Creates the specified dataframe
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        #Defines result and runs mean function to obtain the average
        result = myDF[(myDF["element_code"] == test_element_code)]["value"].mean()
        #Adds year and the average to the dictionary object
        year_dict[year]=result
    
    return year_dict

avg_year_dict(range(1880,1884),["id","date","element_code","value","mflag","qflag","sflag","obstime"], "TAVG") 
                
                

#Question 3
month_dict={}

for year in range(1880,1883):
    file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    df =pd.read_csv(file, header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    df["month"] = pd.to_datetime(df["date"], format ='%Y%m%d').dt.month
    result = df[(df["element_code"] == "TAVG") & (df["month"]== 2)]["value"].mean()
    month_dict[year] = result
    
print(month_dict)
                
month_dict={}

for year in range(1880,1883):
    file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    df =pd.read_csv(file, header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    df["month"] = pd.to_datetime(df["date"], format ='%Y%m%d').dt.month
    result = df[(df["element_code"] == "TAVG") & (df["month"]== 10)]["value"].mean()
    month_dict[year] = result
    
print(month_dict)
                

def avg_month_dict(years_list, month, column_title_list, test_element_code):
    #Define your year dictionary
    month_dict = {}
    
    #Iterate through the year list passed as a parameter
    for year in years_list:
        #Define the file you intend to use for the specific year
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        #Creates the specified dataframe
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        #Create the month column and extract the month data from the date column
        myDF["month"] = pd.to_datetime(df["date"], format ='%Y%m%d').dt.month
        #Defines result and runs mean function to obtain the average
        result = myDF[(myDF["element_code"] == test_element_code) & (myDF["month"]==month)]["value"].mean()
        #Adds year and the average to the dictionary object
        month_dict[month]=result
    
    return year_dict
                
avg_month_dict(range(1880,1884), 8, ["id","date","element_code","value","mflag","qflag","sflag","obstime"], "TAVG")


                
#Question 4
year_dict = {}
for year in range(1880,1884):
    file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myDF = pd.read_csv(file, header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    qflagDF = myDF[myDF["qflag"] == "X"]
    count = len(qflagDF)
    year_dict[year]=count
    print(year_dict)

Keymax = max(year_dict, key= lambda x: year_dict[x])
print(Keymax)
                
def find_max_qflag(years_list, test_qflag):
    #Define a dictionary to hold key-valuepairs
    year_dict = {}
    #iterate through list of years
    for year in years_list:
        #define the file using the Path function
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        #Define your data frame using the file from the Path function
        myDF = pd.read_csv(file, header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
        #Create a new DF called aflagdf that only contains items with the indicated qflag
        qflagDF = myDF[myDF["qflag"] == test_qflag]
        #Determine the length of the df 
        count = len(qflagDF)
        #Add the result to the year_dict dictionary
        year_dict[year]=count  
        
    #Uses a lambda to find the key which has the max value in the dictionary
    Keymax = max(year_dict, key= lambda x: year_dict[x])    
    
    return Keymax
                
find_max_qflag(range(1880,1884), "D")
find_max_qflag(range(1880,1884), "G")
find_max_qflag(range(1880,1884), "I")
find_max_qflag(range(1880,1884), "K")
find_max_qflag(range(1880,1884), "L")
find_max_qflag(range(1880,1884), "O")
find_max_qflag(range(1880,1884), "N")
find_max_qflag(range(1880,1884), "S")
find_max_qflag(range(1880,1884), "X")
                
                
                
#Question 5
def find_min_avg_temp(year_list, column_title_list):
    """
    This function finds the minimum average temperature recorded over a span of years and stores them in a dictionary with 
    the key being the year and the value being the minimum average temperature
    
    Inputs: year_list-a list of the years the user wants to recorded the minimum average temperature of
            column_title_list- a list of the columns for the df since the NOAA data doesn't define columns
    
    Output: the function returns a dictionary of year and minimum average temperature pairs
    """
    #Define a dictionary to hold key-valuepairs
    year_dict = {}
    #iterate through list of years
    for year in year_list:
        #define the file using the Path function
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        #Define your data frame using the file from the Path function
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        #Define min_value that uses the minimum function to find the minimum value in the df
        min_value = myDF[myDF["element_code"]=="TAVG"]["value"].min()
        #Add the value to the year_dict dictionary 
        year_dict[year] = min_value
    
    #return the year and the minimum average temperature
    return(year_dict)
                
find_min_avg_temp(range(1880, 1890), ["id","date","element_code","value","mflag","qflag","sflag","obstime"])
                