class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandie = max(candies)
        sum = 0
        ans = []
        for i in range(0,len(candies)):
            sum = candies[i]+extraCandies
            if (maxCandie <= sum):
                ans.append(True)
            else:
                ans.append(False)
        return ans