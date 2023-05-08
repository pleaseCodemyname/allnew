def handler():
    print("Initialize Handler")
    while True:
        value = (yield )
        print("Received %s " % value)

listener = handler()
listener.__next__()
listener.send(1) #listener.send(1)하면 yield로 들어가고, value = 1 이됨
listener.send("message")
#coroutine을 사용하는 이유?
