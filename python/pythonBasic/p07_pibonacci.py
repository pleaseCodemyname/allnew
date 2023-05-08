#!/usr/bin/env python

# f(x) = f(x-1) + f(x-2)

num = 1
prev = 0
cur = 1

while num < 10:  #python은 indent 때문에 오류가 날 수도 있음
    next = cur + prev    #IndentationError: 인덴트 에러
    print("%3d : %d " % (num, next))  #%3은 3자리수(%3d = 01, 02 이런식으로 나옴)
    prev = cur
    cur = next
    num += 1


##int, long - 정수 (4byte)
