#Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Input: strs = [""]
# Output: [[""]]
# Input: strs = ["a"]
# Output: [["a"]]
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap=defaultdict(list)
        for str in strs:
            sort_str= ''.join(sorted(str))
            hashmap[sort_str].append(str)
        return hashmap.values()

strs = ["eat","tea","tan","ate","nat","bat"]
solution=Solution()
print(solution.groupAnagrams(strs))
