import matplotlib.pyplot as plt
import numpy as np
# simulating the task 1

#defining the inverse of the cumulative distribution function of the laplace disttribution
def F_INV(x):
    # choosing the specific function based on the domain
    if x<1/2 and x>0:
        return (np.log(2*x))
    return (np.log(0.5 * (1/(1-x))))

# defining the density functin of laplace distribution which shall be used for plotting the graph
def Fun(x):
    return 1/2 * np.exp(-np.abs(x))

# sampling the 100,000 uniformly distributed random variables
I =np.random.rand(1,100000)

# vectorizing the inverse function so that it can handle the array of number, instead of iterating through each number
vecF_INV = np.vectorize(F_INV);

# generating the required laplace distribution by passing the uniformly distributed sample into the inverse function
Required_Distribution= vecF_INV(I[0]);
# plotting the distribution in normalized fashion
plt.hist(Required_Distribution,bins = 120,density=True, label='Simulation',color = "red")

# generating the list of the numbers for plotting the graph
Xseq = np.linspace(-5,5,1000000)
#plotting the curve of density of function 
plt.plot(Xseq,Fun(Xseq),color="black")
plt.show()


