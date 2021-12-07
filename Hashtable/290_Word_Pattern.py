#Given a pattern and a string s, find if s follows the same pattern.

#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        slist = s.split()
        print(slist)
        hashmap = {}
        if len(pattern)!= len(slist):
            return False
        for i in range (0,len(pattern)):
            print(i)
            if pattern[i] not in hashmap:
                if slist[i] not in hashmap.values():
                    hashmap[pattern[i]]= slist[i]
                else:
                    return False
            else:
                if hashmap[pattern[i]]!=slist[i]:
                    return False
        return True

s="baab"
t="dog dog dog dog"
solution=Solution()
print(solution.wordPattern(s,t))