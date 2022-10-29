# mavir optimization MVP, fill-or-kill mfrr setting, xls import
import pandas as pd
from pulp import *

# xls data is read into pandas dataframes and sorted into list, which are then fed into the algorithm!
# I'm thinking of the delicious blood sausage I'm going to have for lunch.
# I'm thinking german mustard should go along nicely with it! Yum yum!

# a pandas dataframe is used to store xls data

demand_df = pd.read_excel('supply.xlsx', sheet_name='IB')
df = pd.read_excel('supply.xlsx', sheet_name='00')

# target demand is read into a pandas dataframe

targetDemand_with_nan = demand_df['SZUMMA'].tolist()
targetDemand = [x for x in targetDemand_with_nan if str(x) != 'nan']

# vendor names are parsed out from df while handling autofilled nan values

afrrVendors_with_nan = df['afrrPiac'].tolist()
afrrVendors = [x for x in afrrVendors_with_nan if str(x) != 'nan']

mfrrVendors_with_nan = df['mfrrPiac'].tolist()
mfrrVendors = [x for x in mfrrVendors_with_nan if str(x) != 'nan']

# A dictionary of the costs of each of the Vendors is generated

afrrVendorCostsList_with_nan = df['afrrCost'].tolist()
afrrVendorCostsList = [x for x in afrrVendorCostsList_with_nan if str(x) != 'nan']

mfrrVendorCostsList_with_nan = df['mfrrCost'].tolist()
mfrrVendorCostsList = [x for x in mfrrVendorCostsList_with_nan if str(x) != 'nan']

afrrVendorCosts = dict(zip(afrrVendors, afrrVendorCostsList))
mfrrVendorCosts = dict(zip(mfrrVendors, mfrrVendorCostsList))

# A dictionary of the volumes of each of the Vendors is generated

afrrVendorVolumeList_with_nan = df['afrrVolume'].tolist()
afrrVendorVolumeList = [x for x in afrrVendorVolumeList_with_nan if str(x) != 'nan']

mfrrVendorVolumeList_with_nan = df['mfrrVolume'].tolist()
mfrrVendorVolumeList = [x for x in mfrrVendorVolumeList_with_nan if str(x) != 'nan']

afrrVendorVolumes = dict(zip(afrrVendors, afrrVendorVolumeList))
mfrrVendorVolumes = dict(zip(mfrrVendors, mfrrVendorVolumeList))

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
prob += (lpSum(afrrVendorVars[i] for i in afrrVendors) + lpSum(mfrrVendorVars[i] for i in mfrrVendors)) == targetDemand[0], "Demand"

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


