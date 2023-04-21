# For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for string in words:
    if string[-1] == "e":
        string = string + "d"
        past_tense.append(string)
    else:
        string = string + "ed"
        past_tense.append(string)
