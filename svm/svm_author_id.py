#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys

sys.path.append("../choose_your_own/")
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl

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


#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
#
#print features_train[0:2]
#print labels_train[0:2]
#
#print features_train[26]
#print labels_train[26]

from sklearn.svm import SVC
clf = SVC(kernel="rbf", C=10000.0)
print clf


t_train = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t_train, 3), "s"

print "===FINISH TRAIN==="

#prettyPicture(clf, features_test, labels_test)
#plt.show()

#### store your predictions in a list named pred
pred = clf.predict( features_test)

print "len(pred)", len(pred)

print sum(pred)

#print clf.predict( features_test[9] )
#print clf.predict( features_test[10] )
#print clf.predict( features_test[25] )
#print clf.predict( features_test[26] )
#print clf.predict( features_test[49] )
#print clf.predict( features_test[50] )


#t_test = time()
#print clf.score(features_test, labels_test)
#print "testing time:", round(time()-t_test, 3), "s"

#t_test_train = time()
#print clf.score(features_train, labels_train)
#print "test_training time:", round(time()-t_test_train, 3), "s"




#from sklearn.metrics import accuracy_score
#acc = accuracy_score(pred, labels_test)
#
#print acc
