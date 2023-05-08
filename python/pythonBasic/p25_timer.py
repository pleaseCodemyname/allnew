def counter2():
    t = [0 , 0]
    def increment():
        t[1] += 1
        return t[1]
    return increment

timer = counter2()
print(timer())
print(timer())


