class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        minLen = min(len(word1),len(word2))
        mergedWord = ""
        for i in range(minLen):
            mergedWord += word1[i]
            mergedWord += word2[i]
        if len1 < len2:
            mergedWord += word2[len1:]
        else:
            mergedWord += word1[len2:]
        return mergedWord