
length = int(input("length--->"))
width = int(input("width--->"))

def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter #2 valores
  
x, y = rect(length, width) #2 variables

print(x, y)
