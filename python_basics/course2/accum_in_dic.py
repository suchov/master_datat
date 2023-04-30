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

# exercise - accumulating accurances in dictionary with the number of accurances
f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

# Write a loop that prints the letters and their counts
for key in letter_counts:
    print(key + ": " + str(letter_counts[key]) + " occurrences")



# or the number of words in dictionary that appeard in sentance 
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

sentence_list = sentence.split()

word_counts = {}

for word in sentence_list:
    if word not in word_counts:
        word_counts[word] = 0

    word_counts[word] = word_counts[word] + 1
