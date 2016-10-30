```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/kth-smallest-number-in-sorted-matrix
@Language: Markdown
@Datetime: 16-06-29 13:14
```

有点trick，用堆，保证每次出来的都是最小的，然后放入ret，看ret够了没。出来东西后，然后需要添加一个大的数进去，方法是每一行有个列指针。