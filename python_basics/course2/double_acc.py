# just an accumulator to count and then max or min coun of appearance or something

product = "iphone is and android phones"

lett_d = {}

for c in product:
    if c not in lett_d:
        lett_d[c] = 0
    lett_d[c] = lett_d[c] + 1
print(lett_d)

keys = list(lett_d.keys())

max_value = keys[0]
for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key

