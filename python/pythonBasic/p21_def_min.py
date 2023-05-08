def min(a, b):
    if a > b:
        return b
    else:
        return a

a = input("Input first number : ")
b = input("Input Second number : ")

print("{} vs {} : Min number = {}".format(a, b, min(a, b)))

# 몫과 나머지를 알려주는 함수 작성