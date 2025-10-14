# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        currCount = sorted(words[0])
        res = [words[0]]

        for i in range(1, len(words)):
            count = sorted(words[i])

            if count != currCount:
                res.append(words[i])
                currCount = count
        
        return res