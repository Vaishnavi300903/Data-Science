# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:19:43 2024

@author: Dell
"""

#Reading data in various format
import pandas as pd
df=pd.read_csv("E:/Data Science/Python/buzzers.csv.xls")

#Check for working directory
import os
with open("E:/Data Science/Python/buzzers.csv.xls") as raw_data:
    print(raw_data.read())

#Reading csv data as list
import csv
with open("E:/Data Science/Python/buzzers.csv.xls") as raw_data:
    print(raw_data.read())





























































