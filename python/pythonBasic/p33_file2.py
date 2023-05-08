f = open("out.txt", "w") #open("txt명", "w"(쓰기 가능))
f.write("This file is  %s \n" % ("out.txt"))
f.write("end of file")
f.close() #out.txt파일에 작성하지 않았지만, 여기서 작성해서 파일안헤 포함 시킬 수 있음

f = open("out.txt", "r")
line = 1
while line:
    line = f.readline()
    print(line)
f.close()