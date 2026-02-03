class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch
            count[ch] -= 1
def main():
    sol = Solution()

    # Test case 1
    s1 = "abcd"
    t1 = "abcde"
    print("Test 1:", sol.findTheDifference(s1, t1))  # e

    # Test case 2
    s2 = ""
    t2 = "y"
    print("Test 2:", sol.findTheDifference(s2, t2))  # y


if __name__ == "__main__":
    main()