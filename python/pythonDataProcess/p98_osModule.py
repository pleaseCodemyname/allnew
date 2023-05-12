#폴더 안에 파일을 만들때  zfill(2) 파일명 2자리로 채움
import os

myfolder = './'
newpath = os.path.join(myfolder, 'work') #work라는 폴더를 만듬

try:
    os.mkdir(path=newpath)

    for idx in range(1, 11):
        newfile = os.path.join(newpath, 'somefolder' + str(idx).zfill(2)) #zfill(2자리를 채울 때)
        os.mkdir(path=newfile)
except FileExistsError:
    print('Directory exist already...')
print('finished')