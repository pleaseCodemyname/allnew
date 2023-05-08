# f(x) = x * f(x-1), f(x)= 1
def factorial(n):
    if n <= 1:
        return 1 #1하고 같은 순간까지
    else:
        return n * factorial(n -1) #recursive 함수(재귀함수)

n = input("Input number : ")
print("{} factorial is {}".format(n, factorial(int(n))))