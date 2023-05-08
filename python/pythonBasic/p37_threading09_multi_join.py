import threading, time

class sample(threading.Thread):
    def __init__(self, time):
        super(sample, self).__init__()
        self.time = time
        self.start()

    def run(self):
        print(self.time, " starts")
        for i in range(0, self.time):
            time.sleep(1)
        print(self.time, "has finished")

t1 = sample(3) #t1이 먼저 선언되어도 print에서 t1이 나중에 나오면 나중에 출력됨
t2 = sample(2)
t3 = sample(1)
t3.join()
print("t3.join() has finished")
t2.join()
print("t2.join() has finished")
t1.join()
print("t1.join() has finished")