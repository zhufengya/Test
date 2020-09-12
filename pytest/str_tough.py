#合唱队：最大非连续递增子序列
def maxx(li):
    f = [0 for i in range(len(li))]
    for i in range(len(li)):
        for j in range(i-1,-1,-1):
            if li[i] > li[j] and f[i] < f[j] + 1:
                f[i] = f[j] + 1
    return f

def hechang():
    while True:
        try:
            n = int(input())
            l = list(map(int, input().split(' ')))
            f1 = maxx(l)
            f2 = maxx(l[::-1])
            ma = max([f1[i] + f2[::-1][i] for i in range(n)])
            print(n-ma - 1)
        except:
            break

#最大连续回文子串长度
def process(st):   #先对字符串进行处理
    l = '#'
    for letter in st:
        l += letter
        l += '#'
    return l

def manna(st):
    center = 0
    rmax = -1
    p = [0 for i in range(len(st))]   #回文半径数组
    for i in range(len(st)):
        if i>= rmax:   #对应下一个移动位置位于右边界右边的情况
            p[i] = 1
        else:       #下一个移动位置在右边界左边的情况
            p[i] = min(rmax-i+1, p[2*center - i])
        while i-p[i] >=0 and i+p[i] < len(st) and st[i-p[i]] == st[i+p[i]]:   #向外扩充半径
            p[i] += 1
        if i+p[i] > rmax:    #更新右边界和回文中心
            rmax = i + p[i] -1
            center = i
    return max(p) - 1

def pwdget():   #马拉车算法！
     while True:
        try:
            s = input()
            s = process(s)
            print(manna(s))
        except:
            break



if __name__ == '__main__':
   pwdget()