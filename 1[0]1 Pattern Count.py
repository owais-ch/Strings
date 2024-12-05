'''
1[0]1 Pattern Count (GFG)

Given a string S, your task is to find the number of patterns of form 1[0]1 where [0] represents any number of zeroes (minimum requirement is one 0) there should not be any other character except 0 in the [0] sequence.

Example 1:

Input:
S = "100001abc101"
Output: 2
Explanation:
The two patterns are "100001" and "101".
'''

class Solution:
    def patternCount(self, S): 
        length=len(S)
        
        count=0
        
        start=0
        end=0
        zeros=0
        for i in range(length):
            if S[i]=="1":
                if start==0:
                    start=1
                elif i<length and S[i-1]=="1":
                    start=1
                elif start==1 and zeros==1 and end==0:
                    count+=1
                    start=1
                    zeros=0
            elif S[i]=="0":
                if start==1 and end==0:
                    zeros=1
                else:
                    start,zeros,end=0,0,0
            else:
                start=0
                zeros=0
                end=0
                
        return count
