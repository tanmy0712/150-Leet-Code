class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Lấy độ dài của mảng
        n = len(nums)

        # Tạo mảng kết quả rỗng
        ans = []

        # Thêm các phần tử của nums lần thứ nhất
        for i in range(n):
            ans.append(nums[i])

        # Thêm các phần tử của nums lần thứ hai
        for i in range(n):
            ans.append(nums[i])

        return ans
def main():
    solution = Solution()

    nums1 = [1, 2, 1]
    nums2 = [5, 3, 6, 9]

    print(solution.getConcatenation(nums1))  # [1,2,1,1,2,1]
    print(solution.getConcatenation(nums2))  # [1,3,2,1,1,3,2,1]


if __name__ == "__main__":
    main()
