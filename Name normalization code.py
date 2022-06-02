# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
import csv
### notnames is the list of names that needs to be cleansed.
notnames = pd.read_excel('Names2.xlsx')
yesnormalized = pd.read_excel('Names3.xlsx')
### converted to list because fuzzy was having trouble pulling data
notnames = list(notnames.Unfiltered_Names)
yesnormalized = list(yesnormalized.Normalizednames)

def match_names(notnames, yesnormalized, min_score=0):
    max_score = -1
    max_name = ''
    for x in yesnormalized:
        score = fuzz.ratio(notnames, x)
        if (score > min_score) & (score > max_score):
            max_name = x
            max_score = score
    return (max_name, max_score)
###used 75% score to test. This will be updated once I run the notnames list in cleanco to get rid of common terms
names = []
for x in notnames:
    match = match_names(x, yesnormalized, 75)
    if match[1] >= 75:
        notnames = ('(' + str(x), str(match[0]) + ')')
        names.append(notnames)
name_dict = dict(names)
print name_dict




