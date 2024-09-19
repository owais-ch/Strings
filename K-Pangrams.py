'''
K-Pangrams (GFG)

Given a string str and an integer k, return true if the string can be changed into a pangram after at most k operations, else return false.

A single operation consists of swapping an existing alphabetic character with any other lowercase alphabetic character.

Note - A pangram is a sentence containing every letter in the english alphabet.

Examples :

Input: str = "the quick brown fox jumps over the lazy dog", k = 0
Output: true
Explanation: the sentence contains all 26 characters and is already a pangram.
'''

from collections import Counter

class Solution:
    def kPangram(self,string, k):
        length=len(string)
        string=string.replace(" ","")
        dict1=Counter(string)
        
        num_char=len(dict1)
        if num_char==26:
            return True
            
        possible=len(string)-num_char
        #print("dict1= ",dict1,"possible=",possible,26-num_char)
        if 26-num_char<=possible and 26-num_char<=k:
            return True
            
        return False
        
