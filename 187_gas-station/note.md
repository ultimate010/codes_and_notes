```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/gas-station
@Language: Markdown
@Datetime: 16-06-09 10:43
```


其实很简单，就是如果最后总的gas大于总的cost，才会有解，从每个点尝试，如果失败，从下一个点出发，重新尝试，没必要走完整个路径。

> 分析：其实只要总的汽油量要大于总的消耗量，那么肯定是有解的，可以从头遍历起，什么时候汽油量小于消耗量了，就假设从下一个点重新开始。