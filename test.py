import re
xx = "guru99, education is fun"
r1 = re.findall(r"^[a-z0-9, ]+",xx)
print(r1)