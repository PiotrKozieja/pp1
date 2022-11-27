import re
end = []
text = "To be, or not to be, that is the question"

x = re.findall("[AaEeOoIiUuYy]",text)
print(len(x))

