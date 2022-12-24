'''
You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.
 

Example 1:

Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
'''

from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        if set(num)==set('0'):
            return '0'
        dict1=Counter(num)
        
        list3=list(dict1.items())
        
        list3.sort(key=lambda x:[-int(x[0]),-x[1]])
        #print(list3)
        
        visited=dict()
        
        list2=[]
        list4=[]
        
        for i in list3:
            divider=i[1]//2
            if i[1]%2==0:
                value=i[1]
            else:
                value=i[1]-1
                
            if divider>=1:
                list2.append([i[0],value])
                if value!=i[1]:
                    list3.append([i[0],1])
                visited[i[0]]=1
            else:
                list4.append(i)
        
        list2.sort(key=lambda x:-int(x[0]))
        list4.sort(key=lambda x:-int(x[0]))
        #print(list2,list4)
        
        string1=''
        count=0
        for i in list2:
            if (count==0 and i[0]!='0') or count>0:
                string1+=i[0]*(i[1]//2)
            count+=1
            
        #print(string1)
        ss=''
        if list4!=[]:
            ss=list4[0][0]
        return string1+ss+string1[::-1]
