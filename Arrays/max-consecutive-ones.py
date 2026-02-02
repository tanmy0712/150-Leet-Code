class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cur = 0
        ans = 0

        for x in nums:
            if x == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0

        return ans
