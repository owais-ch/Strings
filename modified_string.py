'''
The Modified String (GFG)

Ishaan is playing with strings these days. He has found a new string. He wants to modify it as per the following rules to make it valid:

The string should not have three consecutive same characters (Refer example for explanation).
He can add any number of characters anywhere in the string. 
Find the minimum number of characters which Ishaan must insert in the string to make it valid.

Example 1:

Input:
S = aabbbcc
Output: 1
Explanation: In aabbbcc 3 b's occur
consecutively, we add a 'd',and Hence,
output will be aabbdbcc.
'''

import math

class Solution:
    
    #Function to find minimum number of characters which Ishaan must insert  
    #such that string doesn't have three consecutive same characters.
    def modified(self,s):
        count=1
        total=0
        
        length=len(s)
        
        for i in range(1,length):
            if s[i]==s[i-1]:
                count+=1
                if count==3:
                    total+=1
                    count=1
            else:
                count=1
            
        return total
