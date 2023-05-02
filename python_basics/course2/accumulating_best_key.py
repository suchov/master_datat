# Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
# initialize variable best_key_so_far to be the first key in d
best_key_so_far = list(ks)[0] 

for k in ks:
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far
    if d[best_key_so_far] > d[k]:
        best_key_so_far = k
print("key " + str(best_key_so_far) + " has the highest value, " + str(d[best_key_so_far]))

