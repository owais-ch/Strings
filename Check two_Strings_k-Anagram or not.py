'''
Check if two strings are k-anagrams or not (GFG)

Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are K-anagrams of each other or not.

Two strings are called K-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most K characters in a string.

Example:

Input:
str1 = "fodr", str2="gork"
k = 2
Output:
1
Explanation: Can change fd to gk
'''

from collections import Counter

class Solution:
    def areKAnagrams(self, str1, str2, k):
        length1,length2=len(str1),len(str2)
        
        if length1!=length2:
            return 0
            
        dict1=Counter(str1)
        dict2=Counter(str2)
        
        total_diff=0
        #print(dict1)
        #print(dict2)
        
        for i in dict1:
            if i not in dict2:
                total_diff+=dict1[i]
            else:
                total_diff+=max(0,dict1[i]-dict2[i])
                
        if total_diff<=k:
            total_diff=0
            for i in dict2:
                if i not in dict1:
                    total_diff+=dict2[i]
                else:
                    total_diff+=max(0,dict2[i]-dict1[i])
            if total_diff<=k:
                return 1
            
        return 0
