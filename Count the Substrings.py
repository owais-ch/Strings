'''
Count the Substrings (GFG)

Given a string S. The task is to count the number of substrings which contains equal number of lowercase and uppercase letters. 

Example 1:

Input:
S = "gEEk"
Output: 3
Explanation: There are 3 substrings of
the given string which satisfy the
condition. They are "gE", "gEEk" and "Ek".
'''
class Solution: 
    def countSubstring(self, S): 
        length=len(S)
        
        num_lower=0
        num_upper=0
        count=0
        
        for i in range(length-1):
            if S[i].isupper()==True:
                num_upper+=1
            else:
                num_lower+=1
            for j in range(i+1,length):
                if S[j].isupper()==True:
                    num_upper+=1
                else:
                    num_lower+=1
                    
                if num_upper==num_lower:
                    count+=1
            num_lower,num_upper=0,0
            
        return count
