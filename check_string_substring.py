'''
Check if a String is Subsequence of Other (GFG)

Given two strings A and B, find if A is a subsequence of B. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.


Example 1:

Input:
A = AXY 
B = YADXCP
Output: False
Explanation: A is not a subsequence of B
as 'Y' appears before 'A'.
'''
class Solution:
    
    #Function to check if a string is subsequence of other string.
    def isSubSequence(self, A, B):
        length_a=len(A)
        length_b=len(B)
        
        i,j=0,0
        
        while i<length_a and j<length_b:
            if A[i]==B[j]:
                i+=1
            j+=1
            
        if i<length_a:
            return False
            
        return True
