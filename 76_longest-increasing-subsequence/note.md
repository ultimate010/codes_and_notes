```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/longest-increasing-subsequence
@Language: Markdown
@Datetime: 16-07-04 08:53
```

动归的方法：
用一个coount[i]表示第i个数前面有多少个比他小的数，然后后面的数遍历前面的所有数，如果i小于j数，那么可以用上count[i]去计算count[j]。

除了算法一的定义之外，增加一个数组b，b[i]用以表示长度为i最长子序列的最后一个数最小可以是多少。易证：i<j时，b[i]<b[j]。
在二分查找时，一直更新b[]内容，设此时b的总长度为k，
若1. arr[i] >= b[k], 则b[k+1] = arr[i];
若2. arr[i] <  b[k], 则在b[1..k]中用二分搜索大于arr[i]的最小值，返回其位置pos，然后更新b[pos]=arr[i]。

