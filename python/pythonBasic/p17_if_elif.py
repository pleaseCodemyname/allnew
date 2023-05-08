while True:
    i = input("Input the number(q : QUit) : ")

    if i == 'q': #i == q  break(그만 할 것임)
        break
    else:
        if int(i) > 0:
            print("This is positive")
        elif int(i) == 0:  #원하는 형태로 바꾸는 것(정수형으로 바꾸어 사용하겠다) == Casting이라고 함
            print("This is zero")
        else:
            print("This is negative")

while Ture:
    i = input("Input the number(q : QUit): ")

    if i == 'q':
        break
    else:
        if int(i) > 0:
            print("positive")
        elif int(i) == 0:
            print("zero")
        else:
            print("negative")
