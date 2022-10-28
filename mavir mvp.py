# mavir optimization MVP, fill-or-kill mfrr setting

from pulp import *

afrrVendors = ["afrr1",
               "afrr2",
               "afrr3",
               "afrr4",
               "afrr5",
               "afrr6",
               "afrr7",
               "afrr8"]

mfrrVendors = ["mfrr1",
               "mfrr1",
               "mfrr2",
               "mfrr3",
               "mfrr4",
               "mfrr5",
               "mfrr6",
               "mfrr7",
               "mfrr8",
               "mfrr9",
               "mfrr10",
               "mfrr11",
               "mfrr12",
               "mfrr13"]

# A dictionary of the costs of each of the Vendors is created

afrrVendorCosts = {"afrr1": 100000,
                   "afrr2": 122322,
                   "afrr3": 218978,
                   "afrr4": 254652,
                   "afrr5": 257130,
                   "afrr6": 260000,
                   "afrr7": 260000,
                   "afrr8": 260000}

mfrrVendorCosts = {"mfrr1": 145000,
                   "mfrr2": 157000,
                   "mfrr3": 159000,
                   "mfrr4": 160000,
                   "mfrr5": 161997,
                   "mfrr6": 161998,
                   "mfrr7": 161999,
                   "mfrr8": 162000,
                   "mfrr9": 162000,
                   "mfrr10": 162000,
                   "mfrr11": 162000,
                   "mfrr12": 162000,
                   "mfrr13": 162000}


afrrVendorVolumes = {"afrr1": 24,
                     "afrr2": 90,
                     "afrr3": 50,
                     "afrr4": 33,
                     "afrr5": 35,
                     "afrr6": 5,
                     "afrr7": 5,
                     "afrr8": 25}

mfrrVendorVolumes = {"mfrr1": 25,
                     "mfrr2": 28,
                     "mfrr3": 171,
                     "mfrr4": 153,
                     "mfrr5": 155,
                     "mfrr6": 57,
                     "mfrr7": 57,
                     "mfrr8": 120,
                     "mfrr9": 10,
                     "mfrr10": 11,
                     "mfrr11": 31,
                     "mfrr12": 32,
                     "mfrr13": 162}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The MAVIR MVP Optimization Problem", LpMinimize)

# A dict called 'vendor_vars' is created to contain the referenced Variables, with lower bounds of 0
afrrVendorVars = LpVariable.dicts("afrrVendor", afrrVendors, 0)
mfrrVendorVars = LpVariable.dicts("mfrrVendor", mfrrVendors, 0)
useMfrr = LpVariable.dicts("useMfrr", mfrrVendors, 0, 1, LpBinary)

# The objective function is added to 'prob' first
prob += (
    lpSum([afrrVendorCosts[i] * afrrVendorVars[i] for i in afrrVendors]) + lpSum([mfrrVendorCosts[i] * mfrrVendorVars[i] for i in mfrrVendors]),
    "Optimal Cost to Fill Supply",
)
# The  constraints are added to 'prob'
prob += (lpSum(afrrVendorVars[i] for i in afrrVendors) + lpSum(mfrrVendorVars[i] for i in mfrrVendors)) == 125.427, "Demand"

for i in afrrVendors:
    prob += afrrVendorVars[i] <= afrrVendorVolumes[i]

for j in mfrrVendors:
    prob += mfrrVendorVars[j] == mfrrVendorVolumes[j] * useMfrr[j]

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Current Optimal Supply Cost = ", value(prob.objective))


