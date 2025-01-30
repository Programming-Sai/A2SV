def isPalindrome(x: int) -> bool:
        if x < 0: return False

        s = str(x)
        r = "".join([s[i-1] for i in range(len(s), 0, -1)])
        # print(str(r))
        if s == r:
            return True
        else:
            return False

print(isPalindrome(121))            