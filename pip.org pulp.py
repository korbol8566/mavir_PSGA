# from pulp import *
#
# x = LpVariable("x", 0, 3)  # 0 <= x <= 3
# y = LpVariable("y", 0, 1)  # 0 <= y <= 1
# prob = LpProblem("myProblem", LpMinimize)
# prob += x + y <= 2
# prob += -4*x + y
# status = prob.solve()
# print(LpStatus[status])
# print(value(x))
# print(value(y))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# empty_list = []
# for n in numbers:
#     empty_list.append(n)
# print(empty_list)

new_list = [n*n for n in numbers]
print(new_list)