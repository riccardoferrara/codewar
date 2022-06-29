# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

import math

def rot13(m):
    print(m)
    encoded = ''.join(map(getLetterAfter13Letters, list(m)))
    return encoded

def getLetterAfter13Letters(l):
    print(l)
    islower = l.islower()
    l = l.lower()
    alph_l_n = {chr(i+96):i for i in range(1,27)}
    if l not in alph_l_n:
        return l
    pos = alph_l_n[l] + 13 
    pos -= math.floor(pos / len(alph_l_n))*len(alph_l_n)
    alph_n_l = {v: k for k, v in alph_l_n.items()}
    return alph_n_l[pos] if islower else alph_n_l[pos].upper()




# print(rot13("test")) # "grfg")
# print(rot13("Test")) # "Grfg")
# print(rot13("Avoid success at all costs!")) # "Grfg")
print(rot13("abcdefghijklmnopqrstuvwxyz")) # "Grfg")



