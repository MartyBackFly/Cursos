from aafuncionimprimir import espacio as aa



# lista

x = ['hi', 'hello', 'welcome']
print(x[2])


aa()


# diccionario 


ages = {
   "Dave": 24,
   "Mary": 42,
   "John": 58
}
print(ages["Dave"])
print(ages["Mary"])


aa()

car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}


a = input("brand, year, color, mileage : --> ")

print(car[a])


aa()


nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)