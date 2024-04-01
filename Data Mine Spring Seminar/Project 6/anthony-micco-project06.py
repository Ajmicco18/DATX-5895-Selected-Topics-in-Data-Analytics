#Question 1
#imports
import pandas as pd
from pathlib import Path

#Setting the value of myyear
myyear = 1980

#Creating path variable
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"

mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]
mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()

myyear = 1984
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()

myyear = 1988
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()

def read_election_year(myyear):
    #Define the column names for the data frame
        mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]
    
    #Define the dictionary types for each data frame column
    mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}
    
    #Define the path with the myyear parameter
    electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
    
    #Create the data frame
    myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
    
    #Change the TRANSACTION_DT column to be in month-day-year format
    myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
    
    #Show the head of the dataframe
    return myDF.head()

read_election_year(1996)

#Question 2
myyear = 1980
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
len(myDF["CMTE_ID"].unique())

myyear = 1984
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
len(myDF["CMTE_ID"].unique())

myyear = 1988
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
len(myDF["CMTE_ID"].unique())

def committees_function(myyear):
    #Define the column names for the data frame
    mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]
    
    #Define the dictionary types for each data frame column
    mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}
    
    #Define the path with the myyear parameter
    electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
    
    #Create the data frame
    myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
    
    #Change the TRANSACTION_DT column to be in month-day-year format
    myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
    
    #Show the number of unique committees 
    print(f"{myyear}: {len(myDF['CMTE_ID'].unique())} unique committees")
    
committees_function(1980)
committees_function(1984)
committees_function(1988)


#Question 3
myyear = 1980
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()

myyear = 1984
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()

myyear = 1988
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()

def top_five_states(myyear):
    #Define the column names for the data frame
    mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]
    
    #Define the dictionary types for each data frame column
    mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}
    
    #Define the path with the myyear parameter
    electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
    
    #Create the data frame
    myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
    
    #Change the TRANSACTION_DT column to be in month-day-year format
    myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
    
    #Return the sum of transactions of the top 5 states
    return myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()

top_five_states(1980)
top_five_states(1984)
top_five_states(1988)


#Question 4
myyear = 1980
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values()

myyear = 1984
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values()

myyear = 1988
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values()

def top_employers(myyear):
    #Define the column names for the data frame
    mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]
    
    #Define the dictionary types for each data frame column
    mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}
    
    #Define the path with the myyear parameter
    electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
    
    #Create the data frame
    myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
    
    #Change the TRANSACTION_DT column to be in month-day-year format
    myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
    
    #Return the sum of transactions of the top 5 employers
    return myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values().tail()

top_employers(1980)
top_employers(1984)
top_employers(1988)


#Question 5
myyear = 1980
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
myDF.groupby('TRANSACTION_DT')["TRANSACTION_AMT"].sum().sort_values()

myyear = 1984
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
myDF.groupby('TRANSACTION_DT')["TRANSACTION_AMT"].sum().sort_values()

myyear = 1988
electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF.head()
myDF.groupby('TRANSACTION_DT')["TRANSACTION_AMT"].sum().sort_values()

def top_dates(myyear):
     #Define the column names for the data frame
    mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]
    
    #Define the dictionary types for each data frame column
    mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}
    
    #Define the path with the myyear parameter
    electPath = f"/anvil/projects/tdm/data/election/itcont{myyear}.txt"
    
    #Create the data frame
    myDF = pd.read_csv(electPath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
    
    #Change the TRANSACTION_DT column to be in month-day-year format
    myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
    
    #Return the sum of transactions of the top 5 employers
    return myDF.groupby('TRANSACTION_DT')["TRANSACTION_AMT"].sum().sort_values().tail()

top_dates(1980)
top_dates(1984)
top_dates(1988)