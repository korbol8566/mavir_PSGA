# mavir optimization MVP
# fill-or-kill mfrr setting
# MAVIR xls import,
# "POSITIVE SUPPLY" SCENARIO
# todo: timestamped xls output

import pandas as pd  # Dataframes
from pulp import *  # Simplex
import uuid  # Unique ID in output file
import json  # pretty printing output dict

# xls data is read into pandas dataframes and sorted into list, which are then fed into the algorithm!
# a pandas dataframe is used to store xls data

demand_df = pd.read_excel('supply.xlsx', sheet_name='IB')  # todo: ezt meg kell csinálni rendes directory-ra
df = pd.read_excel('supply.xlsx', sheet_name='00')

# target demand is read into a pandas dataframe

supplyProductStartHour = 0
supplyProductEndHour = 1
supplyProductTime = "0{}:00-0{}:00.".format(supplyProductStartHour, supplyProductEndHour)

if supplyProductStartHour < 10 & supplyProductEndHour < 10:
    supplyProductTime = "0{}:00-0{}:00.".format(supplyProductStartHour, supplyProductEndHour)

if supplyProductStartHour < 10 & supplyProductEndHour >= 10:
    supplyProductTime = "0{}:00-{}:00.".format(supplyProductStartHour, supplyProductEndHour)

if supplyProductStartHour >= 10 & supplyProductEndHour >= 10:
    supplyProductTime = "{}:00-{}:00.".format(supplyProductStartHour, supplyProductEndHour)

targetDemand_with_nan = demand_df['SZUMMA'].tolist()
targetDemandList = [x for x in targetDemand_with_nan if str(x) != 'nan']
targetDemand = targetDemandList[0]
if targetDemand > 0:
    problemType = LpMinimize
    supplyDirection = "Negativ / Negative"
else:
    problemType = LpMaximize
    supplyDirection = "Pozitiv / Positive"

# vendor names are parsed out from filtered df's while handling autofilled nan values
afrr_df = \
    df[(df['Piac / Market'] == 'aFRR / aFRR')
       & (df['Irany / Direction'] == supplyDirection)
       & (df['Termek / Product'] == supplyProductTime)]

afrr_ids = afrr_df.index.astype(str).tolist()
afrr_df.insert(loc=0, column='row_id', value=afrr_ids)
afrr_df['Piac / Market'] = afrr_df['Piac / Market'] + afrr_df['row_id']
afrrVendors = afrr_df['Piac / Market'].tolist()


mfrr_df = \
    df[(df['Piac / Market'] == 'mFRR es RR / mFRR and RR')
       & (df['Irany / Direction'] == supplyDirection)
       & (df['Termek / Product'] == supplyProductTime)]

mfrr_ids = mfrr_df.index.astype(str).tolist()
mfrr_df.insert(loc=0, column='row_id', value=mfrr_ids)
mfrr_df['Piac / Market'] = mfrr_df['Piac / Market'] + mfrr_df['row_id']
mfrrVendors = mfrr_df['Piac / Market'].tolist()

# A dictionary of the costs of each of the Vendors is generated
# from the new df's filtered from the original df

afrrVendorCostsList = afrr_df['Energia ar / Energy Price [HUF/MWh]'].tolist()
mfrrVendorCostsList = mfrr_df['Energia ar / Energy Price [HUF/MWh]'].tolist()

afrrVendorCosts = dict(zip(afrrVendors, afrrVendorCostsList))
mfrrVendorCosts = dict(zip(mfrrVendors, mfrrVendorCostsList))

# A dictionary of the volumes of each of the Vendors is generated

afrrVendorVolumeList = afrr_df['Felajanlott mennyiseg / Offered Capacity [MW]'].tolist()
mfrrVendorVolumeList = mfrr_df['Felajanlott mennyiseg / Offered Capacity [MW]'].tolist()

afrrVendorVolumes = dict(zip(afrrVendors, afrrVendorVolumeList))
mfrrVendorVolumes = dict(zip(mfrrVendors, mfrrVendorVolumeList))

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The MAVIR MVP Optimization Problem", problemType)

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
prob += (lpSum(afrrVendorVars[i] for i in afrrVendors) + lpSum(mfrrVendorVars[i] for i in mfrrVendors)) <= targetDemand, "Demand"  # alá lövünk a dolognak, optimumban =, nem optimumban <

for i in afrrVendors:
    prob += afrrVendorVars[i] <= afrrVendorVolumes[i]

for j in mfrrVendors:
    prob += mfrrVendorVars[j] == mfrrVendorVolumes[j] * useMfrr[j]

# The problem is solved using PuLP's choice of Solver
prob.solve()

# we initialize a dict with to-be column names to gather output data
# (it's faster as opposed to appending to a df)
output_dict = {"Unique ID": [],
               "Időpont": [],
               "Kereslet (MW)": [],
               "Kínálat (HUF)": [],
               "Optimális eredmény?": [],
               "Piac": [],
               "Felhasznált volumen": [],
               "Ár": []}

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed and added to the output dict with it's resolved optimum value
for v in prob.variables():
    if v.varValue > 0:
        if v.name[0] != 'u':
            print(v.name, "=", v.varValue)
            output_dict["Unique ID"].append(str(uuid.uuid4()))
            output_dict["Időpont"].append(demand_df.at[0, 'Időpont'])  # todo: iterandus legyen
            output_dict["Kereslet (MW)"].append(targetDemand)
            output_dict["Kínálat (HUF)"].append(value(prob.objective))
            output_dict["Optimális eredmény?"].append(LpStatus[prob.status])
            output_dict["Piac"].append(v.name)
            output_dict["Felhasznált volumen"].append(v.varValue)
            output_dict['Ár'].append('PLACEHOLDER')  # todo: ide az kéne, hogy mennyibe került az egyes erőműből
            # cost*volume
            # todo: fura az output formázás, UTF 8 legyen

# the output_dict is converted into a df (due to performance reasons), with a timestamped name (format: yyyymmdd-HHMMSS)
# todo: bele lehetne tenni a névbe, hogy melyik ciklusig ment el (melyik dátumtól meddig)

print(json.dumps(output_dict, indent=2))
output_df = pd.DataFrame(output_dict).to_excel('MAVIR_PSGA_simplex_output_{}.xlsx'.format(pd.datetime.today().strftime('%Y%m%d-%H%M%S')))

# The optimised objective function value is printed to the screen
# print("Current Optimal Supply Cost = ", value(prob.objective))
