```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/k-sum
@Language: Markdown
@Datetime: 16-06-18 08:46
```

动态规划，注意状态表示dp[i][j][k]，表示从n[:i + 1]中选j个，然后和为k的个数。
状态转移比较容易，就是选当前和不选当前的区别。
