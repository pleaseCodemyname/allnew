# while True:
#     n = input("input number (q : quit) : ")
#
#     if n == 'q':
#         print("Exit")
#         break
#
#     n = int(n)
#
#     if (n < 2 or n > 9):
#         print("input number range 2~9!!")
#         continue;
#     else:
#         for c in range(1, 10):
#             print(f'{n} * {c} = {n * c}')


while True:
    n = input("input number (q : quit) : ")

    if n == 'q':
        print("Exit")
        break
    elif (int(n) < 2 or int(n) > 10):
        print("input number range 2~9!!")
    else:
        for m in range(1, 10):
            print(f'{n} * {m} = {n * m}')



