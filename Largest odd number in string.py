'''
Largest odd number in string (GFG)
Given a string S, representing a large integer. Return the largest-valued odd integer (as a string) that is substring of the given string S.

Note: A substring is a contiguous sequence of characters within a string. A null string ("") is also a substring.

Example 1:

Input: s = "504"
Output: "5"
Explanation: The only subtring "5" is odd number.
'''

class Solution:
    def maxOdd(self, s):
        length=len(s)
        maximum=""
        maxz=0
        string=""
        
        for i in range(length-1,-1,-1):
            if int(s[i])%2!=0:
                return s[0:i+1]
                
        return maximum


