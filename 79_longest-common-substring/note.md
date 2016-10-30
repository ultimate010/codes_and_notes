```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-common-substring
@Language: Markdown
@Datetime: 16-07-04 08:29
```

匹配上就是f[i - 1][j - 1] + 1，否则为0，从新开始。
