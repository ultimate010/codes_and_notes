```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/backpack
@Language: Markdown
@Datetime: 16-06-13 14:28
```

可以用dfs来做，因为对于每一个item，可以选中和不选中，这样就是一条路径了。深搜完全可以做。应该是O（2^n），因为每一个item两个状态，都要遍历。

另外就是dp的方法，f(i,j）i表示处理到第i个item，j表示当前可以用的容量。显然，如果j大于A[i - 1]，那么可以选中第i个物品，就需要比较选中它和不选中它，哪个更好。分别用状态f(i-1,j - A[i-1]){注意用i-1，表示前i-1个item只能用j - A[i-1]的容量} + V[i - 1]和f(i - 1, j)表示。

