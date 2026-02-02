class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Tạo một set để lưu các giá trị đã xuất hiện
        seen = set()

        # Duyệt từng phần tử trong mảng
        for num in nums:
            # Nếu phần tử đã tồn tại trong set
            if num in seen:
                return True  # Có phần tử trùng
            # Ngược lại thì thêm vào set
            seen.add(num)

        # Nếu duyệt hết mà không có phần tử trùng
        return False


def main():
    # Khởi tạo đối tượng Solution
    solution = Solution()

    # Test các test case
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    print(solution.containsDuplicate(nums1))  # True
    print(solution.containsDuplicate(nums2))  # False
    print(solution.containsDuplicate(nums3))  # True


if __name__ == "__main__":
    main()