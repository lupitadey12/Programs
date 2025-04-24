class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ansSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in ansSet:#use while not if
                ansSet.remove(s[left])
                left += 1 
            ansSet.add(s[right])
            result = max(result, (right - left) + 1)#(right - left) + 1 is the window length
        return result

    #Concept:
    #The left pointer shriks the window by removing elements from the left until the duplicate element is removed (hence, while)
    #The right pointer keeps expanding the window, addind new elements
    #Maximum window size of unique elements is returned - (right - left) + 1
    #When you encounter a duplicate, the max window size would be already been recorded
