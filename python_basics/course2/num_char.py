# count the number of characters in a file
fileref = open("school_prompt2.txt", "r")
## other code here that refers to variable fileref
num_char = 0
for string in fileref:
    num_char += len(string)
fileref.close()

