
import numpy as np
import pandas as pd

'''The following outputs a list of three lists. If num is 0, the lists will be 
[isotope_data, mineral_names, expirement_part]. If num is 1, the lists will be
[isotope_error_data, mineral_names, expirement_part]'''
#to call isotope data, make num 0. To call errors, make num 1
def sort_the_min_groups(data,num):
    #empty lists to create lists of all data components as they appear
    data_output = []
    min_name = []
    part = []
    for i in range(len(data[0])):
        data_output.append(data[num][i][0])
        min_name.append(data[0][i][1])
        part.append(data[0][i][2])
    return [data_output, min_name, part]


'''The following function sorts through data and gathers it such that there is a list of two lists: the first
list contains isotope data values pertaining to one specific, SINGULAR mineral and the second list are the 
expirament parts (substrate, leaves...) that pertain to each data point in the first list'''

#make num 0 to use isotope value data, and make num 1 to use errror data

def data_plotter_for_one_min(data, mineral,num):
    #by starting following lists of data at plant parts with a None values and strings, it will be assured that a figure will 
    #be plotted in correct order
    
    #these lists will contain x values at particular susbstrates (epsilon or delta notation). Y vals are just string names.
    substrate = ['substrate']
    stem = ['stem']
    leaves = ['leaves']
    flower_stems = ['flower stems']
    flowers = ['flowers']
    seed_pods = ['seed pods']
    
    #these lists will contain x values at particular susbstrates (epsilon or delta notation)
    value_data_substrate = [np.nan]
    value_data_stem = [np.nan]
    value_data_leaves = [np.nan]
    value_data_flower_stems = [np.nan]
    value_data_flowers = [np.nan]
    value_data_seed_pods = [np.nan]
    
    new_structure = sort_the_min_groups(data, num) #uses structure created in sort_the_min_groups to create x and y data sets
    
    #creates x data and y data if mineral boolean is satisfied
    for i in range(len(new_structure[1])):
        if new_structure[1][i] == mineral:
            
            #these will sort string assignments into lists with their associated values
            if new_structure[2][i] == 'substrate':
                substrate.append(new_structure[2][i])
                value_data_substrate.append(new_structure[0][i])
            elif new_structure[2][i] == 'stem':
                stem.append(new_structure[2][i])
                value_data_stem.append(new_structure[0][i])
            elif new_structure[2][i] == 'leaves':
                leaves.append(new_structure[2][i])
                value_data_leaves.append(new_structure[0][i])
            elif new_structure[2][i] == 'flower stems':
                flower_stems.append(new_structure[2][i])
                value_data_flower_stems.append(new_structure[0][i])
            elif new_structure[2][i] == 'flowers':
                flowers.append(new_structure[2][i])
                value_data_flowers.append(new_structure[0][i])
            else:
                seed_pods.append(new_structure[2][i])
                value_data_seed_pods.append(new_structure[0][i])
    #creates list of all x values... also flattens said list
    xvals = sum([value_data_substrate, value_data_stem,value_data_leaves,value_data_flower_stems,value_data_flowers,value_data_seed_pods], [])
    yvals = sum([substrate,stem,leaves,flower_stems,flowers,seed_pods],[])
    return [xvals,yvals]



'''The following block of code is meant to be called when plotting to plot averages of isotope values and
error values instead of generating a scatterplot of multiple values.

(Note for Travis - I ditched what I showed you in class and wrote this function without copilot,
so there is no A.I. disclaimer for this)'''
def calc_min_averages(data, mineral, num): #reads in working data (aka our_working_data), mineral, num (vals vs error)
    
    #lists to average
    substrate_list = []
    stem_list = []
    leaves_list = []
    flower_stems_list = []
    flowers_list = []
    seed_pods_list = []
    
    #based on the value of "part" when calling data_plotter_for_one_min(data,mineral,num)[1], numbers will be added
    #to corresponding lists from data_plotter_for_one_min(data,mineral,num)[0][i] to be averaged
    for i in range(len(data_plotter_for_one_min(data,mineral,num)[1])):
        if data_plotter_for_one_min(data,mineral,num)[1][i] == 'substrate': #checks "part"
            substrate_list.append(data_plotter_for_one_min(data,mineral,num)[0][i]) #adds value to list
        elif data_plotter_for_one_min(data,mineral,num)[1][i] == 'stem':
            stem_list.append(data_plotter_for_one_min(data,mineral,num)[0][i])
        elif data_plotter_for_one_min(data,mineral,num)[1][i] == 'leaves':
            leaves_list.append(data_plotter_for_one_min(data,mineral,num)[0][i])
        elif data_plotter_for_one_min(data,mineral,num)[1][i] == 'flower stems':
            flower_stems_list.append(data_plotter_for_one_min(data,mineral,num)[0][i])
        elif data_plotter_for_one_min(data,mineral,num)[1][i] == 'flowers':
            flowers_list.append(data_plotter_for_one_min(data,mineral,num)[0][i])
        else:
            seed_pods_list.append(data_plotter_for_one_min(data,mineral,num)[0][i])
    
    #pd.Series is used so that np.nan is compatible with .mean()
    substrate_average = pd.Series(substrate_list).mean()
    stem_average = pd.Series(stem_list).mean()
    leaves_average = pd.Series(leaves_list).mean()
    flower_stems_average = pd.Series(flower_stems_list).mean()
    flowers_average = pd.Series(flowers_list).mean()
    seed_pods_average = pd.Series(seed_pods_list).mean()
    
    #returns averages in one list and corresponding plant parts in another. Two list 
    # format is to mimick other created structures.
    return([[substrate_average,stem_average,leaves_average,flower_stems_average, flowers_average,seed_pods_average,],
            ['substrate', 'stem','leaves','flower stems','flowers','seed pods']])