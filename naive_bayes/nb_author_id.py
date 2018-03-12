#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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

#>>> import numpy as np
#>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
#print X
#>>> Y = np.array([1, 1, 1, 2, 2, 2])
#print Y
#
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

t_train = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t_train, 3), "s"

t_test = time()
clf.predict(features_train)
print "testing time:", round(time()-t_test, 3), "s"

t_test = time()
clf.predict(features_test)
print "testing time:", round(time()-t_test, 3), "s"

t_test = time()
print clf.score(features_test, labels_test)
print "testing time:", round(time()-t_test, 3), "s"

t_test_train = time()
print clf.score(features_train, labels_train)
print "test_training time:", round(time()-t_test_train, 3), "s"


#########################################################


