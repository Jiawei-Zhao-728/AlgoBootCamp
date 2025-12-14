# 代码随想录算法训练营第 10 天| Leetcode 232. 用栈实现队列, Leetcode 225. 用队列实现栈, Leetcode 20. 有效的括号, Leetcode 1047. 删除字符串中的所有相邻重复项

## 理论基础

栈和队列的内部实现机制（以 C++ 为例）

## Leetcode 232. 用栈实现队列

#### 题目链接： [题目](https://leetcode.cn/problems/implement-queue-using-stacks/)

#### 思路：

这道题主要思路是用一个 in stack 和一个 out stack，然后每次 push 就 push 到 in，pop 就用 out 去 pop 这样子能完成我们想做的 queue 的要求。

```Java
class MyQueue {
    private Stack<Integer> stackIn;
    private Stack<Integer> stackOut;

    public MyQueue() {
        stackIn = new Stack<>();
        stackOut = new Stack<>();

    }

    public void push(int x) {
        stackIn.push(x);
    }

    public int pop() {
        // make sure that there is stuff to be poped:
        if (stackOut.isEmpty()){
            while(!stackIn.isEmpty()){
                stackOut.push(stackIn.pop());
            }
        }
        return stackOut.pop();
    }

    public int peek() {
        if (stackOut.isEmpty()){
            while(!stackIn.isEmpty()) {
                stackOut.push(stackIn.pop());

            }
        }
        return stackOut.peek();
    }

    public boolean empty() {
        return stackIn.isEmpty() && stackOut.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
```

## Leetcode 225. 用队列实现栈

#### 题目链接: [题目](https://leetcode.cn/problems/implement-stack-using-queues/)

#### 思路:

这道题的思路是，在 push 的时候，我们就通过 rotate，把刚存进去的 element 放在第一位，这样子每次存，我们的顺序都是符合 stack 的顺序。

```Java
class MyStack {

    private Queue<Integer> q;

    public MyStack() {
        q = new LinkedList<>();
    }

    public void push(int x) {
        q.offer(x);
        int size = q.size();
        for (int i = 0; i < size - 1; i ++){
            q.offer(q.poll());
        }

    }

    public int pop() {
        return q.poll();
    }

    public int top() {
        return q.peek();
    }

    public boolean empty() {
        return q.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
```

## Leetcode 20. 有效的括号

#### 题目链接: [题目](https://leetcode.cn/problems/valid-parentheses/)

#### 思路：

这道题就是用 stack 去 track opening 的符号，然后每次遇到 closing 的，我们就 pop 最近的，看看符不符合。有一个比较容易忽略的点就是，最后看看 stack 还有没有东西。

```Java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()){
            // left push:
            if (c == '(') stack.push(')');
            else if (c == '[') stack.push(']');
            else if (c == '{') stack.push('}');

            else{
                if (stack.isEmpty() || c != stack.pop()){
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
```

## Leetcode 1047. 删除字符串中的所有相邻重复项

#### 题目链接: [题目](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/)

#### 思路:

栈顶永远是"上一个字符"，方便和当前字符比较是否相邻重复

```Java
class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()){
            if (!stack.isEmpty() && stack.peek() == c){
                stack.pop();
            }else{
                stack.push(c);
            }
        }

        StringBuilder res = new StringBuilder();
        for (char c : stack){
            res.append(c);
        }

        return res.toString();
    }
}
```

## 总结

### 栈与队列的相互实现

- **232 用栈实现队列**：两个栈（in + out），pop/peek 时如果 out 空就把 in 全倒过去
- **225 用队列实现栈**：一个队列就够了，push 时旋转 `size-1` 次，让新元素到队首

### 栈的经典应用

- **20 有效的括号**：遇到左括号 push 对应的右括号，遇到右括号 pop 检查匹配
- **1047 删除相邻重复项**：栈顶存"上一个字符"，当前字符和栈顶相同就 pop，否则 push

### 核心思想

栈适合**匹配消除**类问题，因为能记录"上一个元素"的状态。队列适合**顺序处理**，用旋转可以实现栈的 LIFO。
