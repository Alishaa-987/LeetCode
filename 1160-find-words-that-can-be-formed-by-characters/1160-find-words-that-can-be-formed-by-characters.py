class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
         l = []
         c = Counter(chars)
         for i in words:
            w = Counter(i)
            if w & c == w:
                l.append(i)
         suml = 0       
         for i in l:
            suml = suml + len(i)
         return suml
