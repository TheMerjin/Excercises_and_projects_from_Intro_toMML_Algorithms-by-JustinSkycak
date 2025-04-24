from Matrix import Matrix
from copy import deepcopy
import matplotlib
from matplotlib import pyplot as plt
import random
columns = ['Portion Eggs', 'Portion Butter', 'PortionSugar', 'Portion Flour']
data = [
[0.14, 0.14, 0.28, 0.44],
[0.22, 0.1, 0.45, 0.33],
[0.1, 0.19, 0.25, 0.4 ],
[0.02, 0.08, 0.43, 0.45],
[0.16, 0.08, 0.35, 0.3 ],
[0.14, 0.17, 0.31, 0.38],
[0.05, 0.14, 0.35, 0.5 ],
[0.1, 0.21, 0.28, 0.44],
[0.04, 0.08, 0.35, 0.47],
[0.11, 0.13, 0.28, 0.45],
[0.0, 0.07, 0.34, 0.65],
[0.2, 0.05, 0.4, 0.37],
[0.12, 0.15, 0.33, 0.45],
[0.25, 0.1, 0.3, 0.35],
[0.0, 0.1, 0.4, 0.5 ],
[0.15, 0.2, 0.3, 0.37],
[0.0, 0.13, 0.4, 0.49],
[0.22, 0.07, 0.4, 0.38],
[0.2, 0.18, 0.3, 0.4 ]
]


def k_means_clustering(data, k, max_iterations=100):
    matrix_k = Matrix(data)
    n = matrix_k.num_rows  # total number of inner lists you want
    pattern = range(1,k+1)

    to_prepend = [[pattern[i % k]] for i in range(n)]
    matrix_k.prepend(to_prepend)

    clusters = { k+1 : [] for k in range(k)}
    for row in matrix_k.matrix:
        clusters[row[0]].append(deepcopy(row[1:]))
    matrix_k.remove_col(0)
    
    for k,v in clusters.items():
        clusters[k] = Matrix(v)
    for i in range(1000):
        mean_clusters = {}
        for k,v in clusters.items():
            mean_clusters[k] = v.mean_cols()
       
        new_clusters = {k+1 : [] for k in range(k)}
        for row in matrix_k.matrix:
            row_vector = Matrix([row])
            min_dist = float("inf")
            closest_cluster = None
            for cluster, mean in mean_clusters.items():
                try: 
                    dist = row_vector.euclidean_distance(mean)
                except ValueError:
                    dist = 0
                if dist < min_dist:
                    min_dist = dist
                    closest_cluster = cluster
            new_clusters[closest_cluster].append(deepcopy(row))
        for k,v in new_clusters.items():
            if len(v) == 0:
                new_clusters[k] = Matrix([random.choice(matrix_k.matrix)])
            else:

                new_clusters[k] = Matrix(v)
        if clusters == new_clusters:
            total_distance = 0 
            for row in matrix_k.matrix:
                row_vector = Matrix([row])
                min_dist = float("inf")
                for cluster, mean in mean_clusters.items():
                    dist = row_vector.euclidean_distance(mean)
                    if dist < min_dist:
                        min_dist = dist
                total_distance += min_dist
            return clusters, total_distance
        clusters = new_clusters
    total_distance = 0 

    for row in matrix_k.matrix:
        row_vector = Matrix([row])
        min_dist = float("inf")
        for cluster, mean in mean_clusters.items():
            try:
                dist = row_vector.euclidean_distance(mean)
            except ValueError:
                dist = 0
            if dist < min_dist:
                min_dist = dist
        total_distance += min_dist
    return clusters, total_distance



output = k_means_clustering(data, 6)
for k,v in output[0].items():
    print(k)
    print("\n")
    v.show()
total_distance = output[1]
print( "total distance",total_distance)

k_vals = [i for i  in range(1,10)]
distances = []
for k_val in k_vals:
    distances.append(k_means_clustering(data, k= k_val)[1])

        
plt.plot(k_vals, distances)
plt.show()





