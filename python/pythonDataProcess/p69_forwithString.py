mystring = "life is an egg"
mylist = mystring.split() #특정구분자를 기준으로 나누어 리스트로 만들어 반환해줌.
# 구분자를 지정하지 않으면 기본값인 공백(space)을 구분자로 사용해 문자열을 나눔

print(mylist) # ['life', 'is', 'an', 'egg']
print(len(mylist)) # 4

for idx in range(len(mylist)):
    if idx % 2 == 0:
        mylist[idx] = mylist[idx].upper() #Life #An
    else:
        mylist[idx] = mylist[idx].lower() #is #egg
print(mylist) #['Life', 'is' 'AN', 'egg']

result = '#'.join(mylist) #result : LIFE#is#AN#egg, 공백을 #으로 join함
print('result : ', result)

result = ''.join(mylist) #result : LIFEisANegg #공백을 줄임
print('result : ', result)

