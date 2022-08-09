'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
'''

class Solution(object):
    def backspaceCompare(self, s, t):
        length1=len(s)
        length2=len(t)
        
        i=length1-1
        
        stack1=[]
        
        while i>-1:
            if stack1==[]:
                stack1.append(s[i])
            elif stack1!=[] and stack1[-1]=='#':
                if s[i]=='#':
                    stack1.append(s[i])
                else:
                    stack1.pop()
            elif stack1!=[] and stack1[-1]!='#':
                stack1.append(s[i])
                
            i-=1
            
        i=length2-1
        
        stack2=[]
        
        while i>-1:
            if stack2==[]:
                stack2.append(t[i])
            elif stack2!=[] and stack2[-1]=='#':
                if t[i]=='#':
                    stack2.append(t[i])
                else:
                    stack2.pop()
            elif stack2!=[] and stack2[-1]!='#':
                stack2.append(t[i])
                
            i-=1
        length_1=len(stack1)
        length_2=len(stack2)
        
        i=length_1-1
        
        while i>-1 and stack1[i]=='#':
            i=i-1
        stack1=stack1[:i+1]
        
        i=length_2-1
        
        while i>-1 and stack2[i]=='#':
            i=i-1
        stack2=stack2[:i+1]
        
        return stack1==stack2
