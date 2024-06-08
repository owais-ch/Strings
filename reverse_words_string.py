'''
Reverse Words in a string (GFG)

Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i
'''

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        length=len(S)
        S=S.split('.')
        length=len(S)
        
        i,j=0,length-1
        
        while i<j:
            S[i],S[j]=S[j],S[i]
            i+=1
            j-=1
            
        return '.'.join(S)
