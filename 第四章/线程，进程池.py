from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(100):
        print(name,i)

if __name__=='__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):#将100个任务交给线程池
            t.submit(fn,name=f"任务{i}")
    #等待线程池任务全部执行完毕
    print("over")