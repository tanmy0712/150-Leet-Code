class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)-1
        lenght=0
        while i>= 0 and s[i]==" ":
            i-=1
        while i>=0 and s[i] !=" ":
            lenght+=1
            i-=1
        return lenght
def main():
    solution = Solution()
    s1 = "Hello World"

    print(solution.lengthOfLastWord(s1))
if __name__ == "__main__":
    main()