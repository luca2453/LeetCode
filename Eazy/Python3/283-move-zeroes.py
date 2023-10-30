class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lista = []
        zerosCount = 0

        for i in range(n):
            if nums[i] != 0:
                lista.append(nums[i])
            else:
                zerosCount = zerosCount + 1
                
        for _ in range(zerosCount):
            lista.append(0)

        for i in range(n):
            nums[i] = lista[i]