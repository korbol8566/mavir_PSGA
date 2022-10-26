# basic supply simplex script based on the supply xls
from PIL.EpsImagePlugin import binary
from pulp import *

# # Create the 'prob' variable to contain the problem data
# prob = LpProblem("The Basic Supply Problem", LpMinimize)
#
# # Variables are added (with a lower limit of 0):
# # variable_name = LpVariable("arbitrary name", lower bound, upper bound,datatype)
# vendor1 = LpVariable("vendor1", 0, 12, LpInteger)
# vendor2 = LpVariable("vendor2", 0, 34, LpInteger)
# vendor3 = LpVariable("vendor3", 0, 24, LpInteger)
#
# # The objective function is added to 'prob' first (cost * vendor)
# prob += 95 * vendor1 + 110 * vendor2 + 120 * vendor3, "Current Optimal Supply Cost"
#
# # The  constraints are entered (supply must equal demand = 50)
# prob += vendor1 + vendor2 + vendor3 == 50, "Demand"
#
# # The problem is solved using PuLP's choice of Solver
# prob.solve()
#
# # The status of the solution is printed to the screen
# print("Status:", LpStatus[prob.status])
#
# # Each of the variables is printed with it's resolved optimum value
# for v in prob.variables():
#     print(v.name, "=", v.varValue)
#
# # The optimised objective function value is printed to the screen
# print("Current Optimal Supply Cost = ", value(prob.objective))

# todo: user input demand
# todo:
# todo:
# todo:

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Basic Supply Problem", LpMinimize)

# Variables are added (with a lower limit of 0):
# variable_name = LpVariable("arbitrary name", lower bound, upper bound,datatype)
vendor1 = LpVariable("vendor1", 0, 10, LpInteger)
vendor2 = LpVariable("vendor2", 0, 34, LpInteger)
vendor3 = LpVariable("vendor3", 0, 24, LpInteger)

# The objective function is added to 'prob' first (cost * vendor)
prob += 5 * vendor1 + 110 * vendor2 + 120 * vendor3, "Current Optimal Supply Cost"

# The  constraints are entered (supply must equal demand = 50)
prob += vendor1 + vendor2 + vendor3 == 50, "Demand"

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Current Optimal Supply Cost = ", value(prob.objective))