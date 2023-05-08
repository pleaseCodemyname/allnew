import threading #thread덩어리가 뭉쳐져아 여러개가 동시에 작동함

def example():
    for _ in range(1, 10):
        print(_)

threading.Thread(target=example).start()
threading.Thread(target=example).start()