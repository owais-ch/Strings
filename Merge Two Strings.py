'''
Merge Two Strings (GFG)
Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.
NOTE: Add the whole string if other string is empty.

Example 1:

Input:
S1 = "Hello" S2 = "Bye"
Output: HBeylelo
Explanation: The characters of both the 
given strings are arranged alternatlively.
'''

class Solution:
    def merge(self, S1, S2):
        length1,length2 = len(S1),len(S2)
        
        i,j = 0,0
        count = 0
        string = ""
        while i < length1 and j < length2:
            if count%2 == 0:
                string+=S1[i]
                i+=1
            else:
                string+=S2[j]
                j+=1
            count+=1
        
        while i < length1:
            string+=S1[i]
            i+=1
            
        while j<length2:
            string+=S2[j]
            j+=1
            
        return string
