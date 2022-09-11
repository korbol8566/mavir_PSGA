# import pandas to handle xls import
#import pandas as pd

# import pulp to do LP stuff on imported xls
import pulp as pl

# import supply.xls from current directory into a pandas dataframe
from pulp import LpInteger

#df = pd.read_excel("supply.xlsx")
#print(df)

# target problem: buy 50 units for the lowest price possible
prob = pl.LpProblem("Test problem to see if this could even work", pl.LpMinimize)

# Create the necessary vars, in this case the 3 sellers
# args: pl.LpVariable("arbitrary name", lower bound, upper bound, type)

x1 = pl.LpVariable("seller1", 0, 12, LpInteger)
x2 = pl.LpVariable("seller2", 0, 34, LpInteger)
x3 = pl.LpVariable("seller3", 0, 24, LpInteger)

# create prob as problem data datatype to store functions, constraints and other necessary stuff
# and a custom string to explain the target function

prob += 95 * x1 + 110 * x2 + 120 * x3, "Total cost to satisfy current demand"

# demand will be a user input data among others, when I get to it eventually
# but who knows in today's godforsaken economy for crying out loud

# demand = ???

# adding necessary constraints to prob

# 50 is an arbitrary value, must be replaced with a variable
prob += x1 + x2 + x3 == 50
prob += x1 <= 12
prob += x2 <= 34
prob += x3 <= 24

# The problem data is written to an .lp file
prob.writeLP("sellers.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total cost to satisfy current demand = ", pl.value(prob.objective))

# Minimize totalCost subject to
# totalPurchased = totalDemand
# purchaseCost <= sumDemandValue
