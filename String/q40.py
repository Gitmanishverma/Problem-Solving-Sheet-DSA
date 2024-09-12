# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
#  all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

import re

def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        # print(s)
        for i in s:
            if i.isalnum()==False:
                s=s.replace(i,"")
        return s==s[::-1]
        
