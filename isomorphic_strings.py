'''
Isomorphic Strings (GFG)

Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.

If the characters in str1 can be changed to get str2, then two strings, str1 and str2, are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.

Example 1:

Input:
str1 = aab
str2 = xxy
Output: 
1
Explanation: 
There are two different characters in aab and xxy, i.e a and b with frequency 2 and 1 respectively.
'''
from collections import Counter

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        dict1=dict()
        dict2=dict()
        
        length1=len(str1)
        length2=len(str2)
        
        if length1!=length2:
            return 0
            
        for i in range(length1):
            if str1[i] not in dict1:
                dict1[str1[i]]=str2[i]
            else:
                if dict1[str1[i]]!=str2[i]:
                    return 0
                    
            if str2[i] not in dict2:
                dict2[str2[i]]=str1[i]
            else:
                if dict2[str2[i]]!=str1[i]:
                    return 0
        return 1
        
