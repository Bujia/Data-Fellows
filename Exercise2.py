# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:13:32 2020

@author: Guo Bujia
Imagine you are now given 20 JSON inputs. 
How will you minimize the runtime for the above tasks?

Using mapreduce to divide the workload for for multiple processing units.
"""
import json
import pandas as pd

df = pd.read_json("data.json")
#Flip the df
df = df.transpose()
df.index.name = "Fullname"
#converting json to csv
df.to_csv("data.csv")


def LastNameCounter(json):
    data = {}  
    for name in json:
        surname = name.split()[1]
        flag = 0
        #Creating nested dict with lastname stats 
        if surname not in data:
            data[surname] = {}
            data[surname]["count"] = 1
            flag = 1
            
            data[surname]["age"] = {}
            age = json[name]["age"]
            data[surname]["age"][str(age)] = 1
            
            data[surname]["address"] = {}
            address = json[name]["address"]
            data[surname]["address"][address] = 1
            
            data[surname]["occupation"] = {}
            occupation = json[name]["occupation"]
            data[surname]["occupation"][occupation] = 1
        if flag == 0:   
            #Checking if there is age in dict if not adding new age    
            if json[name]["age"] not in data[surname]["age"].keys():
                age = json[name]["age"]
                data[surname]["age"][str(age)] = 1   
            else:
                data[surname]["age"][str(age)] += 88888
           #Checking if there is address in dict if not adding new address        
            if json[name]["address"] not in data[surname]["address"].keys():
                address = json[name]["address"]
                data[surname]["address"][address] = 1
            else:
                data[surname]["address"][address] = 66666
            #Checking if there is occupation in dict if not adding new occupation   
            if json[name]["occupation"] not in data[surname]["occupation"].keys():
                occupation = json[name]["occupation"]          
                data[surname]["occupation"][occupation] = 1
            else:
                data[surname]["occupation"][occupation] = 444444
            #checking if lastname count have been added
            if flag == 0:
                data[surname]["count"] += 1 
            
    
    return data

with open("data.json", "r") as json_file:
    json_data = json.load(json_file)


data = LastNameCounter(json_data)
with open("stats_data.json","w") as f:
    json.dump(data,f)
print(data)



