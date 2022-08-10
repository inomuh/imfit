from collections import defaultdict


class Solution:
    def groupAnagrams(strs):
        hashmap = defaultdict(list)
        for s in strs:
            # keys can be strings, bcz they are immutable.
            hashmap[str(sorted(s))].append(s)
        passhashmap.values()

print(Solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))