'''
Remove character (GFG)

Given two strings string1 and string2, remove those characters from first string(string1) which are present in second string(string2). Both the strings are different and contain only lowercase characters.
NOTE: Size of  first string is always greater than the size of  second string( |string1| > |string2|).
 

Example 1:

Input:
string1 = "computer"
string2 = "cat"
Output: "ompuer"
Explanation: After removing characters(c, a, t)
from string1 we get "ompuer".
'''

class Solution:
    def removeChars (ob, string1, string2):
        set1=set(string2)
        
        string = ""
        
        length = len(string1)
        
        for i in string1:
            if i not in set1:
                string+=i
                
        return string
