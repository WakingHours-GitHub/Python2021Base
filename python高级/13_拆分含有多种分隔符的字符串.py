# 我们需要把某个字符串根据不同分隔符拆分成不同的字段.

s = 'hs,i|uags;df\tsg;qwesdeff'
# solution1: 使用str.split()方法, 每次处理一种分隔符.
# solution2: 使用正则表达式: re.split()一次性完成字符串分割.


def longestPalindrome(s: str) -> str:
    if len(s) == 1 or s == s[::-1]:
        return s
    # sliding window
    l = len(s)
    for window in range(l-1, 0, -1):
        print(window, ": ")
        for i in range(0, l-window+1):
            print("\t", i, s[i: window + i], s[window + i - 1: i-1 if i else None: -1])
            if s[i: window + i] == s[window + i - 1: i-1 if i else None: -1]:
                return s[i: window + i]


print(longestPalindrome("babad"))

