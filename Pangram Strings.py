'''
Pangram Strings (GFG)

Check if the given string S is a Panagram or not. A pangram is a sentence containing every letter in the English Alphabet.

Example 1:

Input: S = "Pack mY box witH fIve dozen 
            liquor jugs"
Output: 1
Explanation: Given string contains all 
English Alphabets. 
'''

class Solution:
	def isPanagram(self, S):
	    S=S.lower()
		length=len(S)
		#print(ord('a'),97+25)
		dict1=dict()
		
		for i in S:
		    if ord(i) not in dict1:
		        dict1[ord(i)]=1
		        
        for i in range(97,122):
            if i not in dict1:
                return 0
                
        return 1
		
