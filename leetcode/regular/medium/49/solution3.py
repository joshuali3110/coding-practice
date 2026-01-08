# https://leetcode.com/problems/group-anagrams/description/

# optimized O(N * k) solution using tuples for key generation instead of strings (avoids doing string concatenation through lists and str.join), comparable to using sorted() but still slower for smaller k; definitely best solution for large k

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1

            groups[tuple(counts)].append(s)
        
        return [group for group in groups.values()]