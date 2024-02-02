import numpy as np
import matplotlib.pyplot as plt


# taking inputs from the user about the number of points and limits
n = int (input("enter the number of points : "))
xI = int(input("enter the limit starting point: "))
xF = int(input("enter the limit ending point: "))


# sampling the points from the uniform distribution and scaling them according to the limits, making limits dynamic
x = xI + 2*xF*np.random.rand(1, n)
y = xI + 2*xF*np.random.rand(1, n)


# defining the required experssion as a function so to make later calculations for graphing
def fun(x):
    return x * np.sin(1/x)

# checking if each point lie between curve and the x axis keeping in mind that curve might be above or below the axis, 
# creating another array in which value is assigned 1 if point lie in "interested" area and zero else wise. lastly calculated the sum using np.sum /
# divided by total number and multiplied it by four.
approximation =4 * np.sum(np.where((fun(x) >= 0) & (y <= fun(x)) & (y >= 0) | (fun(x) < 0) & (y > fun(x)) & (y <= 0), 1, 0)) / n 

# here we are plotting the points
# using the same condition as used above to assign different colors to the points
plt.plot(x[((fun(x) >= 0) & (y <= fun(x)) & (y >= 0) | (fun(x) < 0) & (y > fun(x)) & (y <= 0))], y[((fun(x) >= 0) & (y <= fun(x)) & (y >= 0) | (fun(x) < 0) & (y > fun(x)) & (y <= 0))], '.', color=[0.3, 0.7, 0.5], markersize=4)
plt.plot(x[~((fun(x) >= 0) & (y <= fun(x)) & (y >= 0) | (fun(x) < 0) & (y > fun(x)) & (y <= 0))], y[~((fun(x) >= 0) & (y <= fun(x)) & (y >= 0) | (fun(x) < 0) & (y > fun(x)) & (y <= 0))],'.', color=[0.7, 0.5, 0.3], markersize=4)

# plotting the curve here
# generating a list of evenly spaced points
t = np.linspace(-1,1,100000)

# plotting the t points and outcomes in x and y axis respectively
plt.plot(t,fun(t), linewidth=2, color=[0.1, 0.3, 0.5])
plt.axis('equal')
plt.title(label = f'area ~ {approximation} with n = {n}')
plt.show()




