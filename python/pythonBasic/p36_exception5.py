def division_function(a, b): #Exception에 넣는 순서가 중요함
    try:
        print(a / b)
    except TypeError as e:
        print('First')
    except ZeroDivisionError as e:
        print('Second')
    except Exception as e: #다른에러를 처리하려면 Exception을 맨 마지막에 넣기
        print('Third')

division_function("a", 1)
division_function(1, 0)
division_function(4, 2)
