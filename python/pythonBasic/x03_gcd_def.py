def gcd(a, b):
    if a < b:
        a, b = b, a
    print("gcd", (a,b))
    while b != 0:
        r = a % b #r=4
        a = b #a= 28
        b = r
        print("gcd", (a, b))
    return a

a = int(input("Input First number : "))
b = int(input("Input Second number : "))
print(f'gcd {a}, {b} of {a}, {b} : {gcd(a,b)}')


def gcd(a, b):
    print("gcd", (a, b))
    while b != 0:
        r = a % b #28 % 60 = 4(r)
        a = b #
        b = r
        print("gcd", (a, b))
    return a

a = int(input("Input First number : "))
b = int(input("Input Second number : "))

print(f'gcd({a}, {b}) of {a}, {b} : {gcd(a, b)}')











# def gcd(a, b):
#     while b:
#         a, b = b, a % b # a를 b로, b를 a를 b로 나눈 나머지로 대체
#     return a
#
# a = int(input("Input First number: "))
# b = int(input("Input Second number: "))
# result = gcd(a, b)
# print(f"gcd({a}, {b}) = {result}")