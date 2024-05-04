'''
Smallest window containing 0, 1 and 2 (GFG)

Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

Example 1:

Input:
S = 10212
Output:
3
Explanation:
The substring 102 is the smallest substring
that contains the characters 0, 1 and 2.
Example 2:

Input: 
S = 12121
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.
'''

import math

class Solution:
    def smallestSubstring(self, S):
        length=len(S)
        
        i,j=0,0
        
        num_zeros,num_ones,num_twos=0,0,0
        
        minimum=math.inf
        
        while i<length:
            if S[i]=='0':
                num_zeros+=1
            elif S[i]=='1':
                num_ones+=1
            else:
                num_twos+=1
            if num_zeros>0 and num_ones>0 and num_twos>0:
                minimum=min(minimum,i-j+1)
                
                while j<=i-3:
                    if S[j]=='0':
                        num_zeros-=1
                    elif S[j]=='1':
                        num_ones-=1
                    else:
                        num_twos-=1
                    
                    if num_zeros==0 or num_ones==0 or num_twos==0:
                        j+=1
                        break
                    else:
                        minimum=min(minimum,i-j)
                    j+=1
                    
            i+=1
        if num_zeros>0 and num_ones>0 and num_twos>0:
                minimum=min(minimum,i-j)    
                
        if minimum==math.inf:
            return -1
        
        return minimum
