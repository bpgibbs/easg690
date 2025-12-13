

'''The following function is built to organize dataframes of an excel file or multiple excel files of Tl
isotope data generated at the Indiana University Heavy Metal Isotope Lab'''
def names_and_raw_values(your_data_frame):
    for i in range(len(your_data_frame)):
        
        #AI disclaimer: I used github copilot to learn how to sort lists by steps
        
        #Extracts entire norm 205/203 column. This is column o, starting at row 2 and going as far as there is data.
        norm_205_203 = your_data_frame[i].iloc[0:,14].tolist() #14 is column o of the excel file... isotope ratios normalized to instrument drift
        norm_205_203_error = your_data_frame[i].iloc[0:,15].tolist() #15 is column p of the excel file... error vals

        #sort standards and samples into separate lists
        standards_norm_205_203 = norm_205_203[0::2] #starts at index zero, goes to end of list in steps of two
        samples_norm_205_203 = norm_205_203[1::2] #starts at index one, goes to end of list in steps of two
        #Same thing as last two lines but for errors
        standards_norm_205_203_error = norm_205_203_error[0::2]
        samples_norm_205_203_error = norm_205_203_error[1::2]

        #stores sample names
        standard_norm_205_203_name = your_data_frame[i].iloc[0,16] #16 is standard/sample names... no need for list because only one standard is used
        samples_norm_205_203_names = your_data_frame[i].iloc[1::2,16].tolist() #stores values of row 16 in steps of two starting at index one

        #for loop that combines sample names with their values and errors in two lists, one with normalized values and one with error values
        samples_and_names = []
        sample_errors_and_names = []
        for i in range(len(samples_norm_205_203)):
            result_sample = [samples_norm_205_203[i],samples_norm_205_203_names[i]]
            result_sample_error = [samples_norm_205_203_error[i],samples_norm_205_203_names[i]]
            samples_and_names.append(result_sample)
            sample_errors_and_names.append(result_sample_error)
            
    return [samples_and_names, sample_errors_and_names]




'''The following function is used to redefine names of analyzed samples from the IU 
Heavy Metal Isotope Lab MC-ICP-MS raw data files'''
def redefine_names(list_of_names_from_file, list_of_desired_names, data_experiment_location):
    
    '''Two if statements check that all the lists are the same lengths, as this is imperative for the function.
    If list sizes are not the same, an error and a frowny face are printed.'''
    
    exp_locations = ['substrate', 'stem','leaves','flower stems','flowers','seed pods']
    
    if len(list_of_names_from_file) != len(list_of_desired_names):
        print('incompatible list sizes :(')
        
    elif len(list_of_names_from_file) != len(data_experiment_location):
        print('incompatible list sizes :(')
        
    else:
        name_data = []
        for i in range(len(list_of_names_from_file)):
            name_data.append([list_of_names_from_file[i],list_of_desired_names[i],exp_locations[data_experiment_location[i]]])
        return name_data





'''The following function is used to join the previous two functions into a list of data
that is easy for the programer (hi) to work with and the user to understand'''
def solidify_name_schematic(your_data_frame, list_of_names_from_file, list_of_desired_names, data_experiment_location):
    
    #assigns 2D list of sample vals with raw names and sample errors with raw names
    values_and_errors = names_and_raw_values(your_data_frame) 
    
    #assigns return values of user's prefered data names
    your_names = redefine_names(list_of_names_from_file, list_of_desired_names, data_experiment_location)
    
    #in the following nested for loop, values_and_errors data are changed from raw names to prefered names
    for j in range(len(values_and_errors)): #loops through normalized isotopic values and their errors
        for i in range(len(values_and_errors[0])): #loops through the length of the 0 element of values_and_errors
            for k in range(len(your_names)): #loops through every name correction
                if values_and_errors[j][i][1] == your_names[k][0]: #checks if names in lists match
                    values_and_errors[j][i][1] = your_names[k][1] #reassigns names to new names in values_and_errors
                    values_and_errors[j][i].append(your_names[k][2]) #adds in experiment location
                    
    return values_and_errors