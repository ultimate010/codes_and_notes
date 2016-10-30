```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/implement-queue-by-two-stacks
@Language: Markdown
@Datetime: 16-08-05 13:35
```

容易想到的就是每次入都放到s1，出的时候，s1导入s2，然后出队后，倒回s1.
可以优化的是，s2当作出对buffer。如果s2不为空，不需要把s1导入s2， 因为s2的顺序是和出队顺序一致。所以出队后不需要导入s1.