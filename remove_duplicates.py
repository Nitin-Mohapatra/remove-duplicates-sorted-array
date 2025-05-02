class Solution:
    def removeDuplicates(self, nums):
        i = 1
        j = 1
        while i < len(nums):
            if nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

s1 = Solution()
print(s1.removeDuplicates([1, 1, 2, 3, 3, 6, 6, 8, 9, 9, 9]))  # Output: 6
