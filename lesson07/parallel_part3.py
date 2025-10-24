from mpi4py import MPI
import homework_7_part3_generator

# get the 'communicator'
comm = MPI.COMM_WORLD

# get the 'rank' of the process
my_rank = comm.rank

#generates frame
homework_7_part3_generator.generate_frame(my_rank)
