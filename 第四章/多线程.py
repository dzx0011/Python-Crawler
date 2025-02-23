from threading import Thread

#start安排新线程来执行run

#使用target参数
def func():
    for i in range(20):
        print("func",i)

if __name__=="__main__":
    t=Thread(target=func)
    t.start()
    for i in range(20):
        print("main",i)

#重写run方法
class myThread(Thread):
    def run(self):
        for i in range(20):
            print("func",i)

if __name__=="__main__":
    t=myThread()
    t.start()
    for i in range(20):
        print("main",i)