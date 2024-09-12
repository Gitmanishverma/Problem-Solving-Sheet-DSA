# Given two strings s and t, return true if t is an 
# anagram of s, and false otherwise.
# Input: s = "anagram", t = "nagaram"

# Output: true

def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))
        