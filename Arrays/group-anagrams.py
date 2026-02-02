class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Dictionary để nhóm các anagram
        groups = {}

        # Duyệt từng chuỗi trong danh sách
        for s in strs:
            # Sort các ký tự trong chuỗi để làm key
            key = "".join(sorted(s))

            # Nếu key chưa tồn tại thì tạo danh sách mới
            if key not in groups:
                groups[key] = []

            # Thêm chuỗi vào nhóm tương ứng
            groups[key].append(s)

        # Trả về danh sách các nhóm
        return list(groups.values())
def main():
    solution = Solution()

    strs1 = ["eat", "meo", "tan", "ate", "nat", "bat","oemhHHHAHA"]
    strs2 = [""]
    strs3 = ["a"]

    print(solution.groupAnagrams(strs1))
    print(solution.groupAnagrams(strs2))
    print(solution.groupAnagrams(strs3))


if __name__ == "__main__":
    main()
