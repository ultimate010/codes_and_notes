# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/nuts-bolts-problem
@Language: Python
@Datetime: 16-06-29 13:53
'''

# class Comparator:
#     def cmp(self, a, b)
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        def qsort(nuts, bolts, l, r, compare):
            if l < r:
                pat1 = partition(nuts, bolts[l], l, r, compare)
                pat2 = partition(bolts, nuts[pat1], l, r, compare)
                qsort(nuts, bolts, l, pat1 - 1, compare)
                qsort(nuts, bolts, pat1 + 1, r, compare)
        
        def partition(arr, pivot, l, r, compare):
            if l >= r:
                return l
            for i in range(l, r + 1):
                if compare.cmp(arr[i], pivot) == 0 or compare.cmp(pivot, arr[i]) == 0:
                    arr[l], arr[i] = arr[i], arr[l]
                    break
            p = arr[l]
            while l < r:
                while l < r and (compare.cmp(arr[r], pivot) == 1 or compare.cmp(pivot, arr[r]) == -1):
                    r -= 1
                arr[l], arr[r] = arr[r], arr[l]
                while l < r and (compare.cmp(arr[l], pivot) == -1 or compare.cmp(pivot, arr[l]) == 1):
                    l += 1
                arr[l], arr[r] = arr[r], arr[l]
            arr[l] = p
            return l
            
        if not nuts or not bolts:
            return
        if len(nuts) != len(bolts):
            return 
        
        qsort(nuts, bolts, 0, len(bolts) - 1, compare)
        