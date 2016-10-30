```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/single-number
@Language: Markdown
@Datetime: 16-06-09 07:43
```

如果求一个数的时候，此题根据异或操作可以将相同的数变为0，不同的变为存在，0^a = a
两个数的时候，所有的异或c=a^b，找到c中为1的一位，那么其中a为0b为1或者a为1b为0，将原数据分为两组，每组在进行同样的操作，找到a和b。
