from functools import lru_cache
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.l = []
        self.res = []

    #插入排序，时间复杂度为O(n^2),稳定排序，
    def insert_sort(self, l):
        for i in range(1, len(l)):
            temp = l[i]
            j = i - 1
            while j >= 0 and temp < l[j]:
                l[j+1] = l[j]
                j -= 1
            l[j+1] = temp
        return l
    
    #冒泡排序，遍历n-1趟，每次把最小的冒泡到最前面，时间复杂度O(n^2),稳定排序
    def bubble_sort(self, l):
        for i in range(len(l) - 1):
            for j in range(len(l)-1, i, -1):
                if l[j] < l[j-1]:
                    l[j], l[j-1] = l[j-1], l[j]
        return l

    def quick_sort(self, l, st, end):
        if st >= end:
            return
        key = l[st]
        index = st
        for i in range(st + 1, end):
            if l[i] < key:   
                index += 1
                l[i], l[index] = l[index], l[i]
        for j in range(st, index):    #稳定排序
            l[j] = l[j+1]
        l[index] = key
        self.quick_sort(l, st, index)
        self.quick_sort(l, index+1, end)
    
    #归并排序
    def mergesort(self, seq):
        if len(seq) <= 1:
            return seq
        mid = len(seq) // 2  # 将列表分成更小的两个列表
        left = self.mergesort(seq[:mid])
        right = self.mergesort(seq[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        #合并两个已排序好的列表，产生一个新的已排序好的列表
        result = []  
        i = 0  
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result



    #数组中的重复数字，原地调整
    def findRepeatNumber(self, nums):
        if not nums:
            return False
        else:
            for i in range(len(nums)):
                while nums[i] != i:
                    if nums[i] == nums[nums[i]]:
                        return nums[i]
                    else:   #交换两个数的值，下标容易出错
                        #nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                        temp = nums[i]
                        nums[i] = nums[nums[i]]
                        nums[temp] = temp     
            return False
    
    #二维数组中的查找，利用数组的有序性右上角开始搜
    def findNumberIn2DArray(self, matrix, target):
            if not matrix:
                return False
            hang = len(matrix)
            lie = len(matrix[0])
            i = 0
            j = lie - 1
            while i < hang and j >= 0:
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    j -= 1
                else:
                    i += 1
            return False
    #替换空格，直接replace函数...  
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')
    #遍历字符串
    def replaceSpace1(self, s: str) -> str:
        l = ''
        for letter in s:
            if letter == ' ':
                l += '%20'
            else:
                l += letter
        return l
    
    #从尾到头打印链表
    def reversePrint(self, head):
        if not head:
            return []
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l[::-1]
    
    #递归调用
    def reversePrint(self, head):
        if not head:
            return []
        else:
            l = []
            l.extend(self.reversePrint(head.next))
            l.append(head.val)
            return l
    
    #头插法
    def reversePrint(self, head):
        if not head:
            return []
        else:
            newnode = ListNode('#')
            newnode.next = None
            while head:
                temp = ListNode(head.val)
                temp.next = newnode.next
                newnode.next = temp
                head = head.next
            t = newnode.next
            l = []
            while t:
                l.append(t.val)
                t = t.next
            return l

    #笔试题，文件依赖顺序   
    def compileSeq(self, input):
        l = list(map(int, input.split(',')))
        s = []
        index = 0
        for i in range(len(l)):
            if l[i] == -1:
                s.append(i)
                index += 1
        n = len(l) 
        while index < n:
            for j in s:
                for i in range(n):  
                    if l[i] == j:
                        s.append(i)
                        index += 1
        return s

    #重建二叉树
    #前中序构建树
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        else:
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
            root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
            print(root.val, end = ' ')
            return root
    #中后序遍历
    #知道前后序列无法确定树的结构！
    def buildTree1(self, lastorder, inorder):
        if not lastorder:
            return None
        else:
            root = TreeNode(lastorder[-1])
            index = inorder.index(lastorder[-1])
            root.left = self.buildTree1(lastorder[:index], inorder[:index])
            root.right = self.buildTree1(lastorder[index:-1], inorder[index+1:]) 
            print(root.val, end = ' ')   
            return root                

    #层次遍历：
    def buildTree2(self, root):
        if not root:
            return None
        else:
            l = []
            l.append(root)
            while l:
                s = l.pop(0)
                print(s.val, end = ' ')
                if s.left:
                    l.append(s.left)
                if s.right:
                    l.append(s.right)

    #层次遍历二叉树，输出为二维列表，列表中每个元素为一层
    def levelOrder(self, root):  #-> List[List[int]]:
        if not root:
            return []
        l = []
        s = []
        l.append(root)
        while l:
            t = []
            cunt = len(l)
            while cunt:
                temp = l.pop(0)
                t.append(temp.val)
                if temp.left:
                    l.append(temp.left)
                if temp.right:
                    l.append(temp.right)
                cunt -= 1
            if t:
                s.append(t)
        return s

    #分层遍历二叉树，递归来做，思路简直666===树高度太大，递归太深
    def levelOrder(self, root: TreeNode): #-> List[List[int]]:
        if not root:
            return []
        self.layer(root,0)
        return self.l

    def layer(self, node, k):
        if node:
            if len(self.l) <= k:
                self.l.append([])
            self.l[k].append(node.val)
            self.layer(node.left, k + 1)
            self.layer(node.right, k + 1) 

    #层次遍历按之字形打印二叉树,在上一题的基础上加上计数器
    def levelOrder(self, root): #-> List[List[int]]:
        if not root:
            return []
        else:
            l = []
            s = []
            l.append(root)
            index = 0
            while l:
                cunt = len(l)
                z = []
                while cunt:
                    temp = l.pop(0)
                    z.append(temp.val)
                    if temp.left:
                        l.append(temp.left)
                    if temp.right:
                        l.append(temp.right)
                    cunt -= 1
                if z:
                    if index % 2 == 0:
                        s.append(z)
                    else:
                        s.append(z[::-1])
                index += 1
            return s
        
    #二叉搜索树的后序遍历序列
    #二叉搜索树：左子树<根节点<右子树
    #给定一个序列，判断该序列是不是二叉搜索树的后序遍历序列
    #1.递归来做，根据根节点右边的值都应该大于根节点来做
    def verifyPostorder(self, postorder): # -> bool:
        if not postorder:
            return True
        else:
            return self.verify(postorder, 0, len(postorder) - 1)
        
    def verify(self, li, first, last):
        if last - first < 1:
            return True
        else:
            temp = li[last]
            index = 0
            while index < last and li[index] < temp:
                index += 1
            for j in range(index, last):
                if li[j] < temp:
                    return False
            return self.verify(li, first, index - 1) and self.verify(li, index, last - 1)

    #迭代的方法，不好想==后序遍历：左右根，那么倒序就是根右左，利用单调栈来做
    def verifyPostorder(self, postorder):  # -> bool:
        l = []
        root = float("+inf")
        for index in range(len(postorder)-1, -1, -1):
            if postorder[index] > root:
                return False
            else:
                while l and l[-1] > postorder[index]:
                    root = l.pop()
                l.append(postorder[index])
        return True
    
    #同理，判断一个数组是不是二叉搜索树的前序遍历：
    def verifyPreorder(self, postorder):  #-> bool:
        l = []
        root = float("-inf")
        for index in range(len(postorder)):
            if postorder[index] < root:
                return False
            else:
                while l and l[-1] < postorder[index]:
                    root = l.pop()
                l.append(postorder[index])
        return True
    
    #二叉树中和为某一值的路径：注意列表赋值！！
    def pathSum(self, root, sums): #-> List[List[int]]:
        if not root:
            return []
        else:
            l = []
            self.dfs1(root, sums, l)
            return self.res
        
    def dfs1(self, root, summ, temp):
        if not root:
            return 
        else:
            temp.append(root.val)
            summ -= root.val
            if summ == 0 and not root.left and not root.right:
                self.res.append(temp[:])   #将temp直接添加res中，res中的temp会随着pop操作变化！！！
            else:
                self.dfs1(root.left, summ, temp)
                self.dfs1(root.right, summ, temp)
            temp.pop()     #这个就用的很巧妙
        
    #复杂链表的复制，相当于将当前链表进行深拷贝
    #python一行代码： return copy.deepcopy(head)
    def copyRandomList(self, head: 'Node'):  #-> 'Node':
        # return copy.deepcopy(head)
        if not head:
            return 
        else:
            #插入复制后的节点
            cur = head
            while cur:
                newnode = Node(cur.val)
                newnode.next = cur.next
                cur.next = newnode
                cur = newnode.next
            #建立random链接
            cur = head
            while cur:
                clone = cur.next
                if cur.random:
                    clone.random = cur.random.next
                cur = clone.next
            #链表拆分，完成复制
            res = head.next
            cur = head
            while cur.next:
                nextnode = cur.next
                cur.next = nextnode.next
                cur = nextnode
            return res
    
    #36.二叉搜索树与双向链表
    #二叉搜索树按中序遍历即是排好序的，将该序列组装成链表结构就好
    def treeToDoublyList(self, root):   # -> 'Node':
        if not root:
            return 
        else:
            self.pre = None
            def dfs(node):
                if not node:
                    return
                dfs(node.left)
                if self.pre:
                    node.left = self.pre
                    self.pre.right = node
                else:
                    self.head = node
                self.pre = node
                dfs(node.right)
            dfs(root)
            self.pre.right = self.head
            self.head.left = self.pre
            return self.head
    
    #38.字符串的排列， 回溯法+剪枝，这个递归是真滴学不会=====慢慢品
    def permutation(self, s):  #-> List[str]:
        self.res = []
        length = len(s)
        def dfs(st, path):
            if not st:
                self.res.append(path)
            else:
                dic = set()
                for i in range(len(st)):
                    if st[i] in dic:
                        continue
                    else:
                        dic.add(st[i])
                        dfs(st[:i] + st[i+1: ], path + st[i])
        dfs(s, '')
        return self.res

    #数组中出现次数超过一半的数字
    def majorityElement(self, nums):  # -> int:
        #1.排序：
        # nums.sort()
        # return nums[len(nums) // 2]
        #2. 字典
        # dic = {}
        # for ele in nums:
        #     if ele not in dic:
        #         dic[ele] = 1
        #     else:
        #         dic[ele] += 1
        # for k, v in dic.items():
        #     if v > len(nums) // 2:
        #         return k
        #3.摩尔投票法:保存数组中的数字和次数
        cunt = 0
        for ele in nums:
            if cunt == 0:
                res = ele
            if ele == res:
                cunt += 1
            else:
                cunt -= 1
        return res
    
    #40.最小的k个数：1.直接排序取前k个； 2.用最小堆，始终保持最小的k个在堆里； 3.快排
    def getLeastNumbers(self, arr, k):  #-> List[int]:
        arr.sort()
        return arr[:k]


    #两个栈实现队列：
    #直接用列表实现
    def appendTail(self, value):
        self.l1.append(value)

    def deleteHead(self):
        if not self.l1:
            return -1
        else:
            return self.l1.pop(0)     

    #用两个栈实现
    def appendTail1(self, value):
        self.l1.append(value)

    def deleteHead1(self):
        if self.l2:
            return self.l2.pop()
        else:
            if self.l1:
                while self.l1:
                    self.l2.append(self.l1.pop())
                return self.l2.pop()
            else:
                return -1

    #二叉树的下一个节点
    #如果当前节点有右节点，寻找右节点的最左节点
    #否则，判断当前节点是不是父节点的左子节点
    def GetNext(self, pNode):
        if pNode.right:
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp
        else:
            while pNode.next:
                temp = pNode.next
                if temp.left == pNode:
                    return temp
                else:
                    pNode = pNode.next

    #树的子结构，  递归解决，比较B与当前A树、A的左子树、A的右子树        
    def isSubStructure(self, A, B):
        if not A or not B:
            return False
        else:
            return self.dfs(A,B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        
    def dfs(self, A, B):
        if not B:
            return True
        if not A:
            return False
        return A.val == B.val and self.dfs(A.left, B.left) and self.dfs(A.right, B.right)
    
    #二叉树的镜像，简单递归
    def mirrorTree(self, root): #-> TreeNode:
        if not root:
            return None
        else:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
            return root
    
    #对称的二叉树，判断一个二叉树和它的镜像是否相同，递归来写
    def isSymmetric(self, root): #-> bool:
        if not root:
            return True
        else:
            return self.issame(root.left, root.right)
        
    def issame(self,a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and self.issame(a.left, b.right) and self.issame(a.right, b.left)
    
    #顺时针打印矩阵，下标要搞清楚
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        h1 = 0
        h2 = len(matrix) - 1 
        l1 = 0
        l2 = len(matrix[0]) - 1
        l = []
        while h1 <= h2 and l1 <= l2:
            for i in range(l1,l2+1):
                l.append(matrix[h1][i])
            for j in range(h1+1,h2+1):
                l.append(matrix[j][l2])
            if h1 != h2:     #去除最后一次重复的来回
                for k in range(l2-1, l1, -1):
                    l.append(matrix[h2][k])
            if l1 != l2:
                for z in range(h2, h1, -1):
                    l.append(matrix[z][l1])
            h1 += 1
            h2 -= 1
            l1 += 1
            l2 -= 1
        return l
    
    #栈的压入、弹出序列， while循环模拟给出的出栈序列，若最后列表为空，说明该序列是该栈的弹出序列
    def validateStackSequences(self, pushed, popped):
        n = len(pushed)
        l = []
        popindex = 0
        for pushindex in range(0, n):
            l.append(pushed[pushindex])
            while popindex < n and l and popped[popindex] == l[-1]:   #判断条件别漏了
                l.pop()
                popindex += 1
        if not l:
            return True
        else:
            return False

    #包含min函数的栈
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []   #保存正常的栈结构（每次push操作结果）
        self.mins = []   #辅助栈，保存最小值


    def push(self, x):
        self.l.append(x)
        if not self.mins or self.mins[-1] >= x:
            self.mins.append(x)


    def pop(self):
        p = self.l.pop()
        if p == self.mins[-1]:
            self.mins.pop()


    def top(self):
        return self.l[-1]


    def min(self):
        return self.mins[-1]  
    
    




    #斐波那契数列，递归重复计算容易超时，最好迭代
    #lru_cache是个好东西
    def fib(self, n):
        if n <= 1:
            return n
        else:
            a = 0
            b = 1
            index = 2
            while index <= n:
                c = a + b
                a = b
                b = c
                index += 1
            return c % 1000000007
    
    @lru_cache(None)
    def fib(self, n):
        if n <= 1:
            return n
        else:
            return (self.fib(n-1) + self.fib(n-2)) % 1000000007

    #旋转数组中的最小数字
    # 遍历数组，找前面一个数>后面一个数字的，时间复杂度为O(N)
    # 二分查找，时间复杂度为O(logn) 
    def minArray(self, numbers):
        low = 0
        high = len(numbers) - 1
        while low < high:
            mid = (low + high) // 2
            if numbers[mid] > numbers[high]:
                low = mid + 1
            elif numbers[mid] < numbers[high]:
                high = mid
            else:     #处理类似[3,3,1,3]这种情况
                high -= 1
        return numbers[low]
    
    #矩阵中的路径，深度优先搜索，不允许往回走所以要标记
    def exist(self, board, word):
        if not board:
            return False
        else:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.dfs(board, i, j, word):
                        return True
            return False
    
    def dfs(self, mat, col, row, st):
        if not st:
            return True
            
        if col < 0 or row < 0 or col >= len(mat) or row >= len(mat[0]) or mat[col][row] != st[0]:
            return False
        else:
            temp = mat[col][row] 
            mat[col][row] = '#'
            if self.dfs(mat, col + 1, row, st[1:]) or self.dfs(mat, col - 1, row, st[1:]) or self.dfs(mat, col, row + 1, st[1:]) or self.dfs(mat, col, row - 1, st[1:]):
                mat[col][row] = temp
                return True
            else:
                mat[col][row] = temp
                return False
    
    #机器人的运动范围，dfs
    def mul(self, m, n):
        summ = 0
        while m:
            summ += m % 10
            m = m // 10
        while n:
            summ += n % 10
            n = n // 10
        return summ

    def movingCount(self, m, n, k):
        visited = [[0 for i in range(n)] for j in range(m)]
        cunt = self.dfs(0, 0, m, n, k, visited)
        return cunt
    
    def dfs(self, a, b, m, n, k, visited):
        if a < 0 or b < 0 or a >= m or b >= n or self.mul(a,b) > k or visited[a][b]:
            return 0
        else:
            visited[a][b] = 1
            return self.dfs(a + 1, b, m, n, k, visited) + self.dfs(a, b + 1,m,n,k, visited) + 1
    
    # 剪绳子问题， 尽可能多的包含3，3越多乘积越大
    def cuttingRope(self, n):
        if n == 2:
             return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        else:
            summ = 1
            while n > 4:
                summ *= 3
                n -= 3
            return summ * n

    #二进制中1的个数  暴力使用库函数找   
    def hammingWeight(self, n):
        s = bin(n)[2:]
        return s.count('1')
    
    #使用位运算
    def hammingWeight1(self, n):
        cunt = 0
        while n:
            if n & 1:
                cunt += 1
            n = n >> 1
        return cunt

    #巧用n与(n-1)的关系，时间复杂度更低
    def hammingWeight(self, n):
        cunt = 0
        while n:
            cunt += 1
            n = n & (n-1)
        return cunt
    
    #不用pow函数计算数值的整数次方
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            flag = True
            if n < 0 :
                flag = False
                n = - n
            pow = self.myPow(x * x, n // 2)
            if n % 2 == 1:
                pow = pow * x
            return pow if flag else 1/pow

    #打印从1到最大的n位数，首先暴力列表循环输出
    def printNumbers(self, n):
        s = pow(10, n) 
        l = []
        for i in range(1, s):
            l.append(i)
        return l
    
    #对于n非常大的情况，可以考虑用字符串处理
    def printNumbers1(self, n):
        if n <= 0:
            return 
        numbers = ['0' for i in range(n)]
        return self.prt(numbers, 0)
    
    def prt(self, li, index):
        if index == len(li):
            self.prtNumbers(li)
        else:
            for i in range(10):
                li[index] = chr(ord('0') + i)
                self.prt(li, index + 1)
            return self.l
    
    def prtNumbers(self, li):
        tag = 0
        while tag < len(li) and li[tag] == '0':
            tag += 1
        st = ''
        while tag < len(li):
            st += li[tag]
            tag += 1
        if st:
            self.l.append(int(st))

    #删除链表的节点：
    def deleteNode(self, head, val):
        if not head:
            return None
        else:
            if head.val == val:
                head = head.next
            else:
                temp = head
                while temp.val != val:
                    pre = temp
                    temp = temp.next
                pre.next = temp.next
            return head

    #删除链表中重复的节点，递归来做
    def deleteDuplication(self, pHead):
            # write code here
            if not pHead:
                return None
            else:
                temp = pHead.next
                if temp and pHead.val == temp.val:
                    while temp and temp.val == pHead.val:
                        temp = temp.next
                    return self.deleteDuplication(temp)
                else:
                    pHead.next = self.deleteDuplication(temp)
                    return pHead

    #正则表达式匹配，用正则==
    def isMatch(self, s, p):
        import re
        if not re.match(p,s):
            return False
        else:
            if re.match(p,s).group() == s:
                return True
            else:
                return False

    #主要是对于*的处理，动态规划来做
    def isMatch(self, s, p):
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        for i in range(len(s)+1):
            for j in range(len(p) + 1):
                if j == 0:
                    dp[i][j] =  i == 0
                else:
                    if p[j-1] != '*':
                        if i >= 1 and (p[j-1] == '.' or s[i-1] == p[j-1]):
                            dp[i][j] = dp[i-1][j-1]
                    else:
                        if j >= 2:     #不管*及其之前的字符
                            dp[i][j] |= dp[i][j-2]
                        if j >= 2 and i >= 1 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                            dp[i][j] |= dp[i-1][j]
        return dp[len(s)][len(p)]
    
    # 表示数值的字符串, 暴力try==
    def isNumber(self, s):
        try:
            s = float(s)
            return True
        except:
            return False
    
    #使用正则表达式匹配==方便，就是规则难写==
    def isNumber1(self, s):
        import re
        if re.match('[+-]?\d*(\.\d+)?([Ee][+-]?\d+)?', s):
            return True
        else:
            return False

    #调整数组顺序使奇数位于偶数前面
    #冒泡排序，保持偶数之间的相对顺序，时间复杂度大
    def exchange(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            for j in range(i):
                if nums[j] % 2 == 0 and nums[j+1] % 2 != 0 :
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        return nums
    
    #链表中的倒数第k个节点
    #双节点，快慢节点,快节点先走k步，当快节点到达链表尾部时，慢节点刚好到达倒数第k个节点
    def getKthFromEnd(self, head, k):
        if not head:
            return False
        else:
            temp = head
            while k:
                temp = temp.next
                k -= 1
            while temp:
                head = head.next
                temp = temp.next
            return head

    #链表中环的入口节点， 快慢指针，快指针每次走两步，慢指针每次走一步
    #2(x+y) = x + 2y + z  得出x = z
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return None
        else:
            fast = pHead.next.next
            slow = pHead.next
            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            fast = pHead
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow  

    #反转链表，利用列表反转尾插法重新构建
    def reverseList(self, head):
        if not head:
            return None 
        else:
            l = []
            while head:
                l.append(head.val)
                head = head.next
            head = ListNode(l[-1])
            tou = head
            for ele in l[::-1][1:]:
                temp = ListNode(ele)
                head.next = temp
                head = temp
            return tou
    
    #利用头插法
    def reverseList1(self, head):
        if not head:
            return False
        else:
            rehead =  ListNode(-1)
            rehead.next = None
            while head:
                temp = ListNode(head.val)
                temp.next = rehead.next
                rehead.next = temp
                head = head.next
            return rehead.next

    #合并两个排序的链表 迭代 利用尾插法构造链表   
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        head = ListNode(-1)
        tou = head
        while l1 and l2:
            if l1.val < l2.val:
                temp = ListNode(l1.val)
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                l2 = l2.next
            head.next = temp
            head = temp
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return tou.next
    
    #递归进行排序==永远学不会递归==
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

    



#序列化二叉树，先将二叉树按照层次遍历转化成字符串，再将字符串转化为二叉树
class Codec:
    def __init__(self):
        self.root = None

    def serialize(self, root):
        if not root:
            return ''
        else:
            res = []
            deque = []
            deque.append(root)
            while deque:
                node = deque.pop(0)
                if node:
                    res.append(str(node.val))
                    deque.append(node.left)
                    deque.append(node.right)
                else:
                    res.append('#')
            return(','.join(res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return 
        else:
            res = data.split(',')
            root = TreeNode(int(res[0]))
            deque = []
            deque.append(root)
            index = 1
            while deque:
                node = deque.pop(0)
                if res[index] != '#':
                    node.left = TreeNode(int(res[index]))
                    deque.append(node.left)
                index += 1
                if res[index] != '#':
                    node.right = TreeNode(int(res[index]))
                    deque.append(node.right)
                index += 1
            return root


if __name__ == '__main__':
    so = Solution()
    #so.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
    # s = ListNode(1)
    # s.next = ListNode(2)
    # s.next.next = ListNode(3)
    # so.reversePrint(s)
    #print(so.compileSeq('1,2,-1,1'))
    # pre = [1,2,4,7,3,5,6,8]
    # inor = [4,7,2,1,5,3,8,6]
    # post = [7,4,2,5,8,6,3,1]
    # so.buildTree(pre,inor)
    # print('')
    # rot = so.buildTree1(post, inor)
    # print('')
    # so.buildTree2(rot)
    #so.validateStackSequences([1,0], [1, 0])
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    #so.pathSum(root, 22)
    #so.permutation("abc")
    #print(so.insert_sort([5,2,4,6,1,3]))
    #print(so.bubble_sort([5,2,4,6,1,3]))
    # l = [5,2,4,6,1,3]
    # so.quick_sort(l ,0, len(l))
    # print(l)
    seq = [5,3,0,6,1,4]
    print('排序前：',seq)
    result = so.mergesort(seq)
    print('排序后：',result)
        