'''
Reversing the equation (GFG)

Given a mathematical equation that contains only numbers and +, -, *, /. Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
It is guaranteed that the given equation is valid, and there are no leading zeros.

Example 1:

Input:
S = "20-3+5*2"
Output: 2*5+3-20
Explanation: The equation is reversed with
numbers remaining the same.
'''

class Solution:
    def reverseEqn(self, s):
        length=len(s)
        
        num_list=[]
        op_list=[]
        
        start=0
        count=0
        for i in range(length):
            if s[i].isdigit()==True:
                count+=1
            else:
                num_list.append(s[start:start+count])
                count=0
                op_list.append(s[i])
                start=i+1
        
        num_list.append(s[start:length])        
        
        
        num_list.reverse()
        op_list.reverse()
        
        length1=len(num_list)
        length2=len(op_list)
        
        string=""
        
        for i in range(length2):
            string=string+num_list[i]+op_list[i]
        
        if length2==0:
            return s
        
        string+=num_list[i+1]
        
        return string
