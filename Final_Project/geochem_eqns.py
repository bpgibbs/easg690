'''This function will calculate all epsilon values in a dataset'''
import numpy as np

def epsilon_vals(your_data):
    
    #this is the NIST SRM 997, used to calculate epsilon values
    NIST_997_205_203 = 2.38714

    #loops through sample values to create list of epsilon values
    epsilon_205_203 = []
    for i in range(len(your_data[0])):
        val = ((your_data[0][i][0] / NIST_997_205_203) - 1) * 10000
        epsilon_205_203.append(val)

    #for loop that combines sample names with their values and errors in two lists, one with epsilon values and one with epsilon error values
    epsilon_samples_and_names = []
    
    for i in range(len(epsilon_205_203)):
        epsilon_result_sample = [epsilon_205_203[i], your_data[0][i][1]]
        epsilon_samples_and_names.append(epsilon_result_sample)
    return epsilon_samples_and_names

'''This function will calculate all delta values in a dataset'''
def delta_vals(your_data):
    
    #this is the NIST SRM 997, used to calculate epsilon values
    NIST_997_205_203 = 2.38714

    #loops through sample values to create list of epsilon values
    delta_205_203 = []
    for i in range(len(your_data[0])):
        val = ((your_data[0][i][0] / NIST_997_205_203) - 1) * 1000
        delta_205_203.append(val)

    #for loop that combines sample names with their values and errors in two lists, one with epsilon values and one with epsilon error values
    delta_samples_and_names = []
    
    for i in range(len(delta_205_203)):
        delta_result_sample = [delta_205_203[i], your_data[0][i][1]]
        delta_samples_and_names.append(delta_result_sample)
    return [delta_samples_and_names]




