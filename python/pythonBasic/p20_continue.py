sum = 0
for i in range(10): #0~9까지 진행
    if i % 2 ==0: # 2로 나눌때 0(짝수면) continue(아무것도 출력없이 내련감)
        continue
    sum += i #sum은 1씩 증가(1, 3, 5, 7, 9)
    print(f'sum += {i}')
print()
print(f"sum = {sum}") #sum은 5번코드에서 영향을 받아, 1, 3, 5, 7 ,9