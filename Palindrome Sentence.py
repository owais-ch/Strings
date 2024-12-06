'''
Palindrome Sentence (GFG)

Given a single string s, the task is to check if it is a palindrome sentence or not. A palindrome sentence is a sequence of characters,
such as word, phrase, or series of symbols that reads the same backward as forward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

Examples:

Input: s = "Too hot to hoot"
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become “toohottohoot” which is a palindrome.
'''

class Solution:
	def sentencePalindrome(self, s):
		s=s.replace(" ","")
		
		string=""
		
		for i in s:
            if i.isalpha()==True:
                string+=i.lower()
            elif i.isdigit()==True:
                string+=i
        if string==string[::-1]:
            return True
            
        return False
