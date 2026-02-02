class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary lưu giá trị và chỉ số tương ứng
        seen = {}

        # Duyệt qua mảng
        for i, num in enumerate(nums):
            # Giá trị còn thiếu để đạt target
            remain = target - num

            # Nếu đã thấy giá trị còn thiếu trước đó
            if remain in seen:
                return [seen[remain], i]

            # Lưu giá trị hiện tại và chỉ số của nó
            seen[num] = i
def main():
    solution = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9

    nums2 = [3, 2, 4]
    target2 = 6

    nums3 = [3, 3]
    target3 = 6

    print(solution.twoSum(nums1, target1))  # [0, 1]
    print(solution.twoSum(nums2, target2))  # [1, 2]
    print(solution.twoSum(nums3, target3))  # [0, 1]


if __name__ == "__main__":
    main()
