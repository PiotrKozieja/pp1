import re
wzor = [" "]
end = []
text = "To be, or not to be, that is the question"
for i in range(len(wzor)):
    x = re.findall(wzor[i],text)
    for j in x:
        end.append(j)
lenght = len(end)+1
print(lenght)