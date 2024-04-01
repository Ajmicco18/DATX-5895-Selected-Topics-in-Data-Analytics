#Question 1
import pandas as pd
pd.options.mode.copy_on_write = True 
pd.set_option('display.max_columns',None)

df = pd.read_csv("/anvil/projects/tdm/data/whin/weather.csv")
df.head()
df.shape

#Number of records using value counts
df["station_id"].value_counts()

#Number of records using group by
df.groupby("station_id").size()


#Question 2

#Determining the number of null values in each column
df.isna().sum()

#Determining the total number of null values
df.isna().sum().sum()

#Dropping the null values and creating a new df
df_cleaned = df.dropna()
df_cleaned.head()
df_cleaned.isna().sum()
df_cleaned.shape


#Question 3

#Creating df with no null temp values
tempDF = df.dropna(subset=["temperature"])
tempDF.head()

#combining the lat and long columns
tempDF["location"] = df["latitude"].astype(str) + ", " + df["longitude"].astype(str)
tempDF[["location"]]

#Grouping the data by location and finding average temp
tempDF.groupby("location")["temperature"].mean().sort_values()


#Question 4

# creating a function to question 3 work
def drop_null_find_avg_temp(dataframe):
    
    #Creating a new df and dropping the null temperature values
    tmpDF =  dataframe.dropna(subset=["temperature"])
    
    #Creating a new location column by combining lat and long columns
    tmpDF["location"] = dataframe["latitude"].astype(str) + ", " + dataframe["longitude"].astype(str)
    
    #Return the average temperature at each location
    return tmpDF.groupby("location")["temperature"].mean().sort_values()

drop_null_find_avg_temp(df)

#Question 5

#Creating df with no null wind gust speed values
windDF =  df.dropna(subset=["wind_gust_speed_mph"])
windDF.head()

#combining the lat and long columns
windDF["location"] = df["latitude"].astype(str) + ", " + df["longitude"].astype(str)
windDF[["location"]]

#Grouping the data by location and finding average wind gust speed 
windDF.groupby("location")["wind_gust_speed_mph"].mean().sort_values()

#Creating function for dropping null values and finding average wind gust speed
def drop_null_find_avg_wind_gust(dataframe):
    
    #Creating a new df and dropping the null wind gust speed values
    tmp_windDF =  dataframe.dropna(subset=["wind_gust_speed_mph"])
    
    #Creating a new location column by combining lat and long columns
    tmp_windDF["location"] = dataframe["latitude"].astype(str) + ", " + dataframe["longitude"].astype(str)
    
    #Return the average wind gust speed at each location
    return tmp_windDF.groupby("location")["wind_gust_speed_mph"].mean().sort_values()

drop_null_find_avg_wind_gust(df)
    