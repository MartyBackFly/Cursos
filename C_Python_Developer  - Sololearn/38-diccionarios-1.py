from aafuncionimprimir import espacio 

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print(6 in nums)
print("three" in nums)
print(4 not in nums)

espacio()


## GET GET GET GET GET GET GET GET GET GET 


pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12, 42))
print(pairs.get(1, 42))
print(pairs.get(13, "el 13 no esta culiao"))
print(pairs.get(12345, "not found"))


espacio()


fib = {1: 1, 2: 1, 3: 2, 4: 3}

print(fib.get(4, 0) + fib.get(7, 5))