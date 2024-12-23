'''
Anagram Palindrome (GFG)

Given a string S, Check if characters of the given string can be rearranged to form a palindrome.
Note: You have to return 1 if it is possible to convert the given string into palindrome else return 0. 

Example 1:

Input:
S = "geeksogeeks"
Output: Yes
Explanation: The string can be converted
into a palindrome: geeksoskeeg
'''

from collections import Counter

class Solution:

    def isPossible(self, S):
        length = len(S)
        
        dict1=Counter(S)
        
        odd_count =0
        
        if length%2!=0:
            for i in dict1:
                if dict1[i]%2!=0:
                    odd_count+=1
                    if odd_count>1:
                        return 0
        else:
            for i in dict1:
                if dict1[i]%2!=0:
                    return 0
                    
        return 1
