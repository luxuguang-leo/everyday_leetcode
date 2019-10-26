data structure 
* list (5.1)
  * 删除，查找操作
    * 19.remove-nth-node-from-end-of-list
    * 83 remove duplicates from sorted list
  * 有无环
    * 141 dectct if the list has cycle
    * 142 detect the node of the cycle
  * 合并
    * 21.merge two sorted lists
  * 复制
    * 
  * 变身
    * 24 swap nodes in pairs
    * 61 rotate list 
  * 技巧1.是为了操作头结点，使用dummy结点， dummy = ListNode(0) dummy.next =head
  * 技巧2.使用快慢指针，尤其是针对链表有无环。
  * 技巧3. 在最后结点连接开始结点，形成环，待操作结束之后断开环。
* array (5.1)
  * 26.Remove Duplicates from Sorted Array (使用双标，也就是双指针来操作)
  * 121.Best Time to Buy and Sell Stock
* stack (5.2)
* queue (5.2)
* binary tree (5.3 5.4)
  * 树的构造
  * 树的遍历(DFS：preorder,inorder,postorder, BFS)
    * 使用递归
    * 使用非递归方式来实现
      * preorder最容易，加到stack，非空弹出，记录值，右结点，左结点入栈
      * inorder 的话需要循环将左结点压栈，然后等无左结点，记录值，出栈，
      * postorder可以使用变形的preorder，只是压栈顺序是先左后右，最后结果在逆序即可
  * 平衡二叉树
* heap (5.4)

Algo
* search
  * binary search (5.5)
  * heap seach (5.6)
  * DFS & BFS (5.7 )
  * BST  (5.8)
* sorting algo(5.9 5.10)
  *  bubble sorting
  *  insertion sorting
  *  merge sorting
  *  quick sorting
  *  shell sorting 
 * recrusive & interactive (5.11 5.12)
 * greedy algo  (5.13 5.14)
 * dynamic programing (5.15 5.16)
 * backtracking(combination sums)

复习divide-conque算法 和二分查找问题。

