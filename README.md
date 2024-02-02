# Simulations
## Monte Carlo Integration
Monte Carlo Integration is one of methods used to find the definite integrals numerically. In the
this program we calculate the area of a sample function using this method.
The sample function is x sin(1/x) whose integral is calculated from -1 to 1.
Following were the key steps involved in the calculation:
1. Sampled the n number of points from a uniform random distribution.
2. Imagined a square of area 4 units starting from (-1,-1) to (1,1) so that it inscribies the
required portion of the graph.
3. Examined each point to see if it lies between the curve of function and x-axis or not and
marked their counts.
4. Calculated the ratio of points lying in the “interested” area to the total points.
5. Estimated the required integral by multiplying the total area with this ratio.
![alt text](https://github.com/hasib2003/MonteCarloI-RandomWalks/blob/main/monteCarlo.png?raw=true)
## Random Walks
Random walks are generated when we randomly take steps. At each step we either go right
with 0.5 probability or to left with the same, this is the randomness in one dimension. Similarly
we can add randomness to the second dimension by taking the same above step but with
another 0.5 probability of going up and 0.5 probability of going down. If we have more
dimensions we can scale the process accordingly.
Here are the key steps used to simulate Random Walks.
- For each step of each walk in each direction we sampled uniformly distributed random
points, that corresponds to the probability on each step.
- Next we simply started to move from origin according to the sampled points. For
example, if the array for horizontal motion has the first value 0.6 we move to right on our
first step (since 0.6 > 0.5) and to left in the other case. Same is the case for vertical
motion at each step.
![alt text](https://github.com/hasib2003/MonteCarloI-RandomWalks/blob/main/walks.png?raw=true)

