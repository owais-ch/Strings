'''
Remove vowel from a string (GFG)

Given a string, remove the vowels from the string.

Example 1:

Input: S = "welcome to geeksforgeeks"
Output: wlcm t gksfrgks
Explanation: Ignore vowels and print other
characters 
'''

class Solution:
	def removeVowels(self, S):
		S=list(S)
		
		vowels=set({'a','e','i','o','u'})
		
		length = len(S)
		
		for i in range(length):
		    if S[i] in vowels:
		        S[i]=""
		        
        return "".join(S)
