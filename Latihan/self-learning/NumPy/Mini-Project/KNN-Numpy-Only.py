from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np


def knn(xTrain, xTest, k):
    """
    Finds the k nearest neighbors of xTest in xTrain.
    Input:
    xTrain = n x d matrix. n=rows and d=features
    xTest = m x d matrix. m=rows and d=features (same amount of features as xTrain)
    k = number of nearest neighbors to be found
    Output:
    dists = distances between xTrain/xTest points. Size of n x m
    indices = kxm matrix with indices of yTrain labels
    """

    # the following formula calculates the Euclidean distances.
    distances = -2 * xTrain@xTest.T + \
        np.sum(xTest**2, axis=1) + np.sum(xTrain**2, axis=1)[:, np.newaxis]

    # because of numpy precision, some really small numbers might
    # become negatives. So, the following is required.
    distances[distances < 0] = 0

    # for speed you can avoid the square root since it won't affect
    # the result, but apply it for exact distances.
    distances = distances**.5
    indices = np.argsort(distances, 0)  # get indices of sorted items
    distances = np.sort(distances, 0)  # distances sorted in axis 0

    # returning the top-k closest distances.
    return indices[0:k, :], distances[0:k, :]


#!-----------------------------------------------------------------------------------


def knn_predictions(xTrain, yTrain, xTest, k=3):
    """
    Input:
    xTrain = n x d matrix. n=rows and d=features
    yTrain = n x 1 array. n=rows with label value
    xTest = m x d matrix. m=rows and d=features
    k = number of nearest neighbors to be found
    Output:
    predictions = predicted labels, ie preds(i) is the predicted label of xTest(i,:)
    """

    indices, distances = knn(xTrain, xTest, k)
    yTrain = yTrain.flatten()
    rows, columns = indices.shape
    predictions = list()
    for j in range(columns):
        temp = list()
        for i in range(rows):
            cell = indices[i][j]
            temp.append(yTrain[cell])

        # this is the key function, brings the mode value
        predictions.append(max(temp, key=temp.count))
    predictions = np.array(predictions)
    return predictions


#!-------------------------------------------------------------------------------


# will first check which is the best k
Ks = 15
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))
# ConfustionMx = []
for n in range(1, Ks):
    # Train Model and Predict
    # neigh = KNeighborsClassifier(n_neighbors=n).fit(xTrain, yTrain)
    # yhat = neigh.predict(xTest)
    yhat = knn_predictions(xTrain, yTrain, xTest, n)
    mean_acc[n-1] = metrics.accuracy_score(yTest, yhat)
    std_acc[n-1] = np.std(yhat == yTest)/np.sqrt(yhat.shape[0])

print("The best accuracy was:", np.round(
    mean_acc.max()*100, 2), "% with k=", mean_acc.argmax()+1)

plt.plot(range(1, Ks), mean_acc, 'g')
plt.fill_between(range(1, Ks), mean_acc - 1 * std_acc,
                 mean_acc + 1 * std_acc, alpha=0.05)
plt.legend(('Accuracy ', '+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbors (k)')
plt.tight_layout()
plt.show()
