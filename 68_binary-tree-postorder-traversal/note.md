```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-postorder-traversal
@Language: Markdown
@Datetime: 16-06-15 14:34
```

非递归的时候，一种算法是设置一个状态表示第一次进栈还是第二次进栈。如果第一次，接着push，然后从右儿子开始处理。