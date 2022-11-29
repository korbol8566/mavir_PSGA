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

# overallCounter = 0
# lower = 0
# upper = 1
#
# while overallCounter < 101:
#     if overallCounter % 4 == 0:
#         if overallCounter != 0:
#             lower += 1
#             upper += 1
#     if overallCounter % 96 == 0:
#         print("New file beby!")
#         lower = 0
#         upper = 1
#     print(overallCounter, lower, upper)
#     overallCounter += 1


# x = "2021.05.05 05:15:00 +0200"
#
# supplyProductStartHour = int(x[11:13])
# supplyProductTime = "{}:00-{}:00".format(supplyProductStartHour - 1, supplyProductStartHour)
#
#
# print(supplyProductTime)

# 0 0 1
# 1 0 1
# 2 0 1
# 3 0 1
# 4 1 2
# ...
# import datetime
#
# date = datetime.datetime(2021,1,1)
# date += datetime.timedelta(days=1)


# x = 'mfrrVendor_mFRR_es_RR___mFRR_and_RR1423562345634567'
# x_num = x[x.index("___") + 14:]
# print(x_num)




# supplyProductTime = '00:00-01:00'
#
# df = pd.read_csv(r'E:\Tulajdonos\Desktop\Tomasz diplomamunka\Új inputadatok\_ajánlatok\test\AnonimRiport_20210101_0.csv')
# afrr_df = \
#     df[(df['Piac / Market'] == 'aFRR / aFRR')
#        & (df['Irany / Direction'] == supplyDirection)
#        & (df['Termek / Product'] == supplyProductTime)]
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(df[['Termek / Product', 'Piac / Market', 'Felajanlott mennyiseg / Offered Capacity [MW]']])

x = "2021.01.01 00:15:00 +0100"
aktualisDatum = x[:10]

print(aktualisDatum)

# import os
#
# directory_in_str = r'E:\Tulajdonos\Desktop\Tomasz diplomamunka\Új inputadatok\_ajánlatok\test'
#
# file_dict = {} # Create an empty dict
#
# directory = os.fsencode(directory_in_str)
#
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     if filename.endswith(".txt"):
#         print(filename)
#         continue
#     else:
#         continue



