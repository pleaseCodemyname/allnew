def division_function(a, b):
    try:
        print(a / b)
    except TypeError as e:
        return -1
    except ZeroDivisionError as e:
        return -2
    except Exception as e:
        return -3

ret = division_function("a", 1)
print(ret)
ret = division_function(1, 0)
print(ret)
ret = division_function(4, 2) #Error가 없음
if ret != None: #None이 아니기 때문에 뭔가 에러가 났다는 의미
    print("Error")
#Error가 없으면 None, return으로 받으면 가능함