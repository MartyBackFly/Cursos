import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]

matches = re.finditer("[^A-Z]+([A-Z]{3})([a-z])([A-Z]{3})[^A-Z]+", data)

for match in matches:
    print(f"{match.group(1)}, {match.group(2)}, {match.group(3)}")
