#!/usr/bin/python3

# reference:https://www.geeksforgeeks.org/python-maximum-frequency-character-in-string/


from operator import itemgetter
from collections import Counter
import sys
import numpy as np

#initialisation
count = 0 #to get count of data instances in belonging to a centroid/cluster
currentmean = 0
CurrentSum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
currentCentroid = None
centroid = None
temp = "" # to store all data labels belonging to a cluster and get the frequency from this string

#reading each line from standard input
for line in sys.stdin:
    line = line.strip() # strip any whitespaces
    if line:
        centroid, dataInstance = line.split('\t') #get centroid and data instance
        dataLabel = dataInstance.split(',', 1)[0] #gets the label from data instance
        datapointString = dataInstance.split(',', 1)[1]
        datapointStringArray = datapointString.split(',')
        datapointArray = np.array(list(map(int, datapointStringArray)))
        temp += dataLabel 
        # this 'if' runs only the first time to initialize currentCentroid ,CurrentSum and count
        if (currentCentroid == None):
            currentCentroid = centroid
            count = count+1
            CurrentSum = datapointArray
        elif (centroid == currentCentroid): # increase count and add the coordinates belonging to same cluster
            count = count+1
            CurrentSum = CurrentSum + datapointArray
        else:
            if currentCentroid:
                currentmean = CurrentSum/count  # find the average
                strings = ["%d" % number for number in currentmean]
                my_string = ','.join(strings)
                temp += currentCentroid
                c = Counter(temp)
                c = max(c, key=c.get)
                print('%s,%s' % (c, my_string))
            #reinitalize for the next cluster computations
            currentCentroid = centroid
            CurrentSum = datapointArray
            count = 1
            temp = dataLabel
if currentCentroid == centroid:
    currentmean = CurrentSum/count
    strings = ["%d" % number for number in currentmean]
    my_string = ','.join(strings)
    c = Counter(temp)
    c = max(c, key=c.get)
    print('%s,%s' % (c, my_string))
