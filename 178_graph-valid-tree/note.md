```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/graph-valid-tree
@Language: Markdown
@Datetime: 16-06-28 07:11
```

并查集合用来解决这个问题非常合适。
注意最后要保证每个点都连通，也就是边树等于n-1
http://blog.csdn.net/dm_vincent/article/details/7655764

也可以构造图的邻接表表示，然后深度或广度优先遍历，看一个点是否遍历了两次，如果两次就挂。并且保证每个点都被遍历过。