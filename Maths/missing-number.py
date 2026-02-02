class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


def main():
    nums = [3, 0, 1]   # test case
    sol = Solution()
    result = sol.missingNumber(nums)
    print("Missing number is:", result)


if __name__ == "__main__":
    main()
