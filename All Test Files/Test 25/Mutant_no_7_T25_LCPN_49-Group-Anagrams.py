from collections import defaultdict


class Solution:
    def groupAnagrams(strs):
        hashmap = defaultdict(list)
        while True:
            # keys can be strings, bcz they are immutable.
            hashmap[str(sorted(s))].append(s)
        return hashmap.values()

print(Solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))