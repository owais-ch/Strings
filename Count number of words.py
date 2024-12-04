'''
Count number of words (GFG)

Given a string consisting of spaces,\t,\n and lower case  alphabets.Your task is to count the number of words where spaces,\t and \n work as separators.
 
Example 1:

Input: S = "abc def"
Output: 2
Explanation: There is a space at 4th
position which works as a seperator
between "abc" and "def"
'''

class Solution:
    def countWords(self, s):
        s=s.replace("\\n"," ")
        s=s.replace("\\t"," ")
        
        s=s.split(" ")
        count=0
        
        for i in s:
            if i!="":
                count+=1
                
        return count
