#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:46:58 2018

@author: hollyerickson

Closest Pair & Clustering Functions:
    slow_closest_pair(cluster_list)
    fast_closest_pair(cluster_list)
    closest_pair_strip(cluster_list, horiz_center, half_width)
    hierarchical_clustering(cluster_list, num_clusters)
    kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import alg_cluster
import math
 

TEST_CASE= [alg_cluster.Cluster(set(['00']), 0.0, 0.0, 1, 0.1),

alg_cluster.Cluster(set(['10']), 1.0, 0.0, 2, 0.1),

alg_cluster.Cluster(set(['11']), 1.0, 1.0, 3, 0.1),

alg_cluster.Cluster(set(['01']), 0.0, 1.0, 4, 0.1),

alg_cluster.Cluster(set(['1010']), 10.0, 10.0, 5, 0.1),

alg_cluster.Cluster(set(['1011']), 10.0, 11.0, 6, 0.1),

alg_cluster.Cluster(set(['1111']), 11.0, 11.0, 7, 0.1),

alg_cluster.Cluster(set(['1110']), 11.0, 10.0, 8, 0.1)]


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def sort_clusters(cluster_list):
    """
    Helper function to sort on horizontal positions by ascending order
    """
    copy = list(cluster_list)
    copy.sort(key = lambda cluster: cluster.horiz_center())
    
    return copy


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    smallest_dist = (float("inf"), -1, -1)
    
    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                test_distance = pair_distance(cluster_list, idx1, idx2)
                #test_distance = cluster_list[idx1].distance(cluster_list[idx2])
                if smallest_dist[0] > test_distance[0]:
                    #smallest_dist = (test_distance, idx1, idx2)
                    smallest_dist = test_distance
  
    return (smallest_dist)



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """


    num_clusters = len(cluster_list)
    if num_clusters <= 3:
        smallest_dist = slow_closest_pair(cluster_list)
    else:
        half = int(math.floor(num_clusters/2))
        left = [cluster_list[idx] for idx in range(half)]
        right = [cluster_list[idx] for idx in range(half, num_clusters)]
        distance_left = fast_closest_pair(left)
        distance_right = fast_closest_pair(right)
        
        if distance_left[0] < distance_right[0]:
            smallest_dist = distance_left
        else:
            smallest_dist = (distance_right[0], distance_right[1] + half, distance_right[2] + half)
        
        x_mid = cluster_list[half - 1].horiz_center()
        x_mid1 = cluster_list[half].horiz_center()
        mid = .5 * (x_mid + x_mid1)
        
        closest_to_strip = closest_pair_strip(cluster_list, mid, smallest_dist[0])
        
        if smallest_dist[0] > closest_to_strip[0]:
            smallest_dist = closest_to_strip
        
    return (smallest_dist)


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """

    inside_strip = []
    for idx in range(len(cluster_list)):
        if abs(cluster_list[idx].horiz_center() - horiz_center) < half_width:
            inside_strip.append(idx)

    
    inside_strip.sort(key = lambda idx: cluster_list[idx].vert_center())
    len_cluster_list = len(inside_strip)
    
    smallest_dist = (float("inf"), -1, -1)
    for idx_u in range(0, len_cluster_list - 1):
        for idx_v in range(idx_u + 1, min(idx_u + 4, len_cluster_list)):
            test_dist = pair_distance(cluster_list, inside_strip[idx_u], inside_strip[idx_v])
            if  smallest_dist[0] > test_dist[0]:
                smallest_dist = test_dist
        
    
    return (smallest_dist)
            

    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    
    return []


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
            
    return []

