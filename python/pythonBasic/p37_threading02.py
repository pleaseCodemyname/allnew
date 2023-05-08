import threading, requests, time  #thread 뭉치, 여러개가 동시에 동작 가능

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1) #count하는 시간이 있어야해서 time을 가져옴, 일정의 시간을 줌
    print(url, len(resp.text), ' chars')
t = threading.Thread(target=getHtml, args=('http://google.com',))
t.start()

print('### End ###')

#Thread는 실행의 순서를 보장하지 않음