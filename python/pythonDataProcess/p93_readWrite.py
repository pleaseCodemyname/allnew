myfile01 = open('sample.txt', 'rt', encoding='UTF-8')
linelists = myfile01.readlines()
myfile01.close() #\n은 띄어쓰기임
print(linelists) # ['70\n', '60\n', '55\n', '75\n', '95\n', '90\n', '80\n', '80\n', '85\n', '100']

myfile02 = open('result.txt', 'wt', encoding='UTF-8')

total = 0
for one in linelists:
    score = int(one)
    total += score
    myfile02.write('total = ' + str(total) + ', value = ' + str(score) + '\n') #wt이기 때문에 str값을
average = total / len(linelists)


# print(total) # 790
# print(average) # 79.0

myfile02 = open('result.txt', 'wt', encoding='UTF-8') #wt = write type
myfile02.write('총점 : ' + str(total) + '\n') #\n 은 Enter 역할
myfile02.write('평균: ' + str(average))
myfile02.close()
print("done~!!")

myfile03 = open('result.txt', 'rt', encoding='UTF-8') #rt = read type
line = 1
while line:
    line = myfile03.readline()
    print(line) # 총점 : 790 / 평균: 79.0
myfile03.close()

# myfile02 = open('result.txt', 'wt', encoding='UTF-8') #wt = write type
# for i in range(0, 11):
#     i += 1
# myfile02.write('total : ' + linelists[i], )

