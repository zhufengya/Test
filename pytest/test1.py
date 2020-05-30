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

def rond():
    while True:
        try:
            s = input().split('.')
            if int(s[1][0]) >=5 :
                print(int(s[0])+ 1)
            else:
                print(int(s[0]))
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
    rond()
