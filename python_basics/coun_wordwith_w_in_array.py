#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
#contains the number of words that contains "w"
acc_num = 0

for item in items:
    if "w" in item:
        acc_num = acc_num + 1

