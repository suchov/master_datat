
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(words):
    new_word = ""
    for w in words:
        if w not in punctuation_chars:
            new_word = new_word + w
    return new_word

def get_pos(sentence):
    '''takes a string and calculates how many words in it
    considered positive using positive_words list returns
    a positive integer'''
    new_sentence = strip_punctuation(sentence).lower().split()
    positive_count = 0
    for word in new_sentence:
        if word in positive_words:
            positive_count = positive_count + 1
    return positive_count

def get_neg(sentence):
    '''takes a string and calculates how many words in it
    considered negative using positive_words list returns
    a positive integer'''
    new_sentence = strip_punctuation(sentence).lower().split()
    negative_count = 0
    for word in new_sentence:
        if word in negative_words:
            negative_count = negative_count + 1
    return negative_count

# open the files and write for read and write 
projectTwitterDataFile = open("project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")
def writeInDataFile(resultingDataFile):
    ''' method reading and writing to the file result data'''
    # write the header
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    # read the twitter data file in lines
    linesPTDF =  projectTwitterDataFile.readlines()
    # remove header
    headerDontUsed= linesPTDF.pop(0)
    # for each line it the file write it down in the right format  
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")

writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()
