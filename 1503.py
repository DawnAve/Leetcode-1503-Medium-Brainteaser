class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        for i in left:
            time = max(time, i)
        for i in right:
            time = max(time,n-i)
        return time
