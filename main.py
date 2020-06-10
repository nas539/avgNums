from functools import reduce

def get_avg(num_list):
    total = reduce((lambda total, element: total + element), num_list)

    return total / len(num_list)