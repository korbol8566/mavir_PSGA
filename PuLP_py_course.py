# The following code demonstrates a list with strings

# ingredientlist = ["Rice", "Water", "Jelly"]
# for i in ingredientlist:
#     print(i)
# print("No longer in the loop")



# i = 3
# while i <= 15:
#     # some commands
#     print(i)
#     i = i + 1 # a command that will eventually end the loop is naturally required
# # other commands after while loop


# costs = {"CHICKEN": 1.3, "BEEF": 0.8, "MUTTON": 12}
# print("Cost of Meats: ")
# for i in costs:
#     print(i)
#     print(costs[i])

# prime_numbers = [i for i in range(100) if (i % 2 != 0 and
#                                            i % 3 != 0 and
#                                            i % 4 != 0 and
#                                            i % 5 != 0 and
#                                            i % 6 != 0 and
#                                            i % 7 != 0 and
#                                            i % 8 != 0 and
#                                            i % 9 != 0)]
# print(prime_numbers)

class Pattern:
    """Information on a specific pattern in the SpongeRoll Problem"""
    cost = 1
    trimValue = 0.04
    totalRollLength = 20
    lengthOptions = [5, 7, 9]


def __init__(self, name, lengths = None):
    self.name = name
    self.lengthsdictionary = dict(zip(self.lenghtOptions, lengths))


def __str__(self):
    return self.name


def trim(self):
    return Pattern.totalRollLength - sum([int(i)*self.lengthsdictionary[i] for i in self.lengthsdictionary])
