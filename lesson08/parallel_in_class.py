from simplempi.parfor import parfor, pprint
import homework_7_part3_generator

# define the number of timesteps
n_frames = 720

# create a list of timesteps to loop over
times = list(range(n_frames))

#generates frame
for t in parfor(times):
    #print which timestep os being worked on
    pprint(f'Working on timestep {t}')
    #run the generateframe function on each process
    homework_7_part3_generator.generate_frame(t)
