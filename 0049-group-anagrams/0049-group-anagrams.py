from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
       dictionary = {}

       for words in strs:
            sorted_word = ''.join(sorted(words))
            if sorted_word in dictionary:
                dictionary[sorted_word].append(words)
            else:
                dictionary[sorted_word] = [words]
       return list(dictionary.values())
