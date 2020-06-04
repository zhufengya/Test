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
    pwd_valid()
    
