```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/ugly-number-ii
@Language: Markdown
@Datetime: 16-06-14 11:49
```

解决方法：重点需要记住这种迭代的结构，每一个质数有一个乘积起始位置。迭代的生成最后的数。
或者笨的方法，判断每个数是否是丑数，这个通过判断最大2整除，最大3整除，最大5整除，最后能除完，那么是丑数。