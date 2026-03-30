class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count_s ={}
        count_t ={}

        if len(s) != len(t):
            return False
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t
    
# Test cases
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # Expected: True
print(sol.isAnagram("rat", "car"))  # Expected: False
print(sol.isAnagram("listen", "silent"))  # Expected: True   

