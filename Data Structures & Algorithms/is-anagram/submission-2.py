class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_map = {}
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1
        for c in t:
            if not freq_map.get(c):
                return False
            freq_map[c] = freq_map.get(c) - 1
        for i in freq_map.values():
            if i:
                return False
        return True
        