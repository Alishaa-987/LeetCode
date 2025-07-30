class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] =1
            else:
                dic[arr[i]]+=1

        if len(list(dic.values())) == len(set(dic.values())):
            return True
        else:
            return False
        