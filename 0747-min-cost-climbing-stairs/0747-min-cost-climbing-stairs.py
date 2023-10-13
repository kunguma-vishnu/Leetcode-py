class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = two = 0
        for i in range(len(cost)-1,-1,-1):
            cost[i] += min(one,two)
            two = one
            one = cost[i]
        return min(cost[0],cost[1])