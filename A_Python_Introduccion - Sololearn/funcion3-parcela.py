import random


def profitable(d1, d2):
  area = d1 * d2
  invest = area > 700
  return invest

buy = profitable(90, 120)
print(buy)


print("")
print("-------------------------------")
print("")


d1 = int(input("largo->"))
d2 = int(input("ancho->"))

def profitable(d1, d2):
  area = d1 * d2
  invest = area > 700
  return invest

buy = profitable(d1, d2)
print(buy)


print("")
print("-------------------------------")
print("")