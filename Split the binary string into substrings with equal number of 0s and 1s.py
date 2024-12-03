'''
Split the binary string into substrings with equal number of 0s and 1s (GFG)

Given binary string str of length N. The task is to find the maximum count of consecutive substrings str can be divided into such that all the substrings are balanced i.e. they have an equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then return -1.

Example 1:

Input:
S = "0100110101"
Output: 4
Explanation: 
The required substrings are 01, 0011, 01 and 01.
'''

class Solution:
    def maxSubStr(self,str):
        length=len(str)
        
        num_zeros,num_ones=str.count("0"),str.count("1")
        count=0
        zeros,ones=0,0
        
        for i in range(length):
            if s[i]=="0":
                zeros+=1
            elif s[i]=="1":
                ones+=1
                
            if zeros==ones:
                count+=1
                zeros=0
                ones=0
                
        if zeros!=ones:
            return -1
            
        return count
