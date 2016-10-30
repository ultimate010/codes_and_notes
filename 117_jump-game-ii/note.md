```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/jump-game-ii
@Language: Markdown
@Datetime: 16-06-10 07:52
```

贪心，从后面贪心回来，每次跳最长。
dp，递推公式为，跳到当前需要的次数为min（直接跳到当前，通过j点+1次跳跃而来(看从j点能否跳跃过来)）