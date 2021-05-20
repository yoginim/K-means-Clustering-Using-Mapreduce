#!/usr/bin/env python
# coding: utf-8

import random
import math
import numpy as np
import argparse
import string


def parse_args():
    '''Parse command line arguments'''
    parser = argparse.ArgumentParser(description="Run data sampling")
    
    parser.add_argument('--input', nargs='?', default='letter-recognition.data',help='Input File path')
    parser.add_argument('--output', nargs='?', default='Datasets',help='Output Directory path')
    parser.add_argument('--size', type=float, default=10,help='Training size in percentage. Default is 10')
    
    return parser.parse_args()


def sample_data(args):
    data_points = dict()

    fp = open(args.input,'r')

    for i,line in enumerate(fp):
        try:
            data_points[line[0]].append(line)
        except Exception as e:
            data_points[line[0]] = []
            data_points[line[0]].append(line)

    fp.close()


    alphabets = string.ascii_uppercase[:26]
    
    wp = open(args.output + '/centroids.txt','w')
    trp = open(args.output + '/train.txt','w')
    tep = open(args.output + '/test.txt','w')

#     split train and test dataset
    for key in data_points.keys():
#         wp.write(random.choice(data_points[key]))
        dict_length = len(data_points[key])
        to_sample = math.floor(dict_length*(args.size/100))
        rand_nums = [random.randint(0, dict_length) for i in range(to_sample)]

        # get centroid of this cluster
        wp.write(data_points[key][rand_nums[0]])

        for j,data in enumerate(data_points[key]):
            if j in rand_nums:
                trp.write(data)
            else:
                tep.write(data)

    wp.close()
    tep.close()
    trp.close()



if __name__ == "__main__":
    args = parse_args()
    sample_data(args)