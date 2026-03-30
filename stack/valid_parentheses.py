class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack
    
# Test cases
sol = Solution()
print(sol.isValid("()"))  # Expected: True
print(sol.isValid("()[]{}"))  # Expected: True
print(sol.isValid("(]"))  # Expected: False
print(sol.isValid("([)]"))  # Expected: False
print(sol.isValid("{[]}"))  # Expected: True
