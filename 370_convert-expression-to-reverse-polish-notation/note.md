```
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/convert-expression-to-reverse-polish-notation
@Language: Markdown
@Datetime: 16-06-23 11:26
```

遇到数字，直接输出。
遇到（进栈。
遇到），出栈，直到）
遇到操作符号，把栈中的优先级大的符号先出栈，然后再进栈。

中缀表达式翻译成后缀表达式的方法如下：

（1）从右向左依次取得数据ch。

（2）如果ch是操作数，直接输出。

（3）如果ch是运算符（含左右括号），则：
      a：如果ch = '('，放入堆栈。
      b：如果ch = ')'，依次输出堆栈中的运算符，直到遇到'('为止。
      c：如果ch不是')'或者'('，那么就和堆栈顶点位置的运算符top做优先级比较。
          1：如果ch优先级比top高，那么将ch放入堆栈。
          2：如果ch优先级低于或者等于top，那么输出top，然后将ch放入堆栈。

（4）如果表达式已经读取完成，而堆栈中还有运算符时，依次由顶端输出。

如果我们有表达式(A-B)*C+D-E/F，要翻译成后缀表达式，并且把后缀表达式存储在一个名叫output的字符串中，可以用下面的步骤。

（1）读取'('，压入堆栈，output为空
（2）读取A，是运算数，直接输出到output字符串，output = A
（3）读取'-'，此时栈里面只有一个'('，因此将'-'压入栈，output = A
（4）读取B，是运算数，直接输出到output字符串，output = AB
（5）读取')'，这时候依次输出栈里面的运算符'-'，然后就是'('，直接弹出，output = AB-
（6）读取'*'，是运算符，由于此时栈为空，因此直接压入栈，output = AB-
（7）读取C，是运算数，直接输出到output字符串，output = AB-C
（8）读取'+'，是运算符，它的优先级比'*'低，那么弹出'*'，压入'+"，output = AB-C*
（9）读取D，是运算数，直接输出到output字符串，output = AB-C*D
（10）读取'-'，是运算符，和'+'的优先级一样，因此弹出'+'，然后压入'-'，output = AB-C*D+
（11）读取E，是运算数，直接输出到output字符串，output = AB-C*D+E
（12）读取'/'，是运算符，比'-'的优先级高，因此压入栈，output = AB-C*D+E
（13）读取F，是运算数，直接输出到output字符串，output = AB-C*D+EF
（14）原始字符串已经读取完毕，将栈里面剩余的运算符依次弹出，output = AB-C*D+EF/-
