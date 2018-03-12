import sys

sys.path.append("../choose_your_own/")
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()


########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
#clf = SVC(kernel="linear")
#clf = SVC(kernel="linear", C=1000.0)
# clf = SVC(kernel="linear", gamma=1.0)

clf = SVC(kernel="rbf", C=1.0)

print clf
## SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
##   decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
##   max_iter=-1, probability=False, random_state=None, shrinking=True,
##   tol=0.001, verbose=False)

#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
clf.fit(features_train, labels_train)

#### store your predictions in a list named pred
pred = clf.predict( features_test)


prettyPicture(clf, features_test, labels_test)
plt.show()



from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print acc

#def submitAccuracy():
#    return acc
