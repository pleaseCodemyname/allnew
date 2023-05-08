m = 0
n = 1
def func():
    m = 0
    global n # 1
    m += 1 # m = 1
    n += 1 #스코프 내부 n = 2
    print(f'{m} vs {n}') # m = 1 n = 2
func()
print(m, n)