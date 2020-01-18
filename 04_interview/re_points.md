# OS复习点
## C语言

1. static

   1. static function, 意味着此函数只在此文件内部使用(obj file)，对外隐藏
   2. static global varibale，放在文件中的变量，只在这个文件内部使用，但是生命周期是整个
   3. static local variable, 函数中，作用范围是函数，生命周期是整个

2. 各个段的作用

   1. text，程序
   2. rodata, constant data
   3. data，已经初始过得数据，global变量，或者static变量
   4. bss，未初始化数据
   5. heap，一般从BSS结束点开始，数据动态内存范围，malloc,relloc, free, brk, sbrk， 被所有thread, lib, process所使用
   6. stack，LIFO结构，Stack pointer指向栈顶，

3. volatile使用

   1. 告诉编译器此变量容易改变，不要做优化，这样调用此变量系统会从地址读取次变量而不是从寄存器
   2. 一般用在外设寄存器变量
   3. 容易被中断改变的全局变量
   4. 多task会使用的全局变量

4. printf实现（VA_START）

   1. va_list, va_start, va_end: 
   2. va_list表示可变参数列表类型，实质是char指针
   3. va_start表示用于获取可变参数列表的首指针
   4. va_arg表示获取当前ap所指的可变参数并将ap指针移向下一个可变参数
   5. va_end结束对可变参数的处理

5. 预编译宏定义

6. 指针

7. 大小端

   1. 大端数据高位存在地址的低位，如0x12345678, 如果内存分别为0x4000~0x4003分别为低地址和高地址，那么大端的存储应该是：0x4000：0x12   0x4001:0x34 0x4002:0x56 0x4003:0x78. 如果小端那么高位数据应该存在地址的高位。0x4000:0x78 0x4001:0x56 0x4002:0x34 0x4003:0x12

   2. 实现C语言大小端，

      1. int i = 1; char* p = (char*)&i; if (*p == 1) "Little Endian" else "big endian"，解释，int占四个字节，强转只取低地址，大端的内存排列方式应该是(从低到高):00  00 00 01， 因为01是数据低位，存在最高位置，强转之后取低地址00，大端，如果是小端内存分布应该是:01 00 00 00，强转之后取01

      2. 利用联合： 

         ```c
         
         ```

         int checkEndian( )

         {

         		union{

         		     unsigned int a;

                      unsigned char b;        

                }c;

                c.a = 1;

               return (c.b == 1);

         }

         如果为True，1代表是 little-endian, 0 代表big-endian,利用了union的所有成员都是从低地址开始排列。

         ```
         
         ```

                  4000  4001 4002  4003

      a大端    00       00     00       01

      a小端    01      00      00       00

                    b

   3. 网络字节序，X86， ARM小端，powerPC大端，网络字节序大端

## OS
1. 使用过的RTOS

2. 区别和异同点

3. 调度算法

4. thread和task的区别

5. 中断

6. linux常用命令

7. MMU的作用

   1. 如果没有MMU，地址索引就是物理地址，会有一些内存问题

   2. 如果有MMU，程序使用的虚拟地址，MMU会将虚拟地址和物理地址对应，做到了隔离。

      1. 操作系统在初始化中分配、释放和访问时会执行一些指令在物理内存中填写页表，然后设置MMU，告诉MMU表在物理内存中什么位置
      2. 设置好之后，CPU每次访问内存地址都会触发MMU做查表和地址转换，地址转换有硬件完成，不需要指令控制去做。
      3. 多了一层VA到PA的转换，好处就是内存保护作用，物理地址不连续，转换为VA，变成方便。


## 算法
1. bit操作
https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently

   a. 寻找数组中不同的数，

   ```c
   int singleNumber(int* nums, int numsSize){
       if(nums == NULL){
           return NULL;
       }
       int ret = 0;
       for(int i = 0; i < numsSize; i++){
           ret ^= nums[i];
       }
       return ret;
   }
   ```

   b. find the number among the nums, other numbers appear three times, 
      [3,1,3,3] return 1  [0, 1, 0, 1, 01, 99], return 99, count every bits, if the bits cnt, %3 and result is the bit value
   ```c
  int singleNumber(int* nums, int numsSize){
      int ret = 0;
      for(int i = 0; i < 32; i++){
          int bit_cnt = 0;
          for(int j = 0; j < numsSize; j++){
              bit_cnt += (nums[i] >>i)&0x01;
          }
          ret |= ((bit_cnt%3)<<i);
      }
      return ret;
   }
   ```
   c.count bits of a nums
   ```c
   int cnt_1s(int n){
       int ret = 0;
       while(n){
           n = n & (n-1);
           ret++；
       }
       return ret;
   }
   ```

2. 逆序一个linked-list

   ```c
   struct ListNode* reverseList(struct ListNode* head){
       if(head == NULL || head->next == NULL)
           return head;
       struct ListNode* pre = NULL;
       struct ListNode* cur = head;
       struct ListNode* next;
       while (cur != NULL){
           next = cur->next;
           cur->next = pre;
           pre = cur;
           cur = next;
       }
       return pre;
   }
   ```

3. 使用两个stack实现一个queue


## 英语准备
## project
1. ADK stack porting
2. 


## expertise in bluetooth
1. 5 years in BLUETOOTH/BLE, short range wireless embeded area
2. Expertise in Bluetooth stack, firmware, SDK from bottom to top
3. Participate in bluetooth chipset firmware development, mainstream consumer product support
4. Participate in open-source OS project, AliOS Things, owner of BLE stack, BLE SDK
5. Various experience in embeded projects, good at trouble shooting, low-level issue
