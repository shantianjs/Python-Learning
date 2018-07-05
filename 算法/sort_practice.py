from functools import wraps
import random
import inspect
import time
import math
'''
it\' a basal practice of sort algorism.
include merge_sort,bubble_sort,selection_sort,quick_sort,radix_sort
'''

def timecounter(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        start = time.perf_counter()
        f(*args,**kwargs)
        use_time = time.perf_counter() - start
        print(use_time)
    return decorated_function

def generator(num):
    li = [x for x in range(1,int(num))]
    random.shuffle(li)
    return li

#归并排序
def merge(left,right):
    response = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            response.append(left[i])
            i+=1
        else:
            response.append((right[j]))
            j+=1
    response+=left[i:]
    response+=right[j:]
    return response

def merge_sort(list):
    if len(list)<2:
        return list
    center = int(len(list)/2)
    left = merge_sort(list[:center])
    right = merge_sort(list[center:])
    return merge(left,right)

#选择排序
def selection_sort(lists):
    sorted_list = []
    while lists:
        min_num = lists[0]
        for i in lists:
            if i<min_num :
                min_num = i
        sorted_list.append(min_num)
        lists.remove(min_num)
        print(min_num)
    return sorted_list

#冒泡排序
def bubble_sort(li=[]):
    max_index = len(li)-1
    while max_index>0:
        for i in range(max_index):
            if li[i+1] < li[i]:
                li[i+1],li[i] = li[i],li[i+1]
        max_index-=1
    return li

#快速排序
def quick_sort(li):
    if len(li) < 2:
        return li
    key = random.choice(li)
    less = []
    greater = []
    for i in li:
        if i<= key:
            less.append(i)
        else:
            greater.append(i)
    # less = [x for x in li if x<=key]
    # greater = [x for x in li if x>key]
    return quick_sort(less) + quick_sort(greater)

#基数排序
@timecounter
def radix_sort(li=[],radix=10):
     k = math.ceil(math.log(max(li),radix)) #最大数的位数
     for i in range(1,k+1): #分析全部位数
         bucket = [[] for i in range(radix)]
         for val in li:
             bucket[int(val%(radix**i)/radix**(i-1))].append(val)
         li.clear()
         for each in bucket:
             li.extend(each)
     return li

@timecounter
def wrap(*args):
    quick_sort(*args)

#堆排序
def build_heap():
    pass

print(wrap(generator(10000)))