list = []

try:
    while True:
        print('Item amount : ', len(list)) #list.append(item) 하면 갯수가 늘어남
        print('Inventory : ', list)

        if len(list) >= 4: #4개가 되면
            raise Exception('Inventory lack') #exception으로 보냄
        item = 'item' + str(len(list)) #문자는 문자로 묶어줘야함
        list.append(item)
except Exception as e: # 4개일때 오류
    print('Inventory Full')
    print(e) #e를 넣는 이유? 원인을 띄우는 것