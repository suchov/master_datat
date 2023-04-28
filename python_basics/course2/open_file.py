#the best way to work with the file to not forget to close it

with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
# continue on with other code


fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4


# I'm a bit confused, but previous example deffinitely not so good for the iteration over
# over the large data, not sure about this one
with open(fname, 'r') as fileref:
 for lin in fileref:
     ## some code that uses line as the current line of the file
     ## some more code
