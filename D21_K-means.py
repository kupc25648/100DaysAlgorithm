'''
Very easy, yet very power technique used in unsupervised learning is k-means clustering.

K-means first chooses some random clusters. Then assigns each point to the nearest cluster using L2 measure and computes a new cluster centre as mean of all the points inside. These two steps are repeated until convergence.

pros
algorithm is guaranteed to converge
is very fast, works well even on a subsample
is generic; initial clusters, distance measure and centre definition may be adapted to your needs

cons
number of clusters has to be specified manually, it’s detection is very difficult
result tends to be very unstable — which means very — you should re-run many times and choose the best result

https://en.wikipedia.org/wiki/K-means_clustering


run
The code to generate random dataset is available at github. Its result is plot attached below. You can compare the original clusters to those found by k-means. Note that the distributions are strongly overlapped on purpose.


'''
import numpy as np
import matplotlib.pyplot as plt

def kmeans(points, n_clusters):
    # sample initital centroids
    sample = np.random.choice(
        len(points), n_clusters, replace = False)

    centroid = points[sample]

    loss= [-1,-2]
    while not np.allclose(*loss):
        # compute distance for each pair: point/centroid
        distance = [np.sqrt(((points-c)**2).sum(1)) for c in centroid]

        # new loss
        loss = loss[1:] + [np.sum(distance)]
        # assign new clusters
        cluster = np.argmin(distance, axis = 0)
        # update centroids by new cluster means
        for i in range(n_clusters):
            centroid[i] = np.mean(points[cluster == i], axis =0)

    return cluster

'''
run
The code to generate random dataset is available at github. Its result is plot attached below. You can compare the original clusters to those found by k-means. Note that the distributions are strongly overlapped on purpose.
'''

n = 100
A = np.random.multivariate_normal([2, 0], [[1, .1], [-4, 1]], n)
B = np.random.multivariate_normal([-2, 0], [[1, -4], [.1, 1]], n)
C = np.random.multivariate_normal([2, -2], [[1, 4], [-.1, 1]], n)
D = ['red', 'green', 'blue']

points = np.r_[A, B, C]
original_color = np.repeat(D[:3], n)

cluster = kmeans(points, 3)
new_color = [D[i] for i in cluster]




plt.scatter(x=points[:, 0], y=points[:, 1], color=original_color)

plt.show()
plt.scatter(x=points[:, 0], y=points[:, 1], color=new_color)

plt.show()



