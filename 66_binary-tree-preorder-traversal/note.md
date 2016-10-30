```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/binary-tree-preorder-traversal
@Language: Markdown
@Datetime: 16-06-11 10:53
```

注意非递归解法，用一个stack，然后先压入right，然后再压入right。
或者同时使用root和stack，判断root是否为None和stack是否为空。先左到低，然后弹出右儿子。处理右儿子的事情。
