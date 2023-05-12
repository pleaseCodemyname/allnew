someList = ['김의찬', '유만식', '이영철', '심수련', '윤기석', '노윤희','황우철']
print(someList)
print(someList[4])
print(someList[-2])
print(someList[1:4])
print(someList[4:])
length = len(someList)
print(length) # 7
print(someList[:length:2]) #짝수 [시작:끝:몇칸씩] ['김의찬', '이영철', '윤기석', '황우철']
print(someList[1:length:2]) # 홀수 ['유만식', '심수련', '노윤희']

# 해당 코드는 리스트 someList의 인덱스 0부터 length-1까지의 요소들 중에서 짝수 인덱스에 해당하는 요소들과 홀수 인덱스에 해당하는 요소들을 각각 출력하는 코드입니다.
#
# somelist[:length:2]는 리스트 somelist에서 0부터 length-1까지의 인덱스 중에서 2씩 건너뛰며 요소를 출력합니다. 이 때, 0, 2, 4, 6 등 짝수 인덱스에 해당하는 요소들이 출력됩니다.
#
# somelist[1:length:2]는 리스트 somelist에서 1부터 length-1까지의 인덱스 중에서 2씩 건너뛰며 요소를 출력합니다. 이 때, 1, 3, 5, 7 등 홀수 인덱스에 해당하는 요소들이 출력됩니다.