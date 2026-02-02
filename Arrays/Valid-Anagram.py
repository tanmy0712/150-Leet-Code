class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
def main():
    solution = Solution()

    s1 = "anagram"
    t1 = "nagaram"

    s2 = "tar"
    t2 = "tar"

    print(solution.isAnagram(s1, t1))  # True
    print(solution.isAnagram(s2, t2))  # False


if __name__ == "__main__":
    main()    