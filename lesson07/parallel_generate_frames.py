from mpi4py import MPI
import generate_frame

# get the 'communicator'
comm = MPI.COMM_WORLD

# get the 'rank' of the process
my_rank = comm.rank

#generates frame
generate_frame.generate_frame(my_rank)