class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        newList = []

        for i in range(len(nums)):
            if nums[i] == val:
                count -= 1
            else:
                newList.append(nums[i])

        for i in range(len(newList)):
            nums[i] = newList[i]
        
        return count