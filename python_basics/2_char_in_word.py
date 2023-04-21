#Write code that counts the number of words in sentence that contain either an “a” or an “e”.
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
# number of words that contains either "a" of "e"
num_a_or_e = 0
# sentance in array to iterate
sentence_arr = sentence.split()

#ierate with condition and accamulate
for item in sentence_arr:
    if "a" in item or "e" in item:
        num_a_or_e += 1


