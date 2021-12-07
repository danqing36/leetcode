#Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order of characters.
#No two characters may map to the same character, but a character may map to itself.

# Input: s = "egg", t = "add"
# Output: true
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Input: s = "paper", t = "title"
# Output: true

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        hashtable={}
        for i in range(0, len(s)):
            if s[i] not in hashtable and t[i] not in hashtable.values():
                hashtable[s[i]] = t[i]
            elif s[i] not in hashtable and t[i] in hashtable.values():
                return False
            elif hashtable[s[i]] != t[i]:
                return False
        return True

s="badc"
t="baba"
solution=Solution()
print(solution.isIsomorphic(s,t))