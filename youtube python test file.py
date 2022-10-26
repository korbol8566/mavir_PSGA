from pulp import *

# Lists
FOODS = ['OATS', 'CHICKEN', 'EGGS', 'MILK']
CUSTOMER = [1, 2, 3, 4, 5]
FACILITY = ['FAC 1, FAC 2, FAC 3']

# dict
demand = {1: 80, 2: 270, 3: 250, 4: 160, 5: 180}
maxAmount = {'FAC 1': 500, 'FAC 2': 500, 'FAC 3': 500}
transportationCost = {'FAC 1': {1: 4, 2: 5, 3: 6, 4: 8, 5: 10},
                      'FAC 2': {1: 6, 2: 4, 3: 3, 4: 5, 5: 8},
                      'FAC 3': {1: 9, 2: 7, 3: 4, 4: 3, 5: 4}}

# SETTING THE PROBLEM VARIABLE
problem = LpProblem('FacilityLocation', LpMinimize)

# SETTING DECISION VARIABLES

# binary decision variable
use_variables = LpVariable.dicts('UseLocation', FACILITY, 0, 1, LpBinary)
# integer decision variable
service_variables = LpVariable.dicts('Service', [(i, j) for i in CUSTOMER, for j in FACILITY], 0)
# more variables
food_variables = LpVariable.dicts('Food', FOODS, 0)
