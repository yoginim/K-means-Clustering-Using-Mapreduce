#!/usr/bin/env python
# coding: utf-8

# In[31]:


import seaborn as sb
import string
import numpy as np
import argparse


# In[67]:


def parse_args():
    '''Parse command line arguments'''
    parser = argparse.ArgumentParser(description="Run classification evaluation")
    
    parser.add_argument('--input', nargs='?', default='predictions.txt',help='Input File path')
    parser.add_argument('--output', nargs='?', default='performance.png',help='Visualization plot name')
    
    return parser.parse_args()


# In[68]:


def get_performance(args):
    fp = open(args.input,'r')

    # Processing alphabets and preparing confusion matrix
    cm = np.zeros((26, 26))
    alphabets = string.ascii_uppercase[:26]
    alphabet_dict = dict()
    x_axis_labels = []
    y_axis_labels = []
    for i in range(26):
        x_axis_labels.append(alphabets[i])
        y_axis_labels.append(alphabets[i])
        alphabet_dict[alphabets[i]] = i

    # Filling up the confusion matrix
    for i,line in enumerate(fp):
        line_split = line.split('\n')[0].split(',')
        actual = line_split[0]
        predictions = list(line_split[1:])
        total_pred = len(predictions)

        for p in predictions:
            cm[alphabet_dict[actual]][alphabet_dict[p]] += 1.0

    fp.close()

    # Calculate accuracy with total sum of the array and trace of the array
    print('Classification Accuracy: ' + str((np.trace(cm)/np.sum(cm))*100) + '%')

    cm = np.true_divide(cm, cm.sum(axis=1, keepdims=True))
    cm[np.isnan(cm)] = 0

    # Get heatmap of the confusion matrix
    ax = sb.heatmap(cm, vmin=0, vmax=1, xticklabels=x_axis_labels, yticklabels=y_axis_labels).set_title('Confusion matrix')
    fig = ax.get_figure()
    fig.savefig(args.output)


# In[61]:


if __name__ == "__main__":
    args = parse_args()
    get_performance(args)


