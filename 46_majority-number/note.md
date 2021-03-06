```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/majority-number
@Language: Markdown
@Datetime: 16-06-09 08:43
```

几种解法，hash计数，算是比较简陋的方法。O(n)
排序，然后统计，也算是比较简陋的方法。O(nlogn) + O(n)
类似水贴王的算法，这个比较合适。

寻找主元素的3种算法 

定义：如果一个元素的出现次数超过了数组长度的一半，这个元素就叫做主元素 

寻找主元素 的算法有3种。 
第一种，编程之美上的，O（n）的，没什么好说的。 

第二种，如果我们将数组排序，排序以后，中间的那个数，一定是主元素。也就是说，数组的中位数就是主元素。 
寻找数组里的第k大，有O（n）的算法。 

第三种，分治法。 
分治是递归的一种思路，先假定子问题可以解决，然后物尽其用，尽最大努力利用子问题的答案来解决原问题。 
假设数组a的长度是n，令m=n/2，那么，考虑它的两个子问题：寻找a[1..m],和a[m+1..n]的主元素。 
假设我们已经知道了这两个子问题的答案了，就是k和p，然后我们现在要解决原问题。 
考虑一下，子问题的答案跟原问题的答案有些什么关系呢？ 
其中一个关系就是，原数组的主元素，必定是k或者p。你看，子问题的解和原问题的解产生了联系了！ 
有了这个结论，我们就可以，把整个a扫描一次，看看k和p出现的次数哪一个大，大的那一个，就是a的主元素了。 
复杂度为 T(n) = 2 * T(n/2) + O(n) 也就是O(nlogn)