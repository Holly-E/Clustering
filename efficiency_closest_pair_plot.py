#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:30:15 2018

@author: hollyerickson

Code for loading the loglog citation graph.
"""
import matplotlib.pyplot as plt
import random

#import Closest_pair_clustering as cpc
from Closest_pair_clustering import slow_closest_pair
from Closest_pair_clustering import fast_closest_pair
import alg_cluster
import timeit


def gen_random_clusters(num_clusters):
    """
    creates a list of clusters where each cluster in this list 
    corresponds to one randomly generated point in the square with corners (±1,±1).
    """
    cluster_list = [alg_cluster.Cluster(set(), random.randint(-100, 100)/100, random.randint(-100, 100)/100,0,0) for _dummy_idx in range(num_clusters)]
    return cluster_list

def run_time_efficiency(cluster_min, cluster_max, func):
    x = []
    y = []
    for num_clusters in range(cluster_min, cluster_max +1):
        cluster_list = gen_random_clusters(num_clusters)
        x.append(num_clusters)
        
        start = timeit.default_timer()
        func(cluster_list)
        stop = timeit.default_timer()
        
        y.append(stop - start)

    return (x, y)

slow = run_time_efficiency(2, 200, slow_closest_pair)
x_slow = slow[0]
y_slow = slow[1]

fast = run_time_efficiency(2, 200, fast_closest_pair)
x_fast = fast[0]
y_fast = fast[1]

plt.style.use('default')
fig = plt.figure(figsize = (9, 5))
ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(x_slow, y_slow, label = 'Slow Closest Pair') # ls='None', marker='.', ms = 6, mec='black', mew=.5, c='red')
ax1.plot(x_fast, y_fast, label = 'Fast Closest Pair')
ax1.legend(loc = 'best')
ax1.set_title('Efficiency of Closest Pair Algorithms', weight=600)
ax1.set_xlabel('Number of Clusters')
ax1.set_ylabel('Running Time in Seconds')

plt.savefig('Images/Closest Pair Efficiency Plot V2', orientation='landscape')
plt.show()

