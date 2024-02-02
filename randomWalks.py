import numpy as np;
import matplotlib.pyplot as plt

# importing necessary tools for random color for each walk
from itertools import cycle
cycol = cycle('bgrcmk')

# taking inputs from the user about the number of points and limits
steps = int (input("enter the number of random steps : "))
walks = int (input("enter the number of random walks : "))
dims = int (input("enter the number of random dimension : "))

# samlying a high dimension uniform distribution with in open interval (0,1) it can be understood as walks number of matrices stacked upon each other where each row in a matrix represents total steps and the columns represents the dimensions
uniformRandomDist = np.random.rand(walks,dims,steps);

# replacing each points with 1 if it is more the 0.5 and -1 else wise, because adding 1 will move to right or up and -1 shall move to left or downwards
uniformRandomDist = (uniformRandomDist > 0.5) * 2 -1

# generating the path array that represents the path being follwed, initialy all zero
# increasing the steps by one so as to start from the origin
pathArray = np.zeros((walks,dims,steps+1));

# replacing the each zero (except the first one to make start from origin) in the path array with commulative sum upto the same index (since both arrays have compatible shape) along the axis 2 (that represents the steps that are in -1 and 1 form) so that resultantly we have co-ordinates after each step in path array.
pathArray[:,:,1:] = np.cumsum(uniformRandomDist,axis=2);

# iterating over the path array to plot the walks, it is infact the iteration over each walk matrix
for index,subArr in enumerate(pathArray):
    # checking the length to see if randomness was required only in one path
    if len(subArr)!=2:
        # in this case the x is continously increasing and is obtained as follwoing
        temp = np.linspace(0,steps,steps)
        # finaly plotting the walk.
        plt.plot(temp, subArr[0], color=next(cycol))
    else:
    # if we already have two random dimensions then no need to make a synthetic one here
        plt.plot(subArr[0],subArr[1], color=next(cycol))
plt.title(f'steps = {steps}, walks = {walks}, random dimensions = {dims} ')
plt.show()