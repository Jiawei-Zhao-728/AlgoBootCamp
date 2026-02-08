# 代码随想录算法训练营第 48 天 | 第十章 单调栈 part01

## 单调栈入门

今天正式开始单调栈。先做扫盲题和经典题，再对比暴力解与单调栈解法，感受单调栈的巧妙。

## Leetcode 739. 每日温度

#### 题目链接：[题目](https://leetcode.cn/problems/daily-temperatures/)

#### 思路：
单调栈一篇扫盲题，也是经典题。可以读题、想暴力解法，再看单调栈解法，感受单调栈的巧妙。


```Python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append(i) 
        

        return res
```

#### 参考
- [文章讲解](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)

---

## Leetcode 496. 下一个更大元素 I

#### 题目链接：[题目](https://leetcode.cn/problems/next-greater-element-i/)

#### 思路：
本题和 739. 每日温度 看似差不多，其实多加了一点难度。

hashtable + 单调栈


```Python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # for num2, for each elememnt, we store the next greater number:
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1
        
        res = []
        for num in nums1:
            res.append(next_greater[num])

        return res
```

#### 参考
- [文章讲解](https://programmercarl.com/0496.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0I.html)

---

## Leetcode 503. 下一个更大元素 II

#### 题目链接：[题目](https://leetcode.cn/problems/next-greater-element-ii/)

#### 思路：
这道题和 739. 每日温度 几乎如出一辙，可以自己尝试做一做。

这是个环形的，数组，所以为一个的小区别就是 loop 的时候要绕一下，还两次。

```Python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]

            while stack and num > nums[stack[-1]]:
                # we found it:
                prev_i = stack.pop()
                res[prev_i] = num

            if i < n:
                stack.append(i) 

        
        return res
```

#### 参考
- [文章讲解](https://programmercarl.com/0503.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0II.html)

## 总结

