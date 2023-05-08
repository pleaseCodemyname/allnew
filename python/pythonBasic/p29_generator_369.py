for i in range(1, 101):
    if i < 10:
        if str(i)[0] == '3' or str(i)[0] == '6' or str(i)[0] == '9':
            print("짝")
        else:
            print(i)
    else:
        if (str(i)[0] == '3' or str(i)[0] == '6' or str(i)[0] == '9') and (str(i)[1] == '3' or str(i)[1] == '6' or str(i)[1] == '9'):
            print("짝짝")
        elif (str(i)[0] == '3' or str(i)[0] == '6' or str(i)[0] == '9') or (str(i)[1] == '3' or str(i)[1] == '6' or str(i)[1] == '9'):
            print("짝")
        else:
            print(i)


#숫자


# #민희
# for i in range(1, 101):
#     if i < 10:
#         if i in (3, 6, 9):
#             print("짝")
#         else:
#             print(i)
#     else:
#         i = str(i)
#         if i[0] in ['3', '6', '9'] and i[1] in ['3', '6', '9']:
#             print("짝짝")
#         elif i[0] in ['3', '6', '9'] or i[1] in ['3', '6', '9']:
#             print("짝")
#         else:
#             print(i)
# # 강사님
# numbers = (i for i in range(1, 101))
#
# data = list(numbers)
#
# item = [3, 6, 9]
#
# for i in data:
#     n10 = int(i/10)
#     n1 = i % 10
#     if i % 10 == 1:
#         print()
#     if i < 10:
#         if i in item:
#             print('짝', end="")
#         else:
#             print("%4d" % i, end="")
#     else:
#         if n10 in item and n1 in item:
#             print('짝짝', end="")
#         elif n10 in item or n1 in item:
#             print('짝', end="")
#         else:
#             print("%4d" % i , end="")