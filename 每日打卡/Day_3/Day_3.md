# 代码随想录算法训练营第 3 天| Leetcode 24. 两两交换链表中的节点, Leetcode 19.删除链表的倒数第 N 个节点, 面试题 02.07. 链表相交, Leetcode 142.环形链表 II

## Leetcode 24. 两两交换链表中的节点

#### 题目链接： [题目](https://leetcode.cn/problems/swap-nodes-in-pairs/)

#### 思路

这道题，其实最主要是 swap 的这个过程，每两个 node 需要 swap，所以我们是一对一对去 increment 我们的 loop。然后在每次的 loop 里，我们 perform 好这个 swap，swap 最重要的是改变 pointer 的顺序，顺序搞不清楚容易断掉。

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null){
            ListNode front = prev.next;
            ListNode back = prev.next.next;

            // swap:
            prev.next = back;
            front.next = back.next;
            back.next = front;

            // increment:
            prev = prev.next.next;

        }
        return dummy.next;
    }
}
```

## Leetcode 19.删除链表的倒数第 N 个节点

#### 题目链接: [题目](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)

#### 思路:

这道题可以用到一个 two pointer 的方法，我们可以算出 fast 和 slow pointer 的 diff 一定是 n + 1， 这样的话，当 fast 到了尽头，我们 slow 也到了可以去删除的地方。这样子省去了很多 if statement 和一些没有必要的 loop 去算长度。

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy;
        ListNode slow = dummy;

        for (int i = 0; i < n; i++){
            fast = fast.next;
        }

        // going together with the same diff;
        while (fast.next != null){
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return dummy.next;
    }
}
```

## 面试题 02.07. 链表相交

#### 题目链接: [题目](https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/description/)

#### 思路：

这道题，主要是知道一个公式。 就是我们用 pa 和 pb 从两头出发，两个一直走，走到头后切换到另一个链表继续走。
两者走的总长度相同，所以会在交点 c1 相遇！

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA = headA;
        ListNode pB = headB;

        while (pA != pB) {
            if (pA == null) {
                pA = headB;
            } else {
                pA = pA.next;
            }

            if (pB == null) {
                pB = headA;
            } else {
                pB = pB.next;
            }
        }

        return pA;

    }
}
```

## Leetcode 142.环形链表 II

#### 题目链接: [题目](https://leetcode.cn/problems/linked-list-cycle-ii/)

#### 思路:

这道题分两个部分：
1） 判断是否是 loop：

这里我们可以用到一个快慢指针，快指针每次走两步，慢指针每次走两步，特定的环形能保证快慢指针一定会 meet，如果在环的情况下。如果没有环，那我们也会 eventually 到 end。

2）如果是 loop 找 intry：
当快慢指针第一次相遇时，slow 走的距离是 fast 的一半。假设 slow 从入口走了 b 步到达相遇点，那么 fast 比 slow 多走的路程刚好是环的整数倍。
这意味着什么？从 head 到入口的距离，等于从相遇点继续往前走到入口的距离（可能要绕几圈）。
所以我们让两个指针分别从 head 和相遇点出发，每次都走一步，它们一定会在入口相遇。因为当第一个指针刚好走到入口时，第二个指针也恰好走完相同的步数到达入口。

```Java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // flast slow pointer;
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow){
                ListNode ptr = head;
                while (ptr != slow){
                    ptr = ptr.next;
                    slow = slow.next;
                }
                return ptr;
            }
        }
    return null;
    }
}
```
