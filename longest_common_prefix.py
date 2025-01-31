def longestCommonPrefix(strs):
    if not strs: return ""
    l_short = min(strs, key=lambda x : len(x))
    strs.remove(l_short)
    for i in range(len(l_short)):
        for elem in strs:
            if l_short[i] != elem[i]:
                return l_short[:i]
    return l_short



# print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))