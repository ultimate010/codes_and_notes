```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/distinct-subsequences
@Language: Markdown
@Datetime: 16-06-13 11:25
```

状态转义，定义f(i, j)为t[:j]在s[:i] 中出现的次数。
如果s[i] == t[j]
分为使用s中的i 加上 不是用s中的i
那么可以表示成t[:j-1]在s[:i-1]出现次数即f(i-1,j-1) + T[:j]在s[:i-1]出现的次数f(i-1,j)
如果不等，那么即不使用s中的i。
f(i,j) = T[:j]在s[:i-1]出现的次数f(i-1,j)