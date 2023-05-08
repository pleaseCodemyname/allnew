import random

class findMax(object):
    def __init__(self,data):
        self.data = data
    def max(self):
        max = self.data[0] #data의 1번째를 max에다가 담음
        for i in range(len(self.data)): #data의 개수만큼 반복
            if self.data[i] > max: #데이터의 개수가 max보다 넘기면
                max = self.data[i] #max를 i 만큼 돌림
        return max

data = random.sample(range(1, 101), 10)
print(data)

data1 = findMax(data)
print(f'Max value is : {data1.max()}')