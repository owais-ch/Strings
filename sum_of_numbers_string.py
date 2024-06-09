'''
Sum of numbers in string (GFG)

Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.

Example 1:

Input:
str = 1abc23
Output: 24
Explanation: 1 and 23 are numbers in the
string which is added to get the sum as
24.
'''

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        total=0
        
        s_length=len(s)
        number=''
        for i in range(s_length):
            if s[i].isdigit()==True:
                number+=s[i]
            else:
                if number!='':
                    total+=int(number)
                    number=''
        if number!='':
             total+=int(number)
        return total
