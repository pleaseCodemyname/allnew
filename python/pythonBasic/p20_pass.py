sum = 0
for i in range(10):
    if i % 2 ==0:
        pass #pass는 무시하지 않고 그대로 count함
    sum += i
    print(f'sum += {i}')
print()
print(f"sum = {sum}")

#pass를 사용하는이유? if else, try exception사용하는 경우, 뭘 해야할지 모르겠을때 pass를 일단 먼저 작성하고 생각나면 지우면서 진행