# For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

ing=[]
for i in range(len(verbs)):
   ing.append(verbs[i]+"ing")
print(ing)

# Given the list of numbers, numbs, modifiy the list numbs so that each of the original numbers are increased by 5. Note this is not an accumulator pattern problem, but its a good review.
numbs = [5, 10, 15, 20, 25]

for i in range(len(numbs)):
   numbs[i] = numbs[i]+5
