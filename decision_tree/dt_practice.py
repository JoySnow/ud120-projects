#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys

sys.path.append("../choose_your_own/")
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

from sklearn import tree

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!


clf = tree.DecisionTreeClassifier()
clf.fit( features_train, labels_train )


prettyPicture(clf, features_test, labels_test)
plt.show()

print clf.score( features_test, labels_test )


