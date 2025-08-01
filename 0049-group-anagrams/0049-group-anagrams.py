from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)  # A dictionary to hold lists

        for word in strs:
            # Sort the word to form the key
            key = ''.join(sorted(word))
            result[key].append(word)  # Add the word to the correct list

        return list(result.values())  # Return all grouped anagram lists
