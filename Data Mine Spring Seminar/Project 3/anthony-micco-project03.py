#Question 1
import pandas as pd
from pathlib import Path
# finding out how many years are in dataset
year_files = []

for file in Path(f'/anvil/projects/tdm/data/noaa').iterdir():
    if file.is_file():
        year_files.append(file)

print(len(year_files))
print(year_files)

random_year = pd.read_csv(f"/anvil/projects/tdm/data/noaa/1900.csv")
print(random_year.head)

myfiles = [file for file in Path(f"/anvil/projects/tdm/data/noaa").iterdir() for year in range(1880,1884) if file==Path(f"/anvil/projects/tdm/data/noaa/{year}.csv")]
print(myfiles)


#Question 2
file = Path('/anvil/projects/tdm/data/noaa/1880.csv')
with open(file,"r") as f:
    mycount = 0
    for line in f:
        mycount += 1
print(f'There are {mycount} records in the file called {file}')

mycount = 0
for year in range(1880,1884):
    file = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    with open(file,"r") as f:
        for line in f:
            mycount += 1
   
print(f'There are {mycount} records in the 4 files altogether') 


#Question 3
myDF = pd.read_csv(myfiles[0])
myDF.columns
myDF.head
myDF.tail

myDF = pd.read_csv(myfiles[0],header=None)
myDF.columns
pd.read_csv(myfiles[0],names = ["id","date","element_code","value","mflag","qflag","sflag","obstime"])
mydataframes = []
for i in range(0,4):
    mydataframes.append(pd.read_csv(myfiles[i],names = ["id","date","element_code","value","mflag","qflag","sflag","obstime"]))
mydataframes[0].shape
mydataframes[1].shape
mydataframes[2].shape
mydataframes[3].shape
for i in range(0,4):
    print(mydataframes[i].columns)


#Question 4
for i in range(0,4):
    print(mydataframes[i]["element_code"].unique())

for myDF in mydataframes:
    print(myDF["element_code"].value_counts()["SNOW"])


#Question 5
myfiles=[]
for year in range (1880, 1884):
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)
    
count = 0
for file in myfiles:
    for myDF in pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"],chunksize =10000):
        count += len(myDF[myDF['element_code'] == 'SNOW'])

print(count)

count = 0
for file in myfiles:
    for myDF in pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"],chunksize =10000):
        for index, row in myDF.iterrows():
            if row['element_code'] == 'SNOW':
                count += 1

print(count)