```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/minimum-adjustment-cost
@Language: Markdown
@Datetime: 16-07-04 15:04
```

这个动态规划，坑爹想不出。
数值最大为100，f（i，j）表示将第i个数调整为j时候的最小调整距离。
状态转移为，f(i,j） = min(f(i, j), f(i, k) + abs(j - A[i -1]))，k为上一个数，满足abs(j - k)  = 1。

注意溢出问题!