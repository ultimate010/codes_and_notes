```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/edit-distance
@Language: Markdown
@Datetime: 16-06-13 11:01
```

当前位置可以有前一个：
删一个字符，增一个字符，改一个字符
而来，分别对应状态：
m[row][col -1] m[row-1][col] m[row-1][col-1]

