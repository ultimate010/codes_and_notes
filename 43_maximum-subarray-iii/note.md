```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/maximum-subarray-iii
@Language: Markdown
@Datetime: 16-06-18 06:59
```

这个系列问题都是动态规划。
基础版本简单，知道对于当前这个数，要么取，要么留。
2数版本，从左找，从右找，数组保存当前最大。
k数版本就比较难了，需要用g(i,k)表示到i位置取k个数的最大值，l(i,k)表示到i位置，取了i数的最大值。
状态变化为：
l(i,k) = l(i-1, k)+n[i-1]（当前的选中，加入前面的段中）， g(i-1,k-1) + n[i-1]（当前的选中，但是前一个不选中，这个是新的第k段的一个数）
g(i,k) = g(i-1,k)，当前的这个数扔掉，l(i,k)当前这个数选中。