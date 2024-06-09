'''
Check if string is rotated by two places (GFG)

Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating (in any direction) string 'a' by exactly 2 places.

Example 1:

Input:
a = amazon
b = azonam
Output: 
1
Explanation: 
amazon can be rotated anti-clockwise by two places, which will make it as azonam.
'''

class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        str2_length=len(str2)
        
        str2=str2[str2_length-2:]+str2[0:str2_length-2]
        
        if str1==str2:
            return 1
        
        str2=str2[4:]+str2[0:4]  
        
        if str1==str2:
            return 1
            
        return 0
