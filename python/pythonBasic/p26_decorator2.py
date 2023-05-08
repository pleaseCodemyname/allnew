import datetime
#
def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

#CRUD 구현할 때 사용하기 좋음(Template)
@datetime_deco
def func1(): # select
    print("Main Function1 start")

@datetime_deco
def func2(): #insert
    print("Main Function2 start")

@datetime_deco
def func3(): #delete
    print("Main Function3 start")

func1()
func2()
func3()