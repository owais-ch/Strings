'''
Remove common characters and concatenate (GFG)

Given two strings s1 and s2. Modify both the strings such that all the common characters of s1 and s2 are to be removed and the uncommon characters of s1 and s2 are to be concatenated.
Note: If all characters are removed print -1.

Example 1:

Input:
s1 = aacdb
s2 = gafd
Output: cbgf
Explanation: The common characters of s1
and s2 are: a, d. The uncommon characters
of s1 and s2 are c, b, g and f. Thus the
modified string with uncommon characters
concatenated is cbgf.
'''

class Solution:
    
    #Function to remove common characters and concatenate two strings.
    def concatenatedString(self,s1,s2):
        freq_arr_s1,freq_arr_s2=[0]*26,[0]*26
        
        s1_length=len(s1)
        s2_length=len(s2)
        
        result_string=''
        
        for i in range(s2_length):
            freq_arr_s2[ord(s2[i])-97]+=1
            
        for i in range(s1_length):
            if freq_arr_s2[ord(s1[i])-97]==0:
                result_string+=s1[i]
                
        for i in range(s1_length):
            freq_arr_s1[ord(s1[i])-97]+=1
            
        for i in range(s2_length):
            if freq_arr_s1[ord(s2[i])-97]==0:
                result_string+=s2[i]
                
        if result_string=='':
            return -1
            
        return result_string
