class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. Đếm tần suất xuất hiện
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # 2. Tạo bucket: index = số lần xuất hiện
        # nums.length tối đa là n, nên cần n+1 bucket
        bucket = [[] for _ in range(len(nums) + 1)]

        # Đưa các số vào bucket tương ứng với tần suất
        for num, count in freq.items():
            bucket[count].append(num)

        # 3. Lấy k phần tử có tần suất cao nhất
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
def main():
    solution = Solution()

    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2

    nums2 = [1]
    k2 = 1

    nums3 = [1,2,1,2,1,2,3,1,3,2]
    k3 = 2

    print(solution.topKFrequent(nums1, k1))  # [1, 2]
    print(solution.topKFrequent(nums2, k2))  # [1]
    print(solution.topKFrequent(nums3, k3))  # [1, 2]


if __name__ == "__main__":
    main()