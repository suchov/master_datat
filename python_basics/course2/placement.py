# 1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

#d is a dictionary of characters and accociated count
d = {}

for letter in placement:
    if letter not in d:
        d[letter] = 0
    d[letter] = d[letter] + 1

ks = d.keys()
# min_value is a variable that contains the lowest value in the dictionary
min_value = list(ks)[0]
for k in ks:
    if d[min_value] > d[k]:
        min_value = k
print(min_value)
