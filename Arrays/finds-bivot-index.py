class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            if leftSum == total - leftSum - nums[i]:
                return i
            leftSum += nums[i]

        return -1


def main():
    sol = Solution()

    nums = [1, 7, 3, 6, 5, 6]
    print("Input:", nums)
    print("Pivot index:", sol.pivotIndex(nums))

    nums = [1, 2, 3]
    print("Input:", nums)
    print("Pivot index:", sol.pivotIndex(nums))

    nums = [2, 1, -1]
    print("Input:", nums)
    print("Pivot index:", sol.pivotIndex(nums))


if __name__ == "__main__":
    main()
