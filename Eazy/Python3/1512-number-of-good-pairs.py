class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        tamanho = len(nums)
        for i in range(tamanho):
            for j in range(tamanho):
                if i < j and nums[i] == nums[j]:
                    count += 1
        return count