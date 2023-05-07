# the accumulation functions number of elements and the sum of elements 

def total(l):
    '''count the total of elements in the list'''
    tot = 0
    for each in l:
        tot = tot + each
    return tot


def count(n):
    '''count the number of elements in a list'''
    c = 0 # initialize count variable to 0
    for _ in n:
        c = c + 1   # increment the counter for each item in seq
    return c
