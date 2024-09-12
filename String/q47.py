
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Question link:https://www.google.com/url?q=https://leetcode.com/problems/longest-substring-without-repeating-characters/&sa=D&source=editors&ust=1726042709312795&usg=AOvVaw1Q-yWuLz0qdIe0hAEKl0GD


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        max_len=left=0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len



        