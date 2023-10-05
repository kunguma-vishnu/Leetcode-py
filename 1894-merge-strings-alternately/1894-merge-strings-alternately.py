class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(len(word1)):
            res.insert(i*2,word1[i])
        for i in range(len(word2)):
            res.insert((i*2)+1,word2[i])
        return "".join(res)