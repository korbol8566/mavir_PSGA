# from pulp import *
#
# problemType = LpMaximize
# prob = LpProblem("The Basic Supply Problem", problemType)
#
# vendor1 = LpVariable("vendor1", 0, 10, LpInteger)
# vendor2 = LpVariable("vendor2", 0, 34, LpInteger)
# vendor3 = LpVariable("vendor3", 0, 24, LpInteger)
#
# prob += -100 * vendor1 + -110 * vendor2 + -120 * vendor3, "Current Optimal Supply Cost"
# prob += vendor1 + vendor2 + vendor3 == 54, "Demand"
#
# prob.solve()
#
# print("Status:", LpStatus[prob.status])
#
# for v in prob.variables():
#     print(v.name, "=", v.varValue)
#
# print("Current Optimal Supply Cost = ", value(prob.objective))



# print("Start")
# mainCounter = 0
# subCounter = 0
# while mainCounter < 10:
#     print("Main Counter = ", mainCounter)
#     while subCounter < 4:
#         print("Sub Counter = ", subCounter)
#         subCounter += 1
#     subCounter = 0
#     mainCounter += 1
#
#
# print("End")

# import pandas as pd
#
# supplyProductTime = '00:00-01:00'
#
# df = pd.read_csv(r'E:\Tulajdonos\Desktop\Tomasz diplomamunka\Új inputadatok\_ajánlatok\test\AnonimRiport_20210101_0.csv')
# afrr_df = \
#     df[(df['Piac / Market'] == 'aFRR / aFRR')
#        & (df['Irany / Direction'] == supplyDirection)
#        & (df['Termek / Product'] == supplyProductTime)]
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(df[['Termek / Product', 'Piac / Market', 'Felajanlott mennyiseg / Offered Capacity [MW]']])

x = -123
y = -1 * x
print(x, y)
