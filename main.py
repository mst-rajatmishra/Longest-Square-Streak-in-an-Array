from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))  # Sort and remove duplicates
        num_set = set(nums)  # For fast lookup
        max_length = 0
        
        for num in nums:
            current_length = 0
            current_num = num
            
            while current_num in num_set:
                current_length += 1
                current_num = current_num ** 2  # Move to the next square
            
            # Only consider streaks of length at least 2
            if current_length >= 2:
                max_length = max(max_length, current_length)
        
        return max_length if max_length >= 2 else -1

# Example usage:
# sol = Solution()
# print(sol.longestSquareStreak([4, 3, 6, 16, 8, 2]))  # Output: 3
# print(sol.longestSquareStreak([2, 3, 5, 6, 7]))      # Output: -1
