# solucion pagina  https://www.hackingnote.com/en/python-challenge-solutions/level-10/index.html
 

import re
re.findall("(\\d)(\\1*)", "111221")
[('1', '11'), ('2', '2'), ('1', '')]


x = "1"
for n in range(30):
    x="".join([str(len(j) + 1)+i for i, j in re.findall(r"(\d)(\1*)", x)])
print(len(x))