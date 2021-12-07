#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#Input: s = "anagram", t = "nagaram"
#Output: true
#Input: s = "rat", t = "car"
#Output: false

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashtable={}
        for char in s:
            if char in hashtable:
                hashtable[char]+=1
            else:
                hashtable[char]=1
        for char in t:
            if char in hashtable:
                hashtable[char]-=1
            else:
                return False
        for num in hashtable.values():
            if num!=0:
                return False
        return True
s="aacc"
t="ccac"
solu=Solution()
print(solu.isAnagram(s,t))