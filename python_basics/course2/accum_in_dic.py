# accumulate in dictionary all the appearance of the 
f = open('scarlet.txt', 'r')
txt = f.read()

x = {}

for c in x:
    if c not in x:
        x[c] = 0
    x[c] = x[c] + 1

print("t: " + str(['t']) + " occurrences")


# Provided is a string saved to the variable name sentence. Split the string into the list
# of words, then create a dictionary that contains each word and the number of times it 
# occurs. Save the dictionary in the variable words_counts.

sentence = "The dog chases the rabbit into ..."

words = sentence.split()
word_counts = {}

for word in words:
    if word not in words_counts:
        words_counts[word] = 0
    words_counts[word] = words_counts[word] + 1


# create the dictionary called char_d from the stri, so that the key is a charcter and 
# the value is how many times it occurs

stri = "what can I do"

char_d = {}

for c in stri:
    if c is not in char_d:
        char_d[c] = 0
    char_d[c] = char_d[c] + 1
