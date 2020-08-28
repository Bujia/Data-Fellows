# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:13:32 2020

@author: Guo Bujia
Imagine you are now given 20 JSON inputs. 
How will you minimize the runtime for the above tasks?

Using mapreduce to divide the workload for for multiple processing units.
Use different threads for each file and combine the result
"""
import json
import pandas as pd
def part_one():
    df = pd.read_json("data.json")
    #Flip the df
    df = df.transpose()
    df.index.name = "Fullname"
    #converting json to csv
    df.to_csv("data.csv")


def LastNameCounter(json):
    data = {}  
    for name, value in json.items():
        surname = name.split()[1]
        #Creating nested dict with lastname stats 
        if surname not in data:
            data[surname] = {
                    "count": 1,
                    "age": {str(value["age"]): 1},
                    "address": {value["address"]: 1},
                    "occupation": {value["occupation"]: 1}
                }
        else:
            data[surname]["count"] += 1
            for key in ["age", "address", "occupation"]:
                tmp = str(value[key])
                if tmp in data[surname][key]:
                    data[surname][key][tmp] += 1
                else:
                    data[surname][key][tmp] = 1 
    return data

def main():
    part_one()
    with open("data.json", "r") as json_file:
        json_data = json.load(json_file)  
    
    data = LastNameCounter(json_data)
    
    json_object = json.dumps(data, indent = 3)
    with open("myjson.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
   main()
