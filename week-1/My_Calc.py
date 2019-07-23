# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

#Initiate the class and add the attributes

class Calculator:
    def __init__(self, data):
        self.data = data
        self.update_stats()
        
    def update_stats(self):
        self.lenght = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_var()
        self.standev = self.__calc_std()
        
    def __calc_mean(self):    
        mean = sum(self.data)/len(self.data)
        return mean
    
    def __calc_median(self): 
        lenght_data = int(len(self.data)) #save the lenght 
        middle_1 = int(lenght_data/2 - 1)
        middle_2 = int(lenght_data/2)

        if lenght_data % 2 == 0: # check if the lenght is odd or even
            median = (self.data[middle_1] + self.data[middle_2])/2
        else:
            median = self.data[middle_2]
        return median
    
    def __calc_var(self):
        return sum((x-self.mean)**2 for x in self.data)/(len(self.data)-1)

    def __calc_std(self):
        return math.sqrt(self.variance)
    
    #create methods 
        
    def add_data(self, new_data):
        self.data.extend(new_data)
        self.update_stats()
        
    def remove_data(self, index):
        self.data.pop(index)
        self.update_stats()
        