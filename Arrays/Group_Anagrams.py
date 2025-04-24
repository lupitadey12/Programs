class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Anagram: Rearrange characters of a word to get a different word
        
        #Store each pattern in a key, all strings matching with the same pattern, store as value to the key
        #Pattern is created using count of each alphabet occurence as 1, remaining as 0

        result = {} #The pattern is the key, value are all words matching the pattern

        for word in strs:
            count = [0]*26 #Each word is generating it's own pattern of as per alphabet occurence
            for char in word:
                #Each character of the word is assigned an index, the count for that index gains a value else 0
                count[ord(char) - ord('a')] += 1
            key = tuple(count)

            if key not in result:#Default dict handles the same use case, defaultdict(list)
                result[key] = []      
            result[key].append(word)                      

        return list(result.values())
