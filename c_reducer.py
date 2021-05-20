#!/usr/bin/python3


from operator import itemgetter
import sys
import numpy as np

currentCentroid = None #to store current centroid in loop
centroid = None
predictedLabelList = [] # to store predicted labels for each centroid
#combine all predicted labels of a centroids together
for line in sys.stdin:
    line = line.strip()
    if line:
        centroid, predictedLabel = line.split('\t')
        if (currentCentroid == None):
            currentCentroid = centroid
            predictedLabelList.append(predictedLabel)
        elif (centroid == currentCentroid):
            predictedLabelList.append(predictedLabel)
        else:
            if currentCentroid:
                labels = ["%s" % label for label in predictedLabelList]
                stringLabels = ','.join(labels)
                print('%s,%s' % (currentCentroid, stringLabels)) #output centroid label and its predicted labels
                #reinitialising for next cluster computation
                predictedLabelList = []
                currentCentroid = centroid
                predictedLabelList.append(predictedLabel)
if currentCentroid == centroid:
    labels = ["%s" % label for label in predictedLabelList]
    stringLabels = ','.join(labels)
    print('%s,%s' % (currentCentroid, stringLabels)) #output centroid label and its predicted labels
