class Solution:
    def frequencySort(self, s: str) -> str:
       dict = Counter(s)
       list = sorted(dict.items() , key=lambda x:x[1] , reverse=True)
       return ''.join(char * count for char , count in list)