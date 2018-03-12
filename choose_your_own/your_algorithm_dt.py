#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

print len(features_train)
print len(features_test)

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

# 
# #### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
# ################################################################################
# 

### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary








from time import time
import sys


def foo(clf, funname):

    t_train = time()
    clf.fit(features_train, labels_train)
    #print "training time:", round(time()-t_train, 3), "s"
    train_time = round(time()-t_train, 3)

    t_test = time()
    score = clf.score(features_test, labels_test)
    #print "testing time:", round(time()-t_test, 3), "s"
    test_time = round(time()-t_test, 3)

    return [score, train_time, test_time]

    try:
	prettyPicture(clf, features_test, labels_test, funname)
    except NameError:
	pass


def dt():

    from sklearn import tree

    clf = tree.DecisionTreeClassifier( min_samples_split=40 )

    return foo(clf, sys._getframe().f_code.co_name)


def knn():

    from sklearn.neighbors import KNeighborsClassifier

    clf3 = KNeighborsClassifier(n_neighbors=3)
    clf5 = KNeighborsClassifier(n_neighbors=5)
    clf7 = KNeighborsClassifier(n_neighbors=7)

    return [foo(clf3, sys._getframe().f_code.co_name),
            foo(clf5, sys._getframe().f_code.co_name),
            foo(clf7, sys._getframe().f_code.co_name)]


print dt()
#print knn()
