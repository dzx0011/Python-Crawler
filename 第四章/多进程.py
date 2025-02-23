from multiprocessing import Process
import time
#创建进程和线程的api高度相似
def func(a1):
    for i in range(100):
        print(f"子进程{a1}",i)

if __name__=="__main__":
    p=Process(target=func,args=("poppy",))#传参
    p.start()
    #time.sleep(1)由于进程启动的开销，子进程在加载过程中主进程先进行
    for i in range(100):
        print("主进程",i)
