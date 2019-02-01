"""
Adapted from https://medium.freecodecamp.org/solving-a-google-interview-question-python-2-code-included-eddefcaeffb2


Given a string, delete any reoccuring characters. 

aabbcc -> abc

"""

def delete_reoccurring_char(string):
    # hash sets have O(1) lookup runtime complexity
    chars = set()
    ret = '' # O(n) space complexity
    for c in string: #O(n) complexity
        if c not in chars:
            chars.add(c) # union operation 
            ret+=c
    return ret
    

