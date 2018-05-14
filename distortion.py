"""
computing distortion to check automation and accuracy
"""
import Closest_pair_clustering as cpc
from alg_project3_viz import load_data_table
import matplotlib.pyplot as plt
#import alg_clusters_matplotlib
#import math
#import random


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"



############################################################



def get_clusters(data_url, num_clusters, alg, data_table):
    """
    Load a data table, compute a list of clusters
    """
    
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    
    if alg == 'hier':
        cluster_list = cpc.hierarchical_clustering(singleton_list, num_clusters)
    elif alg == 'kmeans':
        cluster_list = cpc.kmeans_clustering(singleton_list, num_clusters, 5)	
    
    return cluster_list


def compute_distortion(cluster_list, data_url, data_table):
    """
    Takes a list of clusters and uses cluster_error to compute its distortion. 
    """
    
    
    errors = [cluster.cluster_error(data_table) for cluster in cluster_list]
    return sum(errors)


def quality_check(data_url, alg):
    x = []
    y = []
    data_table = load_data_table(data_url)
    for num in range(6, 21):
        x.append(num)
        cluster_list = get_clusters(data_url, num, alg, data_table)
        y.append(compute_distortion(cluster_list, data_url, data_table))
    
    return (x, y)

hier = quality_check(DATA_111_URL, 'hier')
x_hier = hier[0]
y_hier = hier[1]

kmeans = quality_check(DATA_111_URL, 'kmeans')
x_kmeans = kmeans[0]
y_kmeans = kmeans[1]

plt.style.use('default')
fig = plt.figure(figsize = (9, 5))
ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(x_hier, y_hier, label = 'hierarchical') # ls='None', marker='.', ms = 6, mec='black', mew=.5, c='red')
ax1.plot(x_kmeans, y_kmeans, label = 'k-means')
ax1.legend(loc = 'best')
ax1.set_title('Distortion for 111 Data Set', weight=600)
ax1.set_xlabel('Number of Clusters')
ax1.set_ylabel('Distortion of Output')

#plt.savefig('Images/Distortion 111', orientation='landscape')
plt.show()


"""
As a check on the correctness, the distortions associated with the 16 output clusters produced by hierarchical clustering and k-means clustering (with 5 iterations) on the 290 county data set are 2.575×10^11 and 2.323×10^11.

Q5 = 9 clusters by hierarchical clustering to the 111 county cancer risk data set.
Q6 = 9 clusters by 5 iterations of k-means clustering to the 111 county cancer risk data set.

"""
    
