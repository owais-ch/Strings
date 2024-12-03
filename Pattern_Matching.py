'''
Pattern Matching (GFG)
Given a text and a pattern, the task is to check if the pattern exists in the text or not.

Example 1:

Input: text = "geeksforgeeks"
       pat = "geek"
Output: 1
Explanation: "geek" exists in
"geeksforgeeks"
'''

class Solution:
	def search(self, text, pat):
		if pat in text:
		    return 1
		    
        return 0
