class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        N = len(nums)
        pivot: int = 0

        # find the pivot
        for i in range(N - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return

        # finding the swap and swapping
        swap: int = N - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1

        nums[pivot - 1], nums[swap] = nums[swap], nums[pivot - 1]

        # reverseing the numbers after the swap to get the smallest possible nextPermutation
        left, right = pivot, N - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


s = Solution()
nums = [1, 2, 3, 4]
s.nextPermutation(nums)
print(nums)
