'''
Amend The Sentence (GFG)

Given a string which is basically a sentence without spaces between words. However the first letter of every word is in uppercase. You need to print this sentence after following amendments:
(i) Put a single space between these words
(ii) Convert the uppercase letters to lowercase.
Note: The first character of the string can be both uppercase/lowercase.

Example 1:

Input:
s = "BruceWayneIsBatman"
Output: bruce wayne is batman
Explanation: The words in the string are
"Bruce", "Wayne", "Is", "Batman".
'''

class Solution:
    def amendSentence(self, s):
        length=len(s)
        
        num_word=1
        
        string=""
        start=0
        end=0
        
        for i in range(1,length):
            if s[i].isupper()==True:
                num_word+=1
                end=i
                string=string+s[start:end]+" "
                start=end
                
        string=string+s[start:length] 
        
        string=string.lower()
        
        return string
