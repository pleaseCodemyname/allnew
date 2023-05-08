def convert2binary(num):
    temp = []

    while True:
        remainder = num % 2
        num = num //2
        temp.append(remainder)

        if num < 2:
            temp.append(num)
            break
