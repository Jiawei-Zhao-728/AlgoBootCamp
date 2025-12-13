# 代码随想录算法训练营第 9 天| Leetcode 151. 翻转字符串里的单词, 卡码网 55. 右旋转字符串, Leetcode 28. 实现 strStr(), Leetcode 459. 重复的子字符串

## Leetcode 151. 翻转字符串里的单词

#### 题目链接： [题目](https://leetcode.cn/problems/reverse-words-in-a-string/)

#### 思路：

这道题，最主要是我们要从 end iterate 到 beginning 但是每次遇到空格的时候，我们要把那个单词抽离出来，然后存到 result 里面。这里面比较 tricky 的就是写代码的格式，和处理一些可能遇到的 corner case。

```Java
class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        int right = s.length() - 1;

        while (right >= 0){
            // we jump over the space:
            while (right >= 0 && s.charAt(right) == ' ') {
                right --;
            }
            // possible it's all space after wards:
            if (right < 0) break;

            // then we encounter a word
            int end = right;
            while (right >= 0 && s.charAt(right) != ' '){
                right --;
            }

            int start = right + 1;

            // then we append this word into the res:
            if (res.length() != 0){
                res.append(' ');
            }
            res.append(s.substring(start, end + 1));


        }

        return new String(res);
    }
}
```

## 卡码网 55. 右旋转字符串

#### 题目链接: [题目](https://kamacoder.com/problempage.php?pid=1065)

#### 思路:

这道题的核心思路就是找到那个分割线在哪里，这个分割线我们通过 k 来找到后，我们就可以一次先把右边的部分放进去，然后把左边的放进去。

```Java
import java.util.*;

public class Main {
    public String rotateString(String s, int k) {
        StringBuilder sb = new StringBuilder();
        // TODO: 实现右旋转逻辑
        int margin_r = s.length() - k;
        int margin_l = margin_r - 1;
        int cur = 0;

        while (margin_r < s.length()){
            sb.append(s.charAt(margin_r));
            margin_r ++ ;
        }

        while (cur <= margin_l){
            sb.append(s.charAt(cur));
            cur ++;
        }


        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();     // 读取 k
        String s = sc.next();     // 读取字符串

        Main main = new Main();
        String result = main.rotateString(s, k);
        System.out.println(result);

        sc.close();
    }
}
```

## Leetcode 28. 实现 strStr()（KMP，可跳过）

#### 题目链接: [题目](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)

#### 思路：

```Java

```

## Leetcode 459. 重复的子字符串（KMP，可跳过）

#### 题目链接: [题目](https://leetcode.cn/problems/repeated-substring-pattern/)

#### 思路:

```Java

```

## 字符串总结

### 核心认知

字符串本质上是**字符数组**，所以数组的技巧（双指针、滑动窗口）都可以用。

### 常用操作

| 操作          | 方法                                  |
| ------------- | ------------------------------------- |
| **反转**      | 双指针，左右往中间走，swap            |
| **拼接/修改** | `StringBuilder`（Java String 不可变） |
| **子串提取**  | `s.substring(start, end)`             |
| **字符遍历**  | `s.toCharArray()` 或 `s.charAt(i)`    |

### 题型总结

1. **反转类**（344、541、151）：双指针是核心，注意区间边界
2. **旋转类**（55）：找分割点，分段处理
3. **替换类**（54）：StringBuilder 拼接
4. **匹配类**（28、459）：KMP 算法（进阶，一刷可跳过）

### 常见坑

- Java 的 `String` 是 immutable，频繁修改要用 `StringBuilder`
- `substring(start, end)` 是左闭右开 `[start, end)`
- 处理空格时注意**连续空格**和**首尾空格**

## 双指针回顾
其实主要是一个处理双指针关系和怎么动的一个逻辑问题。