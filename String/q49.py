# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# question link: https://www.google.com/url?q=https://leetcode.com/problems/group-anagrams/&sa=D&source=editors&ust=1726138918949463&usg=AOvVaw1GK0_4H9ke7bF49zmdm2hg

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_set=set()
        for i in strs:
            i=''.join(sorted(i))
            str_set.add(i)
        print(str_set)
        result=[]
        
        for i in str_set:
            temp=[]    
            for j in range(len(strs)):
                x="".join(sorted(strs[j]))
                if(x==i):
                    temp.append(strs[j])
            result.append(temp)
        return result
            
        

## secand approch with less  time 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets=defaultdict(list)
        for word in strs:
            sortedword=''.join(sorted(word))
            sets[sortedword].append(word)
        return(sets.values())
