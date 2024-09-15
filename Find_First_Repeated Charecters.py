''
Find First Repeated Charecters (GFG)
Given a string S. The task is to find the first repeated character in it.
We need to find the character that occurs more than once and whose index of second occurrence is smallest. S contains only lowercase letters.

Example 1:

Input: S="geeksforgeeks"
Output: e
Explanation: 'e' repeats at third position.
'''

class Solution:

    def firstRepChar(self, s):
        dict1=dict()
        
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                return s[i]
                
        return -1
