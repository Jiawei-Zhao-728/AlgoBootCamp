# 代码随想录算法训练营第 6 天|

## Leetcode 242.有效的字母异位词

#### 题目链接： [题目](https://leetcode.cn/problems/valid-anagram/)

#### 思路:

这道题，我们用 hashmap 去做。把 s 里面出现过的字母和其字母出现的次数用 hashmap 存起来，然后过一遍 t 看看如果有不在 hash 里面和次数对不对，如果有一个地方不对，就 return false。

在这个代码里，有一个很 clever 的地方就是，当碰到没有的字母，他还是会 return false，因为它会放入一个 0 然后 -1 频率的字母，这样子，更好也满足如果频率小于 0，我们也会 return false。不用说判断这个字母在不在里面。

```Java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> map = new HashMap<>();

        // increment s:
        for (char c : s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        // increment t:
        for (char c : t.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) - 1);
            if(map.get(c) < 0){
                return false;
            }
        }

        return true;
    }
}
```

## Leetcode 349. 两个数组的交集

#### 题目链接: [题目](https://leetcode.cn/problems/intersection-of-two-arrays/description/)

#### 思路:

思路会是用两个 set， 一个 set 来存 nums1 出现过的数字，然后另一个来存所有在 nums2 也在 nums1 的 number。然后把这第二个 set 转成 Array 来 return。

```Java
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        // we add stuff into set1:
        for (int n : nums1){
            set1.add(n);
        }

        // check nums2:
        for (int n : nums2) {
            if (set1.contains(n)){
                set2.add(n);
            }
        }

        int [] res = new int [set2.size()];
        int i = 0;
        for (int n : set2){
            res[i] = n;
            i ++;
        }

        return res;

    }
}
```

## Leetcode 202 快乐数

#### 题目链接: [题目](https://leetcode.cn/problems/happy-number/)

#### 思路：
这里用到 set 的地方主要是存之前见过的 n, 如果见到 n 了，代表我们进入了 loop，就没了，如果遇到 1，我们就成了。然后计算整数和，我们可以用 % 和 / 去用数学的方式去计算。

```Java
class Solution {
    public boolean isHappy(int n) {
        Set <Integer> intset = new HashSet<>();

        // in a loop

        while (n != 1){
            if (intset.contains(n)){
                return false;
            }
            intset.add(n);

            // now calc n:
            int sum = 0;
            while (n > 0 ) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10 ;
            }

            n = sum;
        }

        return true;
    }
}
```


## Leetcode 202 快乐数

#### 题目链接: [题目](https://leetcode.cn/problems/happy-number/)

#### 思路：
这里用到 set 的地方主要是存之前见过的 n, 如果见到 n 了，代表我们进入了 loop，就没了，如果遇到 1，我们就成了。然后计算整数和，我们可以用 % 和 / 去用数学的方式去计算。

```Java
class Solution {
    public boolean isHappy(int n) {
        Set <Integer> intset = new HashSet<>();

        // in a loop

        while (n != 1){
            if (intset.contains(n)){
                return false;
            }
            intset.add(n);

            // now calc n:
            int sum = 0;
            while (n > 0 ) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10 ;
            }

            n = sum;
        }

        return true;
    }
}
```

## Leetcode 1 两数之和

#### 题目链接： [题目](https://leetcode.cn/problems/two-sum/)

#### 思路：
这道题，我们用 hashmap，去解，用key 去存 diff，然后用 val 去存 index


```Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (map.containsKey(nums[i])){
                return new int [] {map.get(nums[i]), i};
            }

            map.put(target - nums[i], i); 
        }
        return new int [] {}; 
    }


}
```