from pulp import *  # import pulp to do LP stuff on imported xls

# create the list of vendors
Vendors = ["1", "2", "3"]

# A dictionary of the costs of each of the Vendors is created
costs = {1: 95, 2: 110, 3: 120}

# A dictionary of the volumes of each of the Vendors is created
volumes = {1: 12, 2: 34, 3: 24}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Test problem with dict inputs", LpMinimize)

# A dictionary called 'vendor_vars' is created to contain the referenced Variables
vendor_vars = LpVariable.dict("Vend", Vendors, 0)

# The objective function is added to 'prob' first
prob += (
    lpSum([costs[i] * vendor_vars[i] for i in Vendors]),
    "Total cost to satisfy demand",
)

# The four constraints are added to 'prob'
prob += lpSum([vendor_vars[i] for i in Vendors]) == 50, "DemandSum"
prob += (
    lpSum([volumes[i] for i in Vendors]) <= volumes[],
    "VolumeConstraint",
)
# prob += x1 <= sellers[0, 'volume']
# prob += x2 <= sellers[1, 'volume']
# prob += x3 <= sellers[2, 'volume']

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total cost to satisfy demand: ", value(prob.objective))
