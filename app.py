import pandas as pd
import pulp

df = pd.read_excel("supply.xlsx")
print(df)

prob = pulp.LpProblem("myProblem", pulp.LpMinimize)

#sdfasd fasd f


# Minimize totalCost subject to
# totalPurchased = totalDemand
# purchaseCost <= sumDemandValue
