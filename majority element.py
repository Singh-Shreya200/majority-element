class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = defaultdict(int)
        n = len(nums)//2
        for ele in nums:
            store[ele] += 1
            if store[ele] > n:
                return ele
