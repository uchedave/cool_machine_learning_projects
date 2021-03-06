import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {
    'k':[
        [1, 2],
        [2, 3],
        [3, 1]
    ],
    'r': [
        [6, 5],
        [7, 7],
        [8, 6]
    ]
}

new_feature = [5, 7]

def k_nearset_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups.')

    distances = []
    for group in data:
        for features in data[group]:
            # euclidean_distance = sqrt( (features[0] - predict[0]) ** 2 + (features[1] - predict[1])**2) This method is not fast enough
            # euclidean_distance = np.sqrt( np.sum(  
            #     (np.array(features) - np.array(predict)) ** 2 
            # ) )
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]

        return vote_result