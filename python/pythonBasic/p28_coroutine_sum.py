def handler():
    print("Initialize Handler")
    while True:
        v1, v2 = (yield )
        print(f"{v1} + {v2} = {v1 + v2}")

listener = handler()
listener.__next__() #next를 적용해야 yield에서 멈춘다. 아니면 계속 반복함
listener.send([5, 4]) #listener.send(1)하면 yield로 들어가고, value = 1 이됨
listener.send([3, 6])

def handler():
    print("Initialize Handler")
    while True:
        value = (yield)
        print("%s + %s = %s" % (value[0], value[1], value[0] + value[1]))

listener = handler()
listener.__next__()
listener.send([5,4])