

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start,path) -> None:
            if len(path) == k:
                result.append(path.copy())
                return

            for i in range(start,n+1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()


        backtrack(1,[])
        return result
