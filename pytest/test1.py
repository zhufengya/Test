import re

def wordlength():
    while True:
        try:
            s = input().strip().split(' ')
            print(len(s[-1]))
        except:
            break

def wordcunt():
    while True:
        try:
            s = input().strip()
            s = s.upper()
            char  = input().strip()
            print(s.count(char.upper()))
        except:
            break
"""
    set集合的定义方式l = set(),set是无重复元素的无序集合！！
    l.add():添加元素
    l.remove():删除元素，当元素不存在时报错
    l.discard():删除元素，元素不存在时不会报错
"""
def mingming():
    while True:
        try:
            a = int(input())
            l = set()  
            for i in range(a):
                l.add(int(input()))
            s = list(l)
            s.sort()
            for ele in s:
                print(ele)
        except:
            break
"""
注意python for循环与其他语言for循环的区别
for i in range(5):
    pass
print(i)   i的值为4.
"""
def strsplit():
    while True:
        try:
            s = input().strip()
            if len(s)<=8:
                print(s + '0'*(8-len(s)))
            else:
                for i in range(len(s)//8):   #for循环结束后i的值是len(s)//8-1!!!!!
                    print(s[i*8:(i+1)*8])
                if len(s)%8:
                    print(s[(i+1)*8:]+'0'*((i+2)*8 - len(s)))
        except:
            break

def hextoint():
    while True:
        try:
            s = input().strip()
            print(int(s,16))
        except:
            break

def hextoint1():
    dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    while True:
        try:
            s = input().strip()
            #print(int(s,16))
            summ = 0
            for letter in s[2:]:
                if letter in "ABCDEF":
                    summ = summ * 16 + dic[letter]
                else:
                    summ = summ * 16 + int(letter)
            print(summ)
        except:
            break

#求一个数的质数因子。
def isprime(n):
    i = 2
    while(i*i <= n):
        if n % i == 0:
            return False
        else:
            i = i + 1
    return True

def primenumber():   
    while True:
        try:
            s = int(input().strip())
            if isprime(s):
                print(s)
                continue
            i = 2
            t = s
            while(i <= t // 2):
                if not s % i :
                    print(i,end = ' ')
                    s = s // i
                else:
                    i = i+1
        except:
            break

def rond():    #python round函数分奇偶！！round(1.5) = 2 round(2.5) = 2
    while True:
        try:
            s = input().split('.')
            if int(s[1][0]) >=5 :
                print(int(s[0])+ 1)
            else:
                print(int(s[0]))
        except:
            break
#按照键值将表记录进行合并。      
def mergeRecord():
    while True:
        try:
            s = int(input())
            dic = {}
            for i in range(s):
                a,b = list(map(int,input().split(' ')))
                if a not in dic:
                    dic[a] = b
                else:
                    dic[a] += b
            for k,v in sorted(dic.items(), key = lambda x: x[0]):
                print(k,v)
        except:
            break

#对输入整数进行反序去重。
def setint():
    while True:
        try:
            s = input().strip()
            l = ''
            for al in s[::-1]:
                if al not in l:
                    l += al
            print(l)
        except:
            break  
#统计输入字符串中ascii码在0～127之间的不重复字符的个数
def  charcunt():
    while True:
        try:
            s = input().strip('\n')
            l = ''
            for le in s:
                if ord(le) in range(0,128):
                    if le not in l:
                        l += le
            print(len(l))
        except:
            break  

#字符串逆序输出
def strreverse():
    while True:
        try:
            s = input()
            print(s[::-1])
        except:
            break
    
def senreverse():
    while True:
        try:
            s = input().strip().split(' ')
            print(" ".join(s[::-1]))
        except:
            break

def strdic():
    while True:
        try:
            s = int(input())
            l = []
            for i in range(s):
                l.append(input().strip())
            l.sort()
            for le in l:
                print(le)
        except:
            break

def int1():
    while True:
        try:
            n = int(input())
            st = bin(n)[2:]
            print(st.count('1'))
        except:
            break
 
def coordinate_move():
    while True:
        try:
            s = input().strip().split(';')
            x,y = 0,0
            for word in s:
                if len(word) in range(2,4) and word[1:].isdigit():
                    if word[0] == 'A':
                        x -= int(word[1:])
                    elif word[0] == 'D':
                        x += int(word[1:])
                    elif word[0] == 'W':
                        y += int(word[1:])
                    elif word[0] == 'S':
                        y -= int(word[1:])
                    else:
                        continue
            print(str(x) + ',' + str(y))
        except:
            break

def valid_mask(st):
    try:
        l = list(map(int,st.split('.')))
        if(len(l)!=4):
            return False
        if l == [0,0,0,0] or l == [255,255,255,255]:
            return False
        summ = (l[0]<<24) + (l[1]<<16) + (l[2]<<8) + l[3]
        if summ | (summ -1) == 0xFFFFFFFF:
            return True
        else:
            return False
    except:
        return False

def ipclass(st):
    try:
        l = list(map(int,st.split('.')))
        if(len(l) != 4):
            return 'err'
        if l[0] == 10:
            return 'ap'
        elif l[0] == 172 and l[1] in range(16,32):
            return 'bp'
        elif l[0] == 192 and l[1] == 168:
            return 'cp'
        elif l[0] in range(1,127):
            return 'a'
        elif l[0] in range(128,192):
            return 'b'
        elif l[0] in range(192,224):
            return 'c'
        elif l[0] in range(224,240):
            return 'd'
        elif l[0] in range(240,256):
            return 'e'
        else:
            return 'err'
    except:
        return 'err'

def addressclass():
    a,b,c,d,e,err,p = 0,0,0,0,0,0,0
    while True:
        try:
            ipt = input().strip().split('~')
            ip = ipt[0]
            mask = ipt[1]
            if valid_mask(mask):
                if ipclass(ip) == 'ap':
                    a += 1
                    p += 1
                elif ipclass(ip) == 'bp':
                    b += 1
                    p += 1
                elif ipclass(ip) == 'cp':
                    c += 1
                    p += 1
                elif ipclass(ip) == 'a':
                    a += 1
                elif ipclass(ip) == 'b':
                    b += 1
                elif ipclass(ip) == 'c':
                    c += 1
                elif ipclass(ip) == 'd':
                    d += 1
                elif ipclass(ip) == 'e':
                    e += 1
                else:
                    err += 1
            else:
                err += 1
        except:
            break
    print(a,b,c,d,e,err,p)

def errecord():
    l = []
    recordlist = []
    while True:
        try:
            s = input().strip().split('\\')
            record = s[-1].split(" ")
            if len(record[0]) >= 16:
                temp = record[0][-16:]
            else:
                temp = record[0]
            re = temp + ' ' + record[-1]
            if s[-1] not in l:
                l.append(s[-1])
                recordlist.append([re,1])
            else:
                for ele in recordlist:
                    if ele[0] == re:
                        ele[1] += 1
                        break
            if len(recordlist) > 8:
                for ele in recordlist[-8:]:
                    print(ele[0],ele[1])
            else:
                for ele in recordlist:
                    print(ele[0],ele[1])
        except:
            break
            
def pwd_valid():      
    while True:
        try:
            s = input()
            p1 = r'\d'
            p2 = r'[A-Z]'
            p3 = r'[a-z]'
            p4 = r'[^\dA-Za-z]'
            p5 = r'(.{3,}).*\1'     #寻找长度超过2的重复子串。 \1表示重复前一个()的内容。
            l1 = re.findall(p1,s)
            l2 = re.findall(p2,s)
            l3 = re.findall(p3,s)
            l4 = re.findall(p4,s)
            l5 = re.findall(p5,s)
            if len(s) > 8:
                if (l1,l2,l3,l4).count([]) <= 1:
                    if not l5:
                        print('OK')
                        continue
            print('NG')
        except:
            break       

def symbol(st):
    cunt = [0,0,0,0]
    for letter in st:
        if letter.isdigit():
            cunt[0] = 1
        elif letter.isupper():
            cunt[1] = 1
        elif letter.islower():
            cunt[2] = 1
        else:
            cunt[3] = 1
    return sum(cunt)
 
def substr(st):
    for i in range(len(st)-2):
        if st.find(st[i:i+3], i+1) != -1:
            return False
    return True

def pwd_valid():
    while True:
        try:
            s = input().strip()
            if len(s) > 8:
                if symbol(s) >= 3:
                    if substr(s):
                        print('OK')
                        continue
            print('NG')
        except:
            break                           

def simple_pwd():
    while True:
        try:
            s = input().strip()
            l = ''
            for letter in s:
                if letter.isupper():
                    if letter == 'Z':
                        letter = 'a'
                    else:
                        letter = chr(ord(letter.lower())+1)
                elif letter in 'abc':
                    letter = '2'
                elif letter in 'def':
                    letter = '3'
                elif letter in 'ghi':
                    letter = '4'
                elif letter in 'jkl':
                    letter = '5'
                elif letter in 'mno':
                    letter = '6'
                elif letter in 'pqrs':
                    letter = '7'
                elif letter in 'tuv':
                    letter = '8'
                elif letter in 'wxyz':
                    letter = '9'
                l += letter
            print(l)
        except:
            break

def bottle():
    while True:
        try:
            s = int(input())
            print(s//2)
        except:
            break
#删除字符串中出现次数最少的字符。
def del_least_letter():
    while True:
        try:
            s = input()
            l = [0 for i in range(26)]
            t = ''
            for le in s:
                l[ord(le)-97] += 1
            index = min([i for i in l  if i != 0])
            for st in s:
                if l[ord(st)-97] != index:
                    t += st
            print(t)
        except:
            break
#购物单
def shopping_list():
    N, m =list(map(int, input().split(' '))) 
    N = N // 10
    f = [0 for i in range(N+1)]
    price = [[0 for i in range(3)] for j in range(m+1)]
    value = [[0 for i in range(3)] for j in range(m+1)]
    for i in range(1,m+1):
        v, p, q = list(map(int, input().split(' ')))
        v  = v // 10
        vp = v * p
        if q == 0:
            price[i][0] = v
            value[i][0] = vp
        elif price[q][1] == 0:
            price[q][1] = v
            value[q][1] = vp
        else:
            price[q][2] = v
            value[q][2] = vp
    for i in range(1,m+1):
        if price[i][0] == 0:
            continue
        for j in range(N,0,-1):
            if j >= price[i][0]:
                f[j] = max(f[j], f[j-price[i][0]] + value[i][0])
                if price[i][1] == 0:
                    continue
            if j >= price[i][0] + price[i][1]:
                f[j] = max(f[j], f[j-price[i][0] - price[i][1]] + value[i][0] + value[i][1])
                if price[i][2] == 0:
                    continue
            if j >= price[i][0] + price[i][2]:
                f[j] = max(f[j], f[j-price[i][0] - price[i][2]] + value[i][0] + value[i][2])
            if j >= price[i][0] + price[i][1] + price[i][2]:
                f[j] = max(f[j], f[j-price[i][0] - price[i][1] - price[i][2]] + value[i][0] + value[i][1] + value[i][2])
    print(f[N] * 10)
#合唱队
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
#数据分类处理！ 时刻谨记要写strip()去掉额外的换行等字符！！！
def data_process():
    while True:
        try:
            li = input().strip().split(' ')[1:]
            lr = list(map(int,input().strip().split(' ')[1:]))
            lr = sorted(list(set(lr)))
            l = []
            for ele in lr:
                s = []
                cunt = 0
                ele = str(ele)
                l.append(ele)
                for t in li:
                    if ele in t:
                        s.append(str(li.index(t)))
                        s.append(t)
                        cunt += 1
                if cunt == 0:
                    continue
                l.append(str(cunt))
                l.extend(s)
            print(len(l),' '.join(l))
        except:
            break
#字符串排序
def str_sort():
    while True:
        try:
            s = input().strip()
            l = []
            for letter in s:
                if letter.isalpha():
                    l.append(letter)
            l.sort(key = lambda x: x.lower())
            result = ''
            i = 0
            for letter in s:
                if letter.isalpha():
                    result += l[i]
                    i += 1
                else:
                    result += letter
            print(result)
        except:
            break

def brother_word():
    while True:
        try:
            s = input().split(' ')
            index = int(s[-1])
            word = s[-2]
            wl = list(word)
            wl.sort()
            l = []
            for ele in s[1:-2]:
                elel = list(ele)
                elel.sort()
                if (elel == wl) and (ele != word):
                    l.append(ele)
            l.sort()
            print(len(l))
            if index <= len(l):
                print(l[index-1])
        except:
            break

def prime(a, b):
    summ = a + b
    i = 2
    while i * i <= summ:
        if summ % i == 0:
            return False
        i += 1
    return True
    

def pair(x1,us,res):
    for i in range(1, len(ou)+1):
        if prime(ji[x1-1], ou[i-1]) and us[i] == 0:
            us[i] = 1
            if res[i] == 0 or pair(res[i]):
                res[i] = x1
                return True
    return False
#素数伴侣   递归想清楚==比较难得画图
def primepartner():
    n = int(input())
    s = list(map(int,input().split(' ')))
    for num in s:
        if num % 2:
            ji.append(num)
        else:
            ou.append(num)
    result = [0 for i in range(len(ou)+1)]
    cunt = 0
    for x in range(1,len(ji)+1):
        used = [0 for i in range(len(ou)+1)]
        if pair(x, used,result):
            cunt += 1
    print(cunt)
    '''
    while True:
        try:
           
        except:
            print('ja')
            break
        '''  

s1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s2 = 'BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890'

def en(st):
    l = ''
    for letter in st:
        l += s2[s1.index(letter)]
    print(l)

def de(st):
    ls = ''
    for letter in st:
        ls += s1[s2.index(letter)]
    print(ls)

def strec():  
    while True:
        try:
            s = input()
            t = input()
            en(s)
            de(t)
        except:
            break 
#字符串合并处理    
def str_merge():
    s1 = '0123456789abcdefABCDEF'
    s2 = '084C2A6E195D3B7F5D3B7F'   #还是就暴力破解用字典最简单呀==
    dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while True:
        try:
            s = input().split(' ')
            s = s[0] + s[1]
            l1 = []
            l2 = []
            for i in range(len(s)):
                if i % 2:
                    l2.append(s[i])
                else:
                    l1.append(s[i])   #0,2,4...
            l1.sort()
            l2.sort()
            re = ''
            for i in range(len(s)):
                if i % 2:
                    re += l2[i//2]
                else:
                    re += l1[i//2]
            final = ''
            for letter in re:
                if letter.isdigit():
                    binstr = bin(int(letter))[2:]
                elif letter.upper() in 'ABCDEF':
                    binstr = bin(int(letter,16))[2:]
                else:
                    final += letter
                    continue
                if len(binstr) < 4:    #bin(1) = 1, 逆序后还是1会出错！！所以要补齐四位！！记住了！！！
                    binstr = '0' *(4-len(binstr)) + binstr
                binstr = list(binstr)
                binstr.reverse()
                result = int(''.join(binstr),2)
                if result <= 9:
                    final += str(result)
                else:
                    final += dic[result]
            print(final)
        except:
            break
 
def test(name,age,**kw):    #关键字参数
    print("name:", name, "  age:", age, kw)

def keyname(name, age, *, city, major):   #命名关键字参数，如果前有可变参数，*可省略，否则不可省略
    print("name:",name,"  age:",age, city, major)

def fact(n):
    if n== 1:
        return 1
    else:
        return n * fact(n-1)

def f(n):
    return fa(n,1)

def fa(num, re):    #尾递归：return中不含表达式，且调用自身本身。
    if num == 1:
        return re
    else:
        return fa(num-1, num * re)

def trim(s):
    if not s:
        return ''
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        else:
            break
    for j in range(len(s)-1,-1,-1):
        if s[j] == ' ':
            continue
        else:
            break
    return s[i:j+1]

def fib(max):    #生成器，遇到yield就停止执行，要用next()函数或者for循环来获取生成器的结果
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b = b , a + b
        n += 1
    return 'done'

def triangle():     #使用生成器生成杨辉三角。
    l = [1]
    while True:
        yield l
        l = [1] + [l[x] + l[x+1] for x in range(len(l)-1)] + [1]

from functools import reduce

def str2float(s):    #map /reduce函数！！
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    print(s.split('.')[0])
    return reduce(fn, map(char2num, s.split('.')[0])) + reduce(fn, map(char2num, s.split('.')[1])) * (10 **(-len(s.split('.')[1])))

def _not_divisible(n):
    return lambda x: x % n > 0

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

import functools

# def log(func):         #装饰器
#     @functools.wraps(func)   #不改变原来func的名字
#     def wrapper(*args, **kw):
#         print("begin call")
#         print('call %s():' % func.__name__)
#         f = func(*args, **kw)
#         print("end call")
#         return f
#     return wrapper 

def log(text):   #可同时支持@log和@log("haha")
    if isinstance(text,str):   #先判断text是不是传入的参数
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        print("end call")
        return decorator
    else:
        @functools.wraps(text)   
        def wrapper(*args, **kw):
            print("begin call")
            print('call %s():' % text.__name__)
            f = text(*args, **kw)
            print("end call")
            return f
        return wrapper

@log("haha")
def now():
    print('2020-6-14')

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
#[中级]单词倒排
def word_reverse():  #越写越倒退了==
    while True:
        try:
            s = input().strip().strip('\n')
            l = []
            cunt = 0
            for i in range(len(s)):
                if s[i].isalpha():
                    cunt += 1
                    continue
                else:
                    if cunt == 0:
                        continue
                    l.append(s[i-cunt:i])
                    cunt = 0
                    flag = False
            if cunt:
                l.append(s[i-cunt+1:len(s)])
            l.reverse()
            print(" ".join(l).strip())
        except:
            break

def word_reverse1():
    while True:
        try:
            s = input().strip().strip('\n')
            l = ''
            re = []
            for letter in s:
                if letter.isalpha():
                    l += letter
                else:
                    if l:
                        re.append(l)
                    l = ''
            if l:
                re.append(l)
            print(' '.join(re[::-1]))
        except:
            break
#字符串运用，密码截取          求一个字符串的最大连续回文子串！！
#1.从头回溯遍历整个字符串，找到满足ABA或aabb形式的最大子串
#2.马拉车算法！不需要回溯！时间复杂度为O(n)
def manna(st):    #字符串回溯
    cunt = 0
    for i in range(len(st)):
        low,high = i, i+1
        while low >=0 and high <len(st) and st[low] == st[high]:
            low -= 1
            high += 1
        if high - low - 1 > cunt:
            cunt = high - low -1
        low,high = i-1, i+1
        while low >=0 and high <len(st) and st[low] == st[high]:
            low -= 1
            high += 1
        if high - low - 1 > cunt:
            cunt = high - low -1
    return cunt

#整数与ip地址间的转换
def ip_int(st):
    l = list(map(int,st.split('.')))
    summ = (l[0] << 24) + (l[1]<<16) + (l[2]<<8) + l[3]
    return summ

def int_ip(st):
    l = []
    l.append(str(st >> 24))
    num1 = st % (pow(2,24))
    l.append(str(num1 >> 16))
    num2 = num1 %(pow(2,16))
    l.append(str(num2 >> 8))
    l.append(str(num2 % pow(2,8)))
    return '.'.join(l)

def transform():
    while True:
        try:
            sip = input()
            sint = input()
            print(ip_int(sip))
            print(int_ip(int(sint)))
        except:
            break
 #图片整理，对字符串进行排序！ 直接把str转化成list，然后list.sort()也可以   
def image_analyze():
    dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    while True:
        try:
            s = input()
            for letter in dic:
                for ch in s:
                    if ch == letter:
                        print(ch,end = '')
            print()
        except:
            break
#蛇形矩阵！找到规律就好！
def matrix():
    while True:
        try:
            s = int(input())
            init = 1
            for i in range(s):
                l = []
                l.append(init)
                for j in range(s-i-1):
                    l.append(l[j] + i + j + 2)
                print(' '.join(list(map(str,l))))
                init += i + 1
        except:
            break
#字符串加密，字符替换，简单替换加密。
def encrystr():
    dic = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        try:
            key = input()
            st = input()
            l = ''
            for letter in key:
                letter = letter.lower()
                if letter not in l:
                    l += letter
            for letter in dic:
                if letter not in l:
                    l += letter
            for ch in st:
                if ch.isupper():
                    print(l[dic.index(ch.lower())].upper(), end = '')
                else:
                    print(l[dic.index(ch)],end = '')
            print()
        except:
            break
#统计每个月兔子的总数，总数满足斐波那契数列！！
def fib(n):   
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#辣鸡题==小球反弹高度。
def height():
    while True:
        try:
            s = int(input())
            summ = s
            for i in range(4):
                s = s / 2
                summ += 2 * s
            print(summ)
            print(s/2)
        except:
            break

#判断两个ip是不是属于同一个子网
def mask_valid(ip):
    try:
        l = list(map(int,ip.split('.')))
        summ = (l[0]<<24) +(l[1]<<16) + (l[2] <<8) + l[3]
        if summ | (summ -1) == 0xFFFFFFFF:
            return True
        else:
            return False
    except:
        return False

def ip_valid(ip):
    try:
        l = list(map(int,ip.split('.')))
        for num in l:
            if num >= 0 and num <= 255:
                continue
            else:
                return False
        return True
    except:
        return False

def ip_mask(ip,mask):
    l1 = list(map(int,ip.split('.')))
    l2 = list(map(int,mask.split('.')))
    l = []
    for i in range(4):
        l.append(l1[i] & l2[i])
    return l

def subip():
    while True:
        try:
            mask = input()
            ip1 = input()
            ip2 = input()
            if not mask_valid(mask):
                print('1')
                continue
            elif not ip_valid(ip1) or not ip_valid(ip2):
                print('1')
            else:
                if ip_mask(ip1,mask) == ip_mask(ip2, mask):
                    print('0')
                else:
                    print('2')
        except:
            break       
            
            
            
            
        
if __name__=="__main__":
    #wordlength()
    #wordcunt()
    #mingming()
    #strsplit()
    #hextoint()
    #hextoint1()
    #primenumber()
    #rond()
    # mergeRecord()
    # setint()
    # charcunt()
    # strreverse()
    # senreverse()
    # strdic()
    # int1()
    # coordinate_move()
    # errecord()
    # pwd_valid()
    # shopping_list()
    # hechang()
    # data_process()
    ji = []
    ou = []
    # primepartner()
    # str_merge()

    
        
