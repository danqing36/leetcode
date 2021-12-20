#Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and
# false otherwise.
#Each letter in magazine can only be used once in ransomNote
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter={}
        for letter in magazine:
            if letter not in counter:
                counter[letter]=1
            else:
                counter[letter]+=1
        for letter in ransomNote:
            if letter not in counter:
                return False
            else:
                if counter[letter]==0:
                    return False
                else:
                    counter[letter]-=1
        return True