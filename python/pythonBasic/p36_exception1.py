try:
    f = open("test.txt", "r") #try except는 무조건 set
except IOError as e:
    print(e)
finally:
    data = f.readline()
    print(data)
    f.close()