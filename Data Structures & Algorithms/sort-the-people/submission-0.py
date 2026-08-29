class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map={}
        for i in range(len(names)):
            map[heights[i]] = names[i]
        heights.sort()
        for i in range(len(heights)):
            names[i] = map[heights[len(heights)-1-i]]
        return names