
#作业二：
#自定义一个 python 函数，实现 map() 函数的功能。
#https://blog.51cto.com/suhaozhi/1907951
#https://zhuanlan.zhihu.com/p/180522145
# def myMap(f, iterable):
#加* 参数就是元组类型

def myMap(f, *iterable):

    map_list=[]
    for i in  iterable:

        for j in i:
           map_list.append(f( j ))
           # map_list.append(f( int(i) ))

    return map_list
   # return [ myadd(i) for i in list(args)]
def myadd(a):
    return a*a


listx=[1,2,3,4]
#不能取名为list
print(myMap(myadd,listx))


