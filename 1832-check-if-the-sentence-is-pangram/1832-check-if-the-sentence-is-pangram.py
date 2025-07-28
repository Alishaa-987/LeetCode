class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for i in all_alphabets:
            if i not in sentence:
                return False
        return True
           

