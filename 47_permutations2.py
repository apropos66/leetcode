class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        sol, path = [], []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                if path not in sol:
                    sol.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack()
                    used[i] = False
                    path.pop()

        backtrack()
        return sol
