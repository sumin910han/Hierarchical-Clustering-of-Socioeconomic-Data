import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from scipy.cluster.hierarchy import dendrogram

# takes in a string with a path to a CSV file and returns the data points as a list of dicts.
def load_data(filepath):
    data = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [dict(row) for row in reader]
    return data

# takes in one row dict from the data loaded from the previous function 
# then calculates the corresponding feature vector for that country as specified above, 
# and returns it as a NumPy array of shape (6,). The dtype of this array should be float64.
def calc_features(row):
    x1 = float(row['Population'])
    x2 = float(row['Net migration'])
    x3 = float(row['GDP ($ per capita)'])
    x4 = float(row['Literacy (%)'])
    x5 = float(row['Phones (per 1000)'])
    x6 = float(row['Infant mortality (per 1000 births)'])
    np_array = np.array([x1, x2, x3, x4, x5, x6], dtype=np.float64)

    return np_array

# performs complete linkage hierarchical agglomerative clustering on the country with the (x1, . . . , x6) feature representation, 
# and returns a NumPy array representing the clustering.
def hac(features):
    n = len(features)
    Z = np.zeros((n - 1, 4))
    d_matrix = distance_matrix(features, features)
    np.fill_diagonal(d_matrix, np.inf)
    clusters = {i: [i] for i in range(n)}
    next_cluster_index = n

    for k in range(n - 1):
        # Directly find the pair of clusters with the minimum distance
        min_dist = np.inf
        cluster1, cluster2 = -1, -1

        for c1 in clusters:
            for c2 in clusters:
                if c1 < c2:
                    dist = np.max(d_matrix[list(clusters[c1])][:, list(clusters[c2])])
                    # Update minimum and clusters if a smaller distance is found
                    # or if tie-breaking conditions are met
                    if dist < min_dist or (dist == min_dist and (c1 < cluster1 or (c1 == cluster1 and c2 < cluster2))):
                        min_dist, cluster1, cluster2 = dist, c1, c2
                        
        Z[k, 0] = cluster1
        Z[k, 1] = cluster2
        Z[k, 2] = min_dist
        total = set()
        total.update(clusters[cluster1])
        total.update(clusters[cluster2])
        Z[k, 3] = len(total)

        del clusters[cluster1]
        del clusters[cluster2]

        clusters[next_cluster_index] = total
        next_cluster_index += 1

    return np.array(Z)


# visualizes the hierarchical agglomerative clustering on the country’s feature representation.
def fig_hac(Z, names):
    fig = plt.figure()
    dendrogram(Z, labels=names, leaf_rotation=90)
    plt.tight_layout()
    plt.show()
    return fig

# takes a list of feature vectors and computes the normalized values. 
# The output should be a list of normalized feature vectors in the same format as the input.
def normalize_features(features):
    original_val = np.array(features)
    mean = np.mean(original_val, axis=0)
    sd = np.std(original_val, axis=0)

    normalized_feature_val = (original_val - mean)/sd
    normalized_data = [np.array(row) for row in normalized_feature_val]
    return normalized_data

if __name__=="__main__":
    data = load_data("countries.csv")
    country_names = [row["Country"] for row in data] 
    features = [calc_features(row) for row in data]
    features_normalized = normalize_features(features) 
    n = 50
    Z_raw = hac(features[:n])
    Z_normalized = hac(features_normalized[:n])
    fig = fig_hac(Z_raw, country_names[:n])
    plt.show()

