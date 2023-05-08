import threading, queue, time

work = queue.Queue()

def generator(start, end): #1~10을 반복하는 반복문
    for _ in range(start, end): # 1~10값이 들어감 from threading.Thread
        work.put(_)
def display(): #work가 비면 0값을 줌 그게 end임
    while work.empty() is False:
        data = work.get()
        print('data is ' + str(data))
        time.sleep(1)
        work.task_done()

threading.Thread(target=generator, args = (1, 10)).start()
threading.Thread(target=display).start()
work.join() #work의 task_done과 queue.Queue()를 join한다는 의미 같음