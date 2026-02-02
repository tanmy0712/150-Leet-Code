class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Nếu mảng rỗng thì không có prefix
        if not strs:
            return ""

        # Lấy chuỗi đầu tiên làm prefix ban đầu
        prefix = strs[0]

        # So sánh prefix với từng chuỗi còn lại
        for s in strs[1:]:
            # Trong khi chuỗi s không bắt đầu bằng prefix
            while not s.startswith(prefix):
                # Cắt bớt 1 ký tự ở cuối prefix
                prefix = prefix[:-1]

                # Nếu prefix rỗng thì không có prefix chung
                if prefix == "":
                    return ""

        return prefix
def main():
    solution = Solution()

    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    strs3 = ["a", "a", "a"]
    strs4 = ["", "b"]

    print(solution.longestCommonPrefix(strs1))  # "fl"
    print(solution.longestCommonPrefix(strs2))  # ""
    print(solution.longestCommonPrefix(strs3))  # "a"
    print(solution.longestCommonPrefix(strs4))  # ""


if __name__ == "__main__":
    main()
