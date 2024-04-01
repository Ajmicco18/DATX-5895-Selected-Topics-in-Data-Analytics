#Question 1
import pandas as pd 
from pathlib import Path

df1880 = pd.read_csv("/anvil/projects/tdm/data/noaa/1880.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
df1880.columns
df1880
len(df1880[df1880['id'].str.startswith('US')])

df1881 = pd.read_csv("/anvil/projects/tdm/data/noaa/1881.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])

len(df1881[df1881['id'].str.startswith('US')])

df1882 = pd.read_csv("/anvil/projects/tdm/data/noaa/1882.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
len(df1882[df1882['id'].str.startswith('US')])

df1883 = pd.read_csv("/anvil/projects/tdm/data/noaa/1882.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
len(df1883[df1883['id'].str.startswith('US')])

usDict = {'1880':48428, '1881':48196,'1882':50664,'1883':52363}
yearsList = [1880, 1881,1882,1883]

def find_us_id(myyears):
    year_dict = {}
    column_title_list=["id","date","element_code","value","mflag","qflag","sflag","obstime"]
    for year in myyears:
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        x = len(myDF[myDF['id'].str.startswith('US')])
        year_dict[year]=x

    return year_dict

find_us_id(yearsList)



#Question 2
mydescendingdict = dict([key, usDict[key]] for key in sorted(usDict, key=usDict.get, reverse=True))
mydescendingdict

def find_us_id_desc(myyears):
    year_dict = {}
    column_title_list=["id","date","element_code","value","mflag","qflag","sflag","obstime"]
    for year in myyears:
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        x = len(myDF[myDF['id'].str.startswith('US')])
        year_dict[year]=x
        
    descendingusdict=dict([key, year_dict[key]] for key in sorted(year_dict, key=year_dict.get, reverse=True))
        
    return descendingusdict

find_us_id_desc(yearsList)


#Question 3

#1880
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1880.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
len(df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)])

#1881
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1881.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
len(df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)])

#1882
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1882.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
len(df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)])

#1883
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1883.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
len(df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)])

us_snow_dict = {'1880':203, '1881':266,'1882':253,'1883':187}

def find_us_id_snow(myyears):
    year_dict = {}
    column_title_list=["id","date","element_code","value","mflag","qflag","sflag","obstime"]
    for year in myyears:
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        x = len(myDF[(myDF['id'].str.startswith('US'))&(myDF['element_code']=="SNOW")&(myDF['value']>0)])
        year_dict[year]=x
        
    return year_dict

find_us_id_snow(yearsList)


#Question 4

#1880
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1880.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].idxmax().sort_values(ascending=False)
max_snow_id = max_id.idxmax()
max_snow_id

#1881
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1881.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].idxmax().sort_values(ascending=False)
max_snow_id = max_id.idxmax()
max_snow_id

#1882
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1882.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].idxmax().sort_values(ascending=False)
max_snow_id = max_id.idxmax()
max_snow_id

#1883
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1883.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].idxmax().sort_values(ascending=False)
max_snow_id = max_id.idxmax()
max_snow_id

id_dict = {'1880':'USC00319462','1881':'USC00464045','1882':'USP00CA0002','1882':'USC00134049'}

def find_max_snow_id(myyears):
    year_dict = {}
    column_title_list=["id","date","element_code","value","mflag","qflag","sflag","obstime"]
    for year in myyears:
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        max_id = myDF[(myDF['id'].str.startswith('US'))&(myDF['element_code']=="SNOW")&(myDF['value']>0)].groupby("id")['value'].idxmax().sort_values(ascending=False)
        max_snow_id = max_id.idxmax()
        year_dict[year]=max_snow_id
        
    return year_dict

find_max_snow_id(yearsList)



#Question 5

#1880
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1880.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].sum().sort_values(ascending=False)
total_snow_id = max_id.idxmax()
total_snow_id

#1881
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1881.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].sum().sort_values(ascending=False)
total_snow_id = max_id.idxmax()
total_snow_id

#1882
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1882.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].sum().sort_values(ascending=False)
total_snow_id = max_id.idxmax()
total_snow_id

#1883
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1883.csv", 
                 header=None,
                 names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
max_id = df[(df['id'].str.startswith('US'))&(df['element_code']=="SNOW")&(df['value']>0)].groupby("id")['value'].sum().sort_values(ascending=False)
total_snow_id = max_id.idxmax()
total_snow_id

total_snow_dict = {'1880':'USC00464045', '1881':'USW00014971', '1882':'USC00176902', '1883':'USC00464045'}

def find_total_snow_id(myyears):
    year_dict = {}
    column_title_list=["id","date","element_code","value","mflag","qflag","sflag","obstime"]
    for year in myyears:
        file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
        myDF = pd.read_csv(file, header=None, names=column_title_list)
        max_id = myDF[(myDF['id'].str.startswith('US'))&(myDF['element_code']=="SNOW")&(myDF['value']>0)].groupby("id")['value'].sum().sort_values(ascending=False)
        total_snow_id = max_id.idxmax()
        year_dict[year]=total_snow_id
        
    return year_dict

find_total_snow_id(yearsList)