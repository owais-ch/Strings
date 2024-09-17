'''
Longest Distinct Charecters in String (GFG)
Given a string S, find the length of the longest substring with all distinct characters. 

Example 1:

Input:
S = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest 
substring with all distinct characters.
'''

class Solution:

    def longestSubstrDistinctChars(self, S):
        dict1=dict()
        dict2=dict()
        
        length=len(S)
        
        i=0
        last=0
        
        max_length=0
        
        while i<length:
            if S[i] not in dict1:
                dict1[S[i]]=i
                dict2[i]=S[i]
            else:
                prev_index=dict1[S[i]]
                max_length=max(max_length,i-last)
                
                k=last
                
                while k<prev_index:
                    dict1.pop(dict2[k])
                    k+=1
                    
                dict1[S[i]]=i
                dict2[i]=S[i]
                
                last=prev_index+1
                
            i+=1
            
        max_length=max(max_length,i-last)    
        
        return max_length
