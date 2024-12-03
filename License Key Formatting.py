'''
License Key Formatting (GFG)

Given a string S that consists of only alphanumeric characters and dashes. The string is separated into N + 1 groups by N dashes. Also given an integer K. 

We want to reformat the string S, such that each group contains exactly K characters, except for the first group, which could be shorter than K but still must contain at least one character.
Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted string.


Example 1:

Input: 
S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two
parts, each part has 4 characters. Note that two
extra dashes are not needed and can be removed.
'''

class Solution:
    def ReFormatString(self,S, K):
        S=S.replace("-","")
        length=len(S)
        
        string=""
        final_string=""
        sub_length=0
        first_sub_length=0
        
        if length%K!=0:
            num_groups=length//K
            first_sub_length=length-(num_groups*K)
            
        for i in range(length):
            if first_sub_length!=0:
                if sub_length<K:
                    string+=S[i]
                    sub_length+=1
                if sub_length==first_sub_length:
                    if i+1<length:
                        final_string=final_string+string.upper()+"-"
                        sub_length=0
                        string=""
                        first_sub_length=0
                    else:
                        final_string=final_string+string.upper()
                        first_sub_length=0
            else:
                if sub_length<K:
                    string+=S[i]
                    sub_length+=1
                    
                if sub_length==K:
                    if i+1<length:
                        final_string=final_string+string.upper()+"-"
                        sub_length=0
                        string=""
                    else:
                        final_string=final_string+string.upper()
                
        return final_string
