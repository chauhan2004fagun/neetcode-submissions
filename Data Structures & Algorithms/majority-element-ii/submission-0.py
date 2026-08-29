class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        temp=[]

        for key in count:
            if count[key] > len(nums)//3:
                temp.append(key)
        return temp
        