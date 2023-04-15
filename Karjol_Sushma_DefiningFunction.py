# Sushma Karjol

#importing required libraries
import pandas as pd
import json #used to work with JSON file and objects

#function to read csv file

Path_name = 'Neural_data.csv'  

def Read_csv(path):  
    df = pd.read_csv(filepath_or_buffer=path, header=0)
    return df  # Reading the CSV file

df = Read_csv(Path_name) #calling the function
print(df)


# function to read text file
Path_nameTxt = 'network_data.txt'

def Read_txt(path): # Reading the Text file
    df = pd.read_csv(filepath_or_buffer=path, header=0 ,sep='|')
    return df


df = Read_txt(Path_nameTxt)
print(df)

#Function to call excel File 
Path_nameXl = 'Excel_report.xlsx'

def Read_xl(path): # Reading the Excel file
    df = pd.read_excel(path,sheet_name='Sheet000',skiprows=1,header=1) #skipping unfilled rows,and reading files from the sheet where data is available
    df = df.drop(["Unnamed: 0", "Unnamed: 1"], axis=1) # Dropping unrequired columns
    df2 = pd.read_excel(path,sheet_name='financials',skiprows=24,header=0) #reading data from another worksheet
    df2 = df2.drop( df2.columns[[0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,30,31,32,36,39]], axis=1) # Dropping unrequired columns
    return df,df2


df = Read_xl(Path_nameXl)
print(df) #calling the function

#Function to call Json File

import json  
Path_nameJson = 'nested_data.json'

def Read_Json(path): # Reading the Json file
    df =pd.read_json(path,typ='frame',convert_dates=True,precise_float=False)
    return df


df = Read_Json(Path_nameJson)
print(df) #calling the  Function