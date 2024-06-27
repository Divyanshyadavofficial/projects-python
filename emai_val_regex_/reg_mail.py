import re
pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
mail = input("enter the mail ")
if re.search(pattern,mail):
    print("right email ")
else:
    print("wrong email ")
