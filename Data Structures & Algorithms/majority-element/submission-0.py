class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map={}
        n=len(nums)

        for num in nums:
            count_map[num]=1+count_map.get(num,0)
        for num, freq in count_map.items():
            if freq > n//2:
                return num