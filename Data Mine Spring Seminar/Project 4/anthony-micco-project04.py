#Question 1
import pandas as pd
df = pd.read_csv("/anvil/projects/tdm/data/noaa/1880.csv", header=None,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
df.head()

for index, row in df.iterrows():
    if row["element_code"]=="PRCP":
        if row["value"] > 1200:
            print(row["date"])
            
print(df[(df.element_code == "PRCP") & (df.value > 1200)]["date"])


#Question 2
from pathlib import Path

myfiles=[]
for year in range (1800, 1851):
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)


for file in myfiles:
    myDF = pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    total = 0
    for index,row in myDF.iterrows():
         if row['element_code']=='PRCP':
                total += row["value"]
                
    average = total / len(myDF[myDF["element_code"]=="PRCP"])            
    print(f"Year: {file.stem} Avg. Precip: {average}")
    

year = 1800
myfiles = []

while year < 1851:
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)
    year+=1
    

index = 0
average_precip = 0
while index < len(myfiles) and average_precip < 22:
    file_path = myfiles[index]
    prec = pd.read_csv(file_path, names=["id", "date", "element_code", "value", "mflag", "qflag", "sflag", "obstime"])
    points = len(prec[prec["element_code"]=="PRCP"])
    total_precip = prec[prec["element_code"]=="PRCP"]['value'].sum()
    average_precip = total_precip / points
    
    print("Average precipitation for year {}: {}".format(file_path.stem, average_precip))

    index += 1



#Question 3
df[df["element_code"]=="PRCP"].groupby("id")["value"].mean().sort_values()

df[df["element_code"]=="PRCP"].groupby("id")["value"].mean().sort_values()["USC00288878"]


#Question 4
df[df["element_code"]=="PRCP"].groupby("id")["value"].mean().sort_values().to_dict()


#Question 5
df["element_code"].unique()

#Finding the average max temperature for the years 1800-1850
for file in myfiles:
    myDF = pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    total = 0
    for index,row in myDF.iterrows():
         if row['element_code']=='TMAX':
                total += row["value"]
                
    average = total / len(myDF[myDF["element_code"]=='TMAX'])            
    print(f"Year: {file.stem} Avg. Max Temp: {average}")
    
#Forest Data
forest = pd.read_csv("/anvil/projects/tdm/data/forest/ENTIRE_COUNTY.csv")
forest.head()
forest.columns
print(forest["COUNTYNM"].unique())
#Finding the number of entries in Franklin County
total = 0
for index,row in forest.iterrows():
         if forest['COUNTYNM'][index]=='Franklin':
                total += 1
print(f"There are {total} entries for Franklin County")