'''
Good or Bad string (GFG)

In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'. Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String on the basis of following rules:

If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD". A String is considered "GOOD" only if it is not “BAD”.

NOTE: String is considered as "BAD" if the above condition is satisfied even once. Else it is "GOOD" and the task is to make the string "BAD".
 

Example 1:

Input:
S = aeioup??
Output:
1
Explanation: The String doesn't contain more
than 3 consonants or more than 5 vowels together.
So, it's a GOOD string.
'''

class Solution:
    def isGoodorBad(self, S):
        consonants,vowels = 0,0
        
        for i in S:
            if i in {'a','e','i','o','u'}:
                vowels+=1
                consonants=0
                if vowels>5:
                    return 0
            elif i!="?":
                consonants+=1
                vowels=0
                
                if consonants>3:
                    return 0
            else:
                consonants+=1
                vowels+=1
                if consonants>3:
                    return 0
                elif vowels>5:
                    return 0
                    
        return 1
