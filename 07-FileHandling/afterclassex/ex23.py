import re
medium = 0
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
for temp in temperatures:
    temp = int(temp)
    medium = medium + temp

print("Medium temp:", medium/len(temperatures))