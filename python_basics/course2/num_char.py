# count the number of characters in a file
fileref = open("school_prompt2.txt", "r")
## other code here that refers to variable fileref
num_char = 0
for string in fileref:
    num_char += len(string)
fileref.close()

# count the number of lines in file
fileref = open("travel_plans2.txt", "r")
## other code here that refers to variable fileref
file_lines = fileref.readlines()
num_lines = 0
for string in fileref:
    num_lines += 1
fileref.close()

# read through the file and print the propper programmer way
olypmicsfile = open("olypmics.txt", "r")

for aline in olypmicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()

# count the number of lines in a file 
olypmicsfile = open("emotion_words.txt", "r")

num_lines = 0
for aline in olypmicsfile:
    num_lines += 1
    
olypmicsfile.close()

