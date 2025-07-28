class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        combine = list(zip(names, heights))
        combine.sort(key=lambda x:x[1],reverse=True)
        return [name for  name, _ in combine]