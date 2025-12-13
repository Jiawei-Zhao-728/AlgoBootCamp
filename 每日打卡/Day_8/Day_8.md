# 代码随想录算法训练营第 8 天| Leetcode 344. 反转字符串, Leetcode 541. 反转字符串 II, 卡码网 54. 替换数字

## Leetcode 344. 反转字符串

#### 题目链接： [题目](https://leetcode.cn/problems/reverse-string/)

#### 思路：

这道题用 two pointer，左和右，然后左和右 pointer 都从左右往中间移动，然后互相 swap。

```Java
class Solution {
    public void reverseString(char[] s) {
        // use two pointer:
        int l = 0, r = s.length - 1;

        while (l <= r){
            char templ = s[l];
            s[l] = s[r];
            s[r] = templ;
            l ++;
            r --;
        }
    }
}
```

## Leetcode 541. 反转字符串 II

#### 题目链接: [题目](https://leetcode.cn/problems/reverse-string-ii/)

#### 思路:

这道题主要是有点被题目的描述绕进去了，我一开始的直觉是在 2k 个的时候，我们要去 swap 前面 k 个，这样子的话其实会复杂，但是其实我们不需要往左边看，看 next k 就行，这样子我们的判断条件就简单很多。

```Java
class Solution {
    public String reverseStr(String s, int k) {
        // how to calc k:
        int cur_pos = 0;
        char[] arr = s.toCharArray();  // 先转成 char[]

        while (cur_pos < s.length()){
            // cur_pos arrive at a 2k:
            System.out.println("Current position: " + cur_pos);
            int next_k = Math.min(s.length(), cur_pos + k);

            // swap:
            int l = cur_pos, r = next_k - 1;
            while (l <= r){
                char templ = arr[l];
                arr[l] = arr[r];
                arr[r] = templ;
                l ++;
                r --;
            }


            cur_pos += (2*k);

        }

        return new String(arr);

    }
}
```

## 卡码网 54. 替换数字

#### 题目链接: [题目](https://kamacoder.com/problempage.php?pid=1064)

#### 思路：

这道题主要是一个字母和数字的判断。这道题我觉得比较重要的就是用到了 java 的 stringBuilder，因为是一个 mutable 的 string，非常方便。

```Java
import java.util.*;

public class Main {
    public String replaceNumber (String s) {
        StringBuilder sb = new StringBuilder();

        for ( char c : s.toCharArray()){
            if (Character.isDigit(c)){
                sb.append("number");
            }else{
                sb.append(c);
            }
        }

        return sb.toString(); 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next(); 
        Main main = new Main();
        String result = main.replaceNumber(s);
        System.out.println(result); 
        
        sc.close();

    }

}
```

## 总结

### 核心技巧

- **双指针反转**：左右指针往中间走，swap，字符串反转的基础操作
- **区间处理**：541 的关键是往右看 next k，而不是往左看，简化判断条件
- **StringBuilder**：Java 中处理可变字符串的利器，拼接效率高

### 一句话

字符串问题本质上就是**数组问题** + **字符处理**，双指针依然是核心。
