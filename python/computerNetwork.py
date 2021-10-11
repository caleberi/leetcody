# You are given a two-dimensional matrix containing only ones and zeroes representing a computer network.
# Every one in the matrix represents a server and every zero represents an empty space.
# Two servers within the network can communicate if they are either in the same row or the same column.
# Return the total number of servers that can communicate with at least one other server.

# Ex: Given the following matrix…

# matrix = [
#   [1, 0],
#   [1, 0],
# ], return 2 (both servers are in the same column and can therefore communicate with one another).
# Ex: Given the following matrix…

# matrix = [
#   [1, 0],
#   [0, 1],
# ], return 0.


def computerNetwork(network):
    visited = [[0 if network[i][j] == 1 else 1 for j in range(
        len(network[i]))] for i in range(len(network))]

    pass


################################
######## INTIUTION #############
"""
[1,0,1]
[0,0,1]
[1,0,0]

"""
