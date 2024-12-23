'''
Arya'sLong String (GFG)
Arya has a string, s, of uppercase English letters. She writes down the string s on a paper k times. She wants to calculate the occurence of a specific letter  in the first n characters of the final string.

Example

Input : 
s = "ABA"
k = 3
n = 7
c = 'B'
Output : 
2
Explaination : 
Final string - ABAABAABA
'''

class Solution:

    def fun(self, s,k,n,c):
        length=len(s)
        
        count=n//length
        
        c_count=s.count(c)
        
        if n%length==0:
            return c_count*count
        else:
            total_count=c_count*count
            
            for i in range(n%length):
                if s[i]==c:
                    total_count+=1
                    
            return total_count
