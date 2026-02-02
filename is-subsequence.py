class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  # con trỏ cho chuỗi s

        # Duyệt từng ký tự trong t
        for ch in t:
            # Nếu đã duyệt hết s thì dừng
            if i == len(s):
                break

            # Nếu ký tự khớp thì dịch con trỏ s
            if s[i] == ch:
                i += 1

        # Nếu duyệt hết s thì s là subsequence của t
        return i == len(s)
def main():
    solution = Solution()

    s1 = "abc"
    t1 = "ahbgdc"

    s2 = "axc"
    t2 = "ahbgdc"

    s3 = ""
    t3 = "abc"

    print(solution.isSubsequence(s1, t1))  # True
    print(solution.isSubsequence(s2, t2))  # False
    print(solution.isSubsequence(s3, t3))  # True


if __name__ == "__main__":
    main()
