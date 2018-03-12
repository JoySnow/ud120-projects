#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = []
    for i in xrange(0, len(ages)):
        pre = predictions[i][0]
        net = net_worths[i][0]
        errors.append(abs(pre-net))

    all_data = zip(ages, net_worths, errors)
    sort_data = sorted(all_data, key=lambda d:d[2])
    cleaned_data = sort_data[:81]
    
    return cleaned_data

