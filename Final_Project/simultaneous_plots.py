from mpi4py import MPI
import tl_plot_aid as tlplt
import tl_data_organization as org

# get the 'communicator'
comm = MPI.COMM_WORLD

# get the 'rank' of the process
my_rank = comm.rank


'''The parameters for the function are as follows... first: a list containing a files or files with plant isotopic
values derived from mineral substrates as output by MC-ICP-MS. Second: a list of strings that are the names or IDs 
of the minerals exactly as they appear in raw MC-ICP-MS data file(s). Third: your preferred mineral names as they correspond
to names/IDs from MC-ICP-MS data files. Fourth: integers corresponding to plant parts - 
[0, 1, 2, 3, 4, 5] = [Substrate, Stem, Leaves, Flower Stems, Flowers, Seed Pods].'''
def three_mineral_plot(file_or_files, mineral_list, old_min_names, pref_min_names, plant_parts):

    data_frames = []
    #creates list with dataframes
    for i in range(len(file_or_files)):
        data_frames.append(pd.read_excel(file_or_files[i]))
    
    org.names_and_raw_values(data_frames) #organizes data
        
    mineral = mineral_list[my_rank]  # Each rank works on a different mineral
    
    #creates the main working data set
    our_working_data = org.solidify_name_schematic(data_frames, 
    old_min_names, pref_min_names, plant_parts)
    
    #plots averages for the mineral in the much larger fabricated data seet
    plt.figure(figsize=(10, 6))
    plt.scatter(tlplt.calc_min_averages(our_working_data,mineral,0)[0], #calcs and plots averages
    tlplt.calc_min_averages(our_working_data,mineral,0)[1], color='blue', label=mineral) #plots parts for averages 
    plt.xlabel('ε$^{205}$Tl Values',fontsize=14)
    plt.ylabel('Plant Parts',fontsize=14)
    #y_all and yticks suggested by chatgpt
    y_all = ['substrate', 'stem','leaves','flower stems','flowers','seed pods']
    plt.yticks(y_all)

    rangeVal = len(tlplt.calc_min_averages(our_working_data,'Feldspar',0)[0])

    #connect data points with lines ---- this was written with Github Copilot but modified to be lightblue
    for i in range(rangeVal-1):
        plt.plot(tlplt.calc_min_averages(our_working_data,'Feldspar',0)[0][i:i+2], \
            tlplt.calc_min_averages(our_working_data,'Feldspar',0)[1][i:i+2], color='lightblue')

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title('ε$^{205}$Tl Values by Plant Part for Different Mineral Sources', fontsize=18)
    plt.legend()
    plt.grid(True)
    plt.savefig('three_mineral_figure.png')