# 代码随想录算法训练营第 7 天| Leetcode 454. 四数相加 II, Leetcode 383. 赎金信, Leetcode 15. 三数之和, Leetcode 18. 四数之和

## Leetcode 454. 四数相加 II

#### 题目链接： [题目](https://leetcode.cn/problems/4sum-ii/)

#### 思路：

这道题其实就是分开处理前两个和后两个

```Java
class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        // 这道题我们会用到hashmap：
        HashMap <Integer, Integer> map = new HashMap<>();
        int count = 0;

        // 先处理 nums1 和 nums2：
        for (int i : nums1){
            for (int j : nums2){
                int comb = i + j;
                map.put(comb, map.getOrDefault(comb, 0) + 1);
            }
        }
        for (int i : nums3) {
            for (int j : nums4){
                int comb = -(i + j);
                count += map.getOrDefault(comb, 0);
            }
        }
        return count;
    }
}
```

## Leetcode 383. 赎金信

#### 题目链接: [题目](https://leetcode.cn/problems/ransom-note/)

#### 思路:

这道题其实很相等，我们把 magazine 里面的 char 和出现次数建立一个 hashmap 去存起来，然后，然后 iterate ransomnote，decrement 出现的次数，如果有次数是 0，那么就 return false。

```Java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) return false;

        HashMap <Character, Integer> map = new HashMap <> ();
        // get the chars in ransom note:
        for (char i : magazine.toCharArray()){
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        // now look at the ransomNote:
        for (char c: ransomNote.toCharArray()){
            int count = map.getOrDefault(c, 0);
            if (count == 0) return false;
            map.put(c, count - 1);

        }

        return true;
    }
}
```

## Leetcode 15. 三数之和

#### 题目链接: [题目](https://leetcode.cn/problems/3sum/)

#### 思路：

这道题用到 sort 和双指针，但其实，最主要就是，这道题，我们需要去 jump over duplicate，不然的话答案容易多算。

```Java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // sort, 双指针：
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i ++){
            // jump over duplicate:
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int mid = nums[i];
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = mid + nums[left] + nums[right];

                if (sum == 0){
                    result.add(Arrays.asList(mid, nums[left], nums[right]));

                    // jumping over dup:
                    while (left < right && nums[left] == nums[left + 1]) left ++;
                    while (left < right && nums[right] == nums[right - 1]) right --;

                    left ++;
                    right --;

                }else if (sum < 0){
                    left ++;
                }else{
                    right --;
                }
            }


        }

        return result;

    }
}
```

## Leetcode 18. 四数之和

#### 题目链接: [题目](https://leetcode.cn/problems/4sum/)

#### 思路:

这道题，其实我觉得用 recursion 去 come up with a solution 是可以 ksum 的比较重要。已经是有点像一个 backtracking 的问题了。

```Java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List <List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        ksum(nums, 4, 0, target, new ArrayList<>(), res);
        return res;
    }

    private void ksum (int[]nums, int k, int start, long target, List<Integer> quad, List<List<Integer>> res){

        // base case: when k = 2:
        if (k == 2){
            int l = start, r = nums.length - 1;
            while (l < r){
                long sum = nums[r] + nums[l];
                if (sum > target){
                    r --;
                }else if (sum < target){
                    l ++;
                } else{
                    List<Integer> found = new ArrayList<>(quad);
                    found.add(nums[l]);
                    found.add(nums[r]);
                    res.add(found);
                    l ++;
                    while(l < r && nums[l] == nums[l - 1]) l++;

                }
            }
            return;
        }else{
            // recursive step:
             for (int i = start; i < nums.length; i++){
                if (i > start && nums[i] == nums[i - 1]) continue;
                quad.add(nums[i]);
                ksum(nums, k - 1, i + 1, target - nums[i], quad, res);
                quad.remove(quad.size() - 1);
             }
        }

    }
}
```

## 总结

今天的题目主要围绕**哈希表**和**双指针**两种方法：

### 哈希表系列（454、383）

- **454 四数相加 II**：因为是四个独立数组，不需要去重，所以可以用 HashMap 分组处理（前两个一组，后两个一组），时间复杂度从 O(n⁴) 降到 O(n²)
- **383 赎金信**：和 Day 6 的 242 有效的字母异位词思路一样，HashMap 存频率，decrement 检查

### 双指针系列（15、18）

- **15 三数之和**：排序 + 双指针，核心难点是**去重**（跳过相同元素），不然答案会重复
- **18 四数之和**：可以用递归写成通用的 **kSum** 模板，类似 backtracking 的思想。注意 target 要用 `long` 防止溢出

### 454 vs 18 的区别

- 454 是四个**独立数组**，元素不会重复使用，用哈希表更简单
- 18 是**同一个数组**，需要去重 + 不能重复使用同一位置元素，双指针更合适

### 关键技巧

1. 看到 **n 数之和** 类型题，先想能不能排序 + 双指针
2. **去重**的关键：`if (i > start && nums[i] == nums[i-1]) continue`
3. HashMap 适合**不需要去重**的场景，双指针适合**需要去重**的场景
