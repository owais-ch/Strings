'''
Same characters in two strings (GFG)

Given two strings A and B of equal length, find how many times the corresponding position in the two strings hold exactly the same character. The comparison should not be case sensitive. 

Example 1:

Input:
A = choice 
B = chancE
Output: 4
Explanation: characters at position 0, 1, 4 and 5
are same in the two strings A and B.
'''

class Solution:
    def sameChar(self, A, B):
        length=len(A)
        
        count=0
        
        for i in range(length):
            if A[i].upper()==B[i].upper():
                count+=1
                
        return count
