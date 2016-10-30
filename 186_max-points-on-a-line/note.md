```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/max-points-on-a-line
@Language: Markdown
@Datetime: 16-06-28 13:42
```

穷举，判断一个点和他在一条线的所有点。通过斜率计算，可以知道是否在一条线上。斜率计算，应该用分数表示更好，因为浮点数除法的非精确性。
分数一定要搞成最简分数，通过除以gcd(a,b)来做。
gcd的方法，如果b为0，那么返回a。否则返回gcd ( b , a % b ),