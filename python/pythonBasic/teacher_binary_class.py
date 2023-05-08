import random

class Binary_digits(object):
    def __init__(self, num, lists):
        self.num = num
        self.lists = lists
    def convert(self):
        q = self.num
        lists = self.lists
        while True:
            r = q % 2 #나머지 값을 반환
            q = q //2
            lists.append(r) # 나머지 값을 넣음
            if q == 0: # 몫이 0이면 break
                break
            lists.reverse() #list선수를 반대로
            return lists

    lists = []
    num = random.randrange(4, 16)
    binary = Binary_digits(num, lists)
    print(f'{num} binary number is : {binary.convert()}')