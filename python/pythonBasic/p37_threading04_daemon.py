import threading, requests, time  #thread 뭉치, 여러개가 동시에 동작 가능

"""
Thread Class 속성 중 daemon 속성은 sub thread가 daemon thread인지 여부를 지정.
daemon thread는 Background thread로 Main thread가 종료되면 즉시 종료됨.
반면, daemon thread가 아닌 thread는 Main thread와 관계없이 자신의 작업이 끝날때까지 계속 실행되는 특징이 있음.
"""
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1) #count하는 시간이 있어야해서 time을 가져옴, 일정의 시간을 줌
    print(url, len(resp.text), ' chars') #작업이 끝나버렸음 MainThread는 print 되자마자 끝나버림
t = threading.Thread(target=getHtml, args=('http://google.com',))
t.daemon = True
t.start()

print('### End ###')
#Thread를 사용하는 이유? Main Thread 무한 반복 걸어놓고 센서 데이터