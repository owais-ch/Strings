'''
Case-specific Sorting of Strings (GFG)

Given a string S consisting of only uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character
then it should not have a lowercase character after being sorted and vice versa.

Example 1:

Input:
N = 12
S = defRTSersUXI
Output: deeIRSfrsTUX
Explanation: Sorted form of given string
with the same case of character as that
in original string is deeIRSfrsTUX
'''

class Solution:
    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        lstring=''
        ustring=''
        
        for i in range(n):
            if s[i].islower()==True:
                lstring+=s[i]
            else:
                ustring+=s[i]
                
        lstring=sorted(lstring)
        ustring=sorted(ustring)
        
        resulting_string=''
        
        p,q=0,0
        
        for i in range(n):
            if s[i].islower()==True:
                resulting_string+=lstring[p]
                p+=1
            else:
                resulting_string+=ustring[q]
                q+=1
                
        return resulting_string
