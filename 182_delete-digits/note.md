```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/delete-digits
@Language: Markdown
@Datetime: 16-06-10 05:53
```

动态规划，状态为
*         (m, n) = min((m-1, n-1), (m-1, n))
*         min(del current, or del before)


贪心法
