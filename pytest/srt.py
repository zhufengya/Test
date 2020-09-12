#插入排序，时间复杂度为O(n^2)    稳定
def insert_sort(l):
    for i in range(len(l)):
        temp = l[i]
        j = i-1
        while (j >= 0 and l[j] > temp):
            l[j+1] = l[j]
            j -= 1
        l[j + 1] = temp
    print(l)

#冒泡排序：时间复杂度为O(n^2), 每次将最小的数冒泡到最前面的位置   稳定
def pao(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1,i-1,-1):
            if l[j+1] < l[j]:
                l[j+1],l[j] = l[j],j[j+1]
    print(l)
#时间复杂度为O(nlogn),具体的稳定性取决于划分算法。
def quick_sort(l,st,end):
    if st >= end:
        return
    else:
        key = l[st]
        little_end = st
        for i in range(st + 1, end+1):
            if l[i] < key:
                little_end += 1
                l[i],l[little_end] = l[little_end], l[i]
        for i in range(st,little_end):
            l[i] = l[i+1]
        l[little_end] = key
    quick_sort(l,st,little_end-1)
    quick_sort(l,little_end+1, end)



# if __name__ == '__main__':
#     while True:
#         try:
           
#         except:
#             break
l = list(map(int,input().split(' ')))
# insert_sort(l)
# pao(l)
quick_sort(l,0,len(l)-1)
print(l)