'''
Length of Longest Substring (GFG)
Given a string S, find the length of the longest substring without repeating characters.


Example 1:

Input:
S = "geeksforgeeks"
Output:
7
Explanation:
Longest substring is
"eksforg".
'''

class Solution:
    def longestUniqueSubsttr(self, S):
        dict1=dict()
        dict2=dict()
        
        length=len(S)
        
        i=0
        last=0
        longest=1
        count=0
        
        while i<length:
            if S[i] not in dict1:
                dict1[S[i]]=i
                dict2[i]=S[i]
                count+=1
            else:
                longest=max(longest,count)
                
                prev_index=dict1[S[i]]
                
                count=i-prev_index
                
                dict1[S[i]]=i
                dict2[i]=S[i]
                
                k=last
                
                while k<prev_index:
                    dict1.pop(dict2[k])
                    k+=1
                    
                last=prev_index+1
                
                
                
            i+=1
            
        longest=max(longest,count)
        
        return longest
