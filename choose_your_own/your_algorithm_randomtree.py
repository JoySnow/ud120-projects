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

    try:
	prettyPicture(clf, features_test, labels_test, funname)
    except NameError:
	pass

    return [score, train_time, test_time]


def random_tree():

    from sklearn.ensemble import RandomForestClassifier
    # from sklearn.ensemble import ExtraTreesClassifier

    clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=50, random_state=0)
    return foo(clf, "random_tree")

#    clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,	min_samples_split=2, random_state=0)
#    scores = cross_val_score(clf, X, y)
#
#
#    result = []
#    for k in ka:
#        clf = KNeighborsClassifier(n_neighbors=k)
#        result.append(foo(clf, "knn_clf"+str(k)))
#
#    return result


#print knn([3, 23, 53, 101])
print random_tree()
