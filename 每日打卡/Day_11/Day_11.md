# 代码随想录算法训练营第 11 天| Leetcode 150. 逆波兰表达式求值, Leetcode 239. 滑动窗口最大值, Leetcode 347. 前 K 个高频元素

## Leetcode 150. 逆波兰表达式求值

#### 题目链接： [题目](https://leetcode.cn/problems/evaluate-reverse-polish-notation/)

#### 思路：

这道题其实我们就是用一个 stack 去存数字，然后每次遇到一个符号，我们用这个符号去运算 stack 头的两个数字。

```Java
class Solution {
    public int evalRPN(String[] tokens) {
        Stack <Integer> stack = new Stack<>();


        for (String token : tokens){
            if (token.equals("+") || token.equals("-") || token.equals("/") || token.equals("*")){
                int b = stack.pop();
                int a = stack.pop();

                if (token.equals("+")) stack.push(a + b);
                else if (token.equals("-")) stack.push(a - b);
                else if (token.equals("*")) stack.push(a * b);
                else stack.push(a / b);


            } else{
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }
}
```

## Leetcode 239. 滑动窗口最大值（有点难度，一刷至少理解思路）

#### 题目链接: [题目](https://leetcode.cn/problems/sliding-window-maximum/)

#### 思路:

这道题比较 clever 的地方就是用一个 dequeue 去存这个下标，然后让头永远是最大的那个 element 的下标。这样子我们的值又存好了，然后也可以 track 这个 window 的位置。

```Java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int [] res = new int[n - k + 1];
        Deque<Integer> deque = new LinkedList<>();

        for (int i = 0; i < n; i ++){
            // 移除队尾：
            if (!deque.isEmpty() && deque.peekFirst() < i - k + 1){
                deque.pollFirst();
            }

            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]){
                deque.pollLast();
            }

            deque.offerLast(i);

            // if the size is right:
            if(i >= k - 1){
                res[i - k + 1] = nums[deque.peekFirst()];

            }
        }

        return res;
    }
}
```

## Leetcode 347. 前 K 个高频元素（有点难度，一刷至少理解思路）

#### 题目链接: [题目](https://leetcode.cn/problems/top-k-frequent-elements/)

#### 思路：

这道题巧妙在，会用到两个 data structure，一个 priority queue 和一个 hashmap，用 hashmap 来存出现评论，然后用 heap 来根据出现频率排序。

```Java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map <Integer, Integer> map = new HashMap<>();
        for (int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1 );
        }

        // small stack:
        PriorityQueue <Integer> heap = new PriorityQueue<>(
            (a, b) -> map.get(a) - map.get(b)
        );

        for ( int num : map.keySet()){
            heap.offer(num);
            if (heap.size() > k){
                heap.poll();
            }
        }

        int [] res = new int [k];
        for (int i = 0; i < k; i ++){
            res[i] = heap.poll();
        }

        return res;
    }
}
```

## 栈与队列总结

### 栈的应用

- **150 逆波兰表达式求值**：栈存数字，遇到运算符弹出两个数运算，结果再入栈

### 队列的高级应用

- **239 滑动窗口最大值**：双端队列（Deque）存**下标**，保持队头是窗口最大值。关键：队尾维护单调递减，队头检查是否出窗口
- **347 前 K 个高频元素**：HashMap 统计频率 + PriorityQueue（小顶堆）维护 top K

### 核心技巧

- **单调队列**：用 Deque 维护窗口最值，O(n) 时间复杂度
- **优先级队列（堆）**：找 top K 问题的经典解法，小顶堆维护 K 个最大元素
- **栈 + 队列组合**：HashMap 统计 + 堆排序，解决频率相关的问题

### 一句话

栈适合**表达式求值**，队列适合**滑动窗口**，堆适合**top K**。
