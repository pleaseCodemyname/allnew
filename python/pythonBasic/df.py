# # a= str(10)
# # print(len(a))
# # print((a[0]))
# # print((a[1]))
#
# numbers = (i for i in range(1, 101))
#
# game = (("짝' if('3' in str(i) or '6' in str(i) or '9' in str(i))
#         else str(i) for i in numbers
#
# print(list(game))
# print(type(numbers))
#
# numbers = (i for i in range(1, 101))
# for i in numbers:
#     if i == 3 or i == 6 or i == 9:
#         print("짝")
#     elif len(str(i[0])) == 3 or len(str(i[0])) == 6 or len(str(i[0])) == 9:
#         print("짝짝")
#     else:
#         print(i)

# 나는 이런식으로 생각
#
# 짝꿍 빨리 소스 만드세요ㅕ~~~
# 나는 이런식으로 생각

# def game(numbers):
#     for number in numbers:
#         count = 0
#         if number % 10 in [3, 6, 9]:
#             count += 1
#         if number // 10 in [3, 6, 9]:
#             count += 1
#
#         if count == 1:
#             print("👏")
#         elif count == 2:
#             print("👏👏")
#         else:
#             print(number)
#
# numbers = (i for i in range(1, 101))
# game(numbers)