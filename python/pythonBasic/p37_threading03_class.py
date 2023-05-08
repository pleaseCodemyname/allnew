import threading, requests, time  #thread 뭉치, 여러개가 동시에 동작 가능

class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self): #run은 기본 태그
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')
t = HtmlGetter('http://google.com')
t.start()

print('### End ###')

# 즉, 위 코드에서 HtmlGetter 스레드는 requests 모듈을 사용하여 인스턴스 변수 self.url에 저장된 URL로 HTTP GET 요청을 보내고,
# 이에 대한 서버 응답으로 받은 본문을 resp.text 속성에서 문자열로 가져와서 출력합니다. 이때 len(resp.text)는 받아온 문자열의 길이를 의미합니다.