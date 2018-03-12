#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################


features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]


from sklearn.svm import SVC

print "=== Start of clf1 ==="
clf1 = SVC(kernel="rbf", C=10.0)

t_train = time()
clf1.fit(features_train, labels_train)
print "training time:", round(time()-t_train, 3), "s"

t_test = time()
print clf1.score(features_test, labels_test)
print "testing time:", round(time()-t_test, 3), "s"

print "=== End of clf1 ==="

print "=== Start of clf2 ==="
clf2 = SVC(kernel="rbf", C=100.0)

t_train = time()
clf2.fit(features_train, labels_train)
print "training time:", round(time()-t_train, 3), "s"

t_test = time()
print clf2.score(features_test, labels_test)
print "testing time:", round(time()-t_test, 3), "s"

print "=== End of clf2 ==="

print "=== Start of clf3 ==="
clf3 = SVC(kernel="rbf", C=1000.0)

t_train = time()
clf3.fit(features_train, labels_train)
print "training time:", round(time()-t_train, 3), "s"

t_test = time()
print clf3.score(features_test, labels_test)
print "testing time:", round(time()-t_test, 3), "s"

print "=== End of clf3 ==="

print "=== Start of clf4 ==="
clf4 = SVC(kernel="rbf", C=10000.0)

t_train = time()
clf4.fit(features_train, labels_train)
print "training time:", round(time()-t_train, 3), "s"

t_test = time()
print clf4.score(features_test, labels_test)
print "testing time:", round(time()-t_test, 3), "s"

print "=== End of clf4 ==="

#t_test_train = time()
#print clf.score(features_train, labels_train)
#print "test_training time:", round(time()-t_test_train, 3), "s"

#prettyPicture(clf, features_test, labels_test)
#plt.show()



#from sklearn.metrics import accuracy_score
#acc = accuracy_score(pred, labels_test)
#
#print acc
