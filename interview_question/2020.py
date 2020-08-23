# coding=utf-8

# ======= 排序算法(自己写的)：
def strlist_to_numlist(strlist):   # 判断输入的是否为数字
    li=[]
    for i in range(len(strlist)):
        try:
            tonum=float(strlist[i])
            li.append(tonum)
        except ValueError:
            print('您输入的不是数字！')
            break
    return li

def num_sort(num,method):   # 排序
    # num=input('请输入一串数字,并用“，”隔开：')
    # method = input('请输入排序方式（asc代表升序，desc代表降序）：')
    num = num.split(',')

    li=strlist_to_numlist(num)


    for j in range(len(li)-1):
        for k in range(1,len(li)-j):
            if li[k-1]>li[k]:
                li[k],li[k-1]=li[k-1],li[k]
    if method == 'asc':
        li=li
    elif method == 'desc':
        li=li[::-1]  #  a[:]/a[::]从左往右 ; a[::-1]从右往左,此方式对列表和字符串均有效
    else:
        print('请输入正确的排序方式！')
    print(li)
#
# list1='1,5,6,4,7,665,215,7,1,0'
# method='desc'
# num_sort(list1,method)

# =====以下为网上找的答案
# 1.快熟排序
import random
def quicksort(seq):
    if len(seq)<2:
        return seq
    else:
        base=seq[0]
        left = [elem for elem in seq[1:] if elem<base]
        right= [elem for elem in seq[1:] if elem>base]
        return quicksort(left)+[base]+quicksort(right)
# li=[9,4,15,2,546,]
# print(quicksort(li))

# 2.冒泡排序
def bouble_sort(sequence):
    for i in range(len(sequence)-1):
        for j in range(1,len(sequence)-i):
            if sequence[j-1]>sequence[j]:
                sequence[j - 1],sequence[j]=sequence[j],sequence[j - 1]
    print(sequence)

# sequence=[8,4,6,7,9,2,1,3]
# bouble_sort(sequence)

# 3.选择排序
# +++自己理解的算法：
def select_sort_mi(seq):
    for i in range(len(seq)-1):
        for j in range(i+1,len(seq)):
            if seq[i]>seq[j]:
                seq[i],seq[j]=seq[j],seq[i]
    print(li)

# li=[13,54,68,6,8,9,1,0]
# select_sort_mi(li)

# ++++++网上搜的：
def find_minimal_index(seq):
    min_elem=seq[0]
    count=0
    min_elem_index=count
    for elem in seq[1:]:
        count +=1
        if elem < min_elem:
            elem,min_elem=min_elem,elem
            min_elem_index=count
    return min_elem_index

def select_sort(sequence):
    seq=sequence[:]
    length=len(seq)
    for i in range(length):
        index=find_minimal_index(seq[i:])
        seq[index+i],seq[i]=seq[i],seq[index+i]
    return seq

# li=[13,54,68,6,8,9,1,0]
# print(select_sort(li))

# 4.插入排序
def insert_sort(lists):
    count=len(lists)
    for i in range(1,count):
        key=lists[i]
        j=i-1
        while j>=0:
            if lists[j]>key:
                lists[j+1]=lists[j]
                lists[j]=key
            j-=1
    return lists

# li=[13,54,68,6,8,9,1,0]
# print(insert_sort(li))

# =====判断某字符串是否包含另一个字符串
def iscontain(str1,str2):
    if str2 in str1:
        print('%s包含%s'%(str1,str2))
    else:
        print('%s不包含%s' % (str1, str2))

iscontain('123','')