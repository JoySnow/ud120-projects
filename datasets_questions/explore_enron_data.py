#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

#sum = 0
#for i in enron_data:
#    #print i
#    if enron_data[i]["poi"]:
#        sum += 1
#
#print sum

#poi_nu = 0
#f = open("../final_project/poi_names.txt", "r")
#print f
#names = f.readlines()
#print names
#for n in names[2:]:
#    flag = n[1]
#    name = n[4:-1]
#    print flag, name
#    if flag == "y":
#        poi_nu += 1
#print poi_nu

#name = "Prentice James".upper()
#print enron_data[name]
#print enron_data[name]["restricted_stock"] + enron_data[name]["exercised_stock_options"]
#
#name = "Colwell Wesley".upper()
#print enron_data[name]["from_this_person_to_poi"]
#
#name = "Skilling Jeffrey K".upper()
#print enron_data[name]["exercised_stock_options"]

#sum, sum_e = 0, 0
#for i in enron_data:
#    #print i
#    if enron_data[i]["salary"] != "NaN":
#        sum += 1
#    if enron_data[i]["email_address"] != "NaN":
#        sum_e += 1
#
#print sum, sum_e

#poi_names = []
#poi_nu = 0
#f = open("../final_project/poi_names.txt", "r")
#print f
#names = f.readlines()
#print names
#for n in names[2:]:
#    flag = n[1]
#    name = n[4:-1]
#    print flag, name
#    if flag == "y":
#        poi_nu += 1
#print poi_nu


for i in enron_data:
    print enron_data[i]
    break

sum, sum_e = 0, 0
for i in enron_data:
    #print i
    if enron_data[i]["poi"]:
        print enron_data[i]["total_payments"]
        sum_e += 1
        if enron_data[i]["total_payments"] == "NaN":
            sum += 1

print sum, sum_e
print float(sum) / sum_e
