# CISC455
# The optimal delivery route for delivery personnel
  This is a Python program that uses genetic algorithms to solve and Vehicle Routing Problem (VRP).
  
## Problem Description
  The vehicle routing problem is a combinatorial optimization problem, which requires that a certain number of customers be assigned the optimal delivery/receipt routes to minimize the total travel distance. This program solves for ordered VRP (VRP with time windows).
  
## Program Structure
Our code is divided into two modules. The inner module provides settable distances and functions for the route module and the main function for the outer module;
1. main.py(routemain.py)：Running genetic algorithms in the main() function; Order generation: in create_ Generate stores and orders in the orders() class.
2. initialization.py(Routeinitialization.py): Initialize population
3. evaluation. py(Routeevaluation.py): calculate the fitness value of an individual
4. parent_ Selection.py(routeparent_ Selection.py): Select parents for cross operation
5. recombination.py(Routerecombination.py):Implementing cross operations
6. mutation.py(Routemutation.py): Implementing mutation operations
7. survivor_ Selection.py(routesurvivor_ Selection.py): Select a new generation of individuals

## Using method
1. Firstly, ensure that the required dependency libraries are installed: math, random, and numpy.
2. Place the code files in the same directory.
3. Import VRPSolver into the code and create a solver instance.
4. Define the problem, including order list, route history, route restructuring, and survivor selection methods.
5. Use the method to solve the problem and obtain the results.

## Genetic algorithm parameters
The following are the main parameters of genetic algorithm:
  1. pop_ Size: Population size
  2. mating_ pool_ Size: mating pool size
  3. tournament_ Size: The size of the tournament selection
  4. xover_ Rate: Cross probability
  5. mut_ Rate: probability of variation
  6. gen_ Limit: maximum number of iterations
In the main() & routemain() function, different parameter combinations can be attempted to find the best solution. In addition, different search strategies can be attempted by modifying the selection, crossover, and mutation strategies of genetic algorithms, as well as survivor selection strategies.

## Result analysis
After the program runs, the best fitness and average fitness of each generation will be output, and the roadmap of the optimal solution will be drawn. By analyzing these results, we can understand the performance of genetic algorithms in problem-solving, as well as the effectiveness of selection, crossover, and mutation strategies.
