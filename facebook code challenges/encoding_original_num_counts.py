"""
Adapted from https://www.youtube.com/watch?v=qli-JCrSwuk which came from daily coding problems blog. 

Problem:

Say you have a encoding scheme for every letter in the alphabet like:
    
    a -> 1
    b -> 2
    c -> 3
    ...
    z -> 26

Find a way to count the number of ways a decoded value could have originally come from. 

For example if "12" is entered, there should be an answer of 2 returned 

ab -> 12
l -> 12

"""

def num_ways(enc):
    """this function wil determine all the number of original values that an encoded
    phrase could have come from. 
    
    Args:
        enc: str representing the encoded phrase
    Returns:
        num: int representing the number of original value choices
        
        
    """
    count=len(enc)
    for i in range(0, len(enc)):
        if int(enc[i:i+2])<26:
            count+=1        
    return count
        
        
    
    
