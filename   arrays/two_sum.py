# Problem: Two Sum
# Difficulty: Easy
# Pattern: Hash Map
# Time: O(n) | Space: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i



# Test cases
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(sol.twoSum([3, 2, 4], 6))        # Expected: [1, 2]
print(sol.twoSum([3, 3], 6))           # Expected: [0, 1]            