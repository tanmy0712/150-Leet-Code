class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            s = 0
            while n > 0:
                digit = n % 10
                s += digit * digit
                n //= 10
            n = s

        return True


def main():
    sol = Solution()

    n = 19   # test case
    print("Is happy number?", sol.isHappy(n))

    n = 2    # test case
    print("Is happy number?", sol.isHappy(n))


if __name__ == "__main__":
    main()
