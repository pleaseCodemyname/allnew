f = open("test.txt") #test.txt 파일을 import
line =1;
while line:
    line = f.readline()
    print(line)
f.close()

#read only임 (w)를 적어줘야 write도 가능함