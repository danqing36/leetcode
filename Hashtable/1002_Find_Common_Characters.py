#Given a string array words, return an array of all characters that show up
# in all strings within the words (including duplicates). You may return the answer in any order.
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d={}
        for c in list(words[0]):
            d[c]=d.get(c,0)+1
        for word in words[1:]:
            for k in d.keys():
                d[k]=min(d[k], word.count(k))
        result=[]
        for i in d.keys():
            result+=i*d[i]
        return result