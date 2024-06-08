'''
Non Repeating Character (GFG)

Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.

Example 1:

Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.
'''

import math

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        freq_arr=[0]*26
        index_arr=[0]*26
        
        length=len(s)
        
        for i in range(length):
            freq_arr[ord(s[i])-97]+=1
            if freq_arr[ord(s[i])-97]==1:
                index_arr[ord(s[i])-97]=i
        
        maximum=math.inf
        value=None
        
        for i in range(26):
            if freq_arr[i]==1:
                if index_arr[i]<maximum:
                    maximum=index_arr[i]
                    value=chr(i+97)
                    
        if value==None:
            return '$'
        
        return value
