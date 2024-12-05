'''
Meta Strings (GFG)

Given two strings consisting of lowercase english alphabets, the task is to check whether these strings are meta strings or not.
Meta strings are the strings which can be made equal by exactly one swap in any of the strings. Equal string are not considered here as Meta strings.

Example 1:

Input:
S1 = "geeks", S2 = "keegs"
Output: 1
Explanation: We can swap the 0th and 3rd
character of S2 to make it equal to S1.
'''
class Solution:
    def metaStrings(self, S1, S2):
        length=len(S1)
        
        count=0
        string1=""
        string2=""
        for i in range(length):
            if S1[i]!=S2[i]:
                count+=1
                string1+=S1[i]
                string2+=S2[i]
                
        if count==2:
            if ''.join(sorted(list(string1)))==''.join(sorted(list(string2))):
                return 1
            
        return 0
