import threading  #thread 뭉치, 여러개가 동시에 동작 가능

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print('Sub Thread : ', total)
t = threading.Thread(target=sum, args=(1, 100000))
t.start()

print('Main Thread')

#Thread는 실행의 순서를 보장하지 않는다