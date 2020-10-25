#作业三：
#实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import datetime
import time


def timer(func, ):
    def decorator(*args,**kwargs):
        # ts=time.time()
        ts=datetime.datetime.now()
        print(f'start time{ts}')
        func(*args,**kwargs)
        #te=time.time()
        te=datetime.datetime.now()
        print(f'end time{te}')
        print("run all time",te-ts)
        return te-ts
    return decorator

@timer
def get_all(**kwargs):
    time.sleep(2)
    print ("excute")

get_all()
