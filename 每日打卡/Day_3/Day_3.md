# 代码随想录算法训练营第3天|

## Leetcode 203 移除链表元素

#### 题目链接： [题目](https://leetcode.cn/problems/remove-linked-list-elements/)

#### 思路:
思路就是用一个 dummy node 和双指针，去处理头尾节点可能也要被删除的可能性。


```Java
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        // we use a two pointer:
         ListNode dummy = new ListNode(0);
         dummy.next = head;

         ListNode prev = dummy;
         ListNode curr = head;

         while (curr != null){
            if (curr.val == val){
                // 跳过当前节点
                prev.next = curr.next; 
            }else{
                // increment prev
                prev = curr;
            }
            // increment cur
            curr = curr.next; 
         }

         return dummy.next;
    }
}
```

## 707.设计链表

#### 题目链接: [题目](https://leetcode.cn/problems/design-linked-list/)

#### 思路:
这道题，主要有点复杂的就是 add 和 delete，但是具体就是找到 prev 和 next，其实就可以进行一个增加或者删除。


```Java
class MyLinkedList {

    class Node {
        int val; 
        Node prev; 
        Node next; 
        Node (int val) {
            this.val = val;
        }
    }
        private Node head;
        private Node tail;
        private int size;

    public MyLinkedList() {
        head = new Node(0);
        tail = new Node(0);

        head.next = tail; 
        tail.prev = head; 

        size = 0;
    }
    
    public int get(int index) {
         if (index < 0 || index >= size) return -1; 

         Node curr = head.next;
         for (int i = 0; i < index; i ++){
            curr = curr.next;
         }

         return curr.val;
    }

    public void addAtHead(int index, int val){
        if (index < 0 || index > size) {
            return;
        }

        Node prev = head;

        for (int i = 0; i < index; i++) {
            prev = prev.next;
        }
        Node next = prev.next; 

        // insert:
        Node newNode = new Node(val);
        newNode.prev = head;
        newNode.next = next; 
        prev.next = newNode;
        next.prev = newNode;

        size ++; 
    }
    
    public void addAtHead(int val) {
        addAtHead(0, val);
    }

    
    public void addAtTail(int val) {
        addAtHead(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if (index < 0 || index > size) return;


        // find the place to insert: 
        Node prev = head; 
        for (int i = 0; i < index; i ++){
            prev =  prev.next;
        }
        Node next = prev.next;

        // insert:
        Node newNode = new Node (val);
        newNode.prev = prev;
        newNode.next = next;
        prev.next = newNode;
        next.prev = newNode;

    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;

        Node curr = head.next; 
        for (int i = 0; i < index; i++){
            curr = curr.next; 
        }

        curr.prev.next = curr.next; 
        curr.next.prev = curr.prev;
    }
}
```

## Leetcode 206 反转列表

#### 题目链接: [题目](https://leetcode.cn/problems/reverse-linked-list/description/)

#### 思路：

其实这道题用双指针的方法，分为四个步骤，找到 next，反转，更新 prev，更新 next。 但是在处理双指针的时候，容易复杂化指针的变化。



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
    public ListNode reverseList(ListNode head) {
        if (head == null) return null; 

        ListNode prev = null; 
        ListNode curr = head; 

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;

    }
}
```
