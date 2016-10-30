```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/data-stream-median
@Language: Markdown
@Datetime: 16-06-15 06:10
```

用两个堆来做：
最大堆，存储排序后的前半段，
最小堆，存储排序后的后半段
如果数字比最大堆的最大值，即是中位数前一个数，那么这个数应该放到后半段。
如果数字比最大堆的最大值小，那么应该放到前半段。
注意放后，保持最大堆和最小堆的平衡。至于要多少平衡，根据是中位数，还是k位数来处理。

代码中的方法，分别加最大和最小堆，然后比较最大堆顶和最小堆顶，是否满足，不满足进行swap就行。