class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mapping={}
        t_mapping={}
        for char in s:
            if char not in s_mapping:
                s_mapping[char] = 1
            else:
                s_mapping[char] += 1
        for char in t:
            if char not in t_mapping:
                t_mapping[char] = 1
            else:
                t_mapping[char] += 1
                
        return s_mapping==t_mapping