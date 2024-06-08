'''
Minimum indexed character (GFG)

Given a string str and another string patt. Find the minimum index of the character in str that is also present in patt.

Example 1:

Input:
str = geeksforgeeks
patt = set
Output: 1
Explanation: e is the character which is
present in given str "geeksforgeeks"
and is also present in patt "set". Minimum
index of e is 1. 
'''
import math

class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat): 
        index_arr=[0]*26
        freq_arr=[0]*26
        
        Str_length=len(Str)
        
        ascii_a=ord('a')
        
        for i in range(Str_length):
            freq_arr[ord(Str[i])-ascii_a]+=1
            
            if freq_arr[ord(Str[i])-ascii_a]==1:
                index_arr[ord(Str[i])-ascii_a]=i
        
        pat_length=len(pat)
        
        maximum=math.inf
        
        for i in range(pat_length):
            if index_arr[ord(pat[i])-ascii_a]<maximum and freq_arr[ord(pat[i])-ascii_a]>0:
                maximum=index_arr[ord(pat[i])-ascii_a]
                    
        if maximum==math.inf:
            return -1
            
        return maximum
