class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        sol, path = [], []
        n = len(nums)

        def backtrack():
            if len(path) == n:
                sol.append(path.copy())
                return

            for i in range(n):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack()
                    path.pop()

        backtrack()
        return sol


s = Solution()
result = s.permute([1, 2, 3])
print(result)
