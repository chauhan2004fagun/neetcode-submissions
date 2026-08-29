class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        temp=[]

        for num in count:
            if count[num] > len(nums)//3:
                temp.append(num)
        return temp