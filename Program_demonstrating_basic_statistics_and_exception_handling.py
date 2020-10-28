# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:10:33 2020

@author: Niall
"""

#Program demonstrating basic statistics and exception handling
from math import sqrt

supercomputers_list = []

filename = input("Enter the name of the data file: ")

try:
    #Open supercomputers
    with open(filename) as data_file:
    
    #Find the number of values
        line = 0
        for data in data_file:
            line+=1
            try:
                data = float(data)
                supercomputers_list.append(data)
            except ValueError:
                print(f"Line {line} of data file has an invalid value {data}")
            
except FileNotFoundError:
    print(f"Unable to open file {filename}")



if len(supercomputers_list) == 0:
    print("File empty")
else:
    mean = sum(supercomputers_list)/len(supercomputers_list)
    print(f"Number of supercomputers: {len(supercomputers_list)}")
    print(f"Average supercomputer performance: {(mean):.1f} Tf")
    print(f"Maximum supercomputer performance: {(max(supercomputers_list)):.1f} Tf")
    print(f"Minimum supercomputer performance: {(min(supercomputers_list)):.1f} Tf")
    
    #sort values
    supercomputers_list.sort()
    #Get the middle val index
    mid_index = int(len(supercomputers_list)/2)
    
    #Check if the lenght is odd to see if their is a middle val
    if len(supercomputers_list) % 2 == 1:
        median = supercomputers_list[mid_index]
    else:
        median = (supercomputers_list[mid_index-1] + supercomputers_list[mid_index])/2
    
    print(f"Median value is: {median:.1f} Tf")
    
    #Calc the standard dev 
    
    #Create a list of the deviations squared
    deviations = [ (x - mean) ** 2 for x in supercomputers_list]
    
    #Calculate the standard deviation
    std_dev = sqrt(sum(deviations)/(len(supercomputers_list)-1))
    print(f"Standard Deviation: {std_dev:.1f} Tf")
        
    
    #print(f"Median supercomputer performance: {(median(supercomputers_list)):.1f} Tf")