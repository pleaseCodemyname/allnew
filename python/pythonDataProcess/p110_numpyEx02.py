import numpy as np

a = np.array([-1, 3, 2, -6])
b = np.array([3, 6, 1, 2])
A = np.reshape(a, [2, 2]) #2행 2열로 바뀜
B = np.reshape(b, [2, 2]) #2행 2열로 바뀜
print("\nsol1")
print(A) # [[-1 3] [2 -6]
print("\nsol2")
print(B) # [[3 6] [1 2]]

result3_1 = np.matmul(A, B)
result3_2 = np.matmul(B, A)
print("\nsol3-1")
print(result3_1) # [[0 0][0 0]]
print("\nsol3-2")
print(result3_2) # [[9 -27][3 -9]]

a = np.reshape(a, [1, 4]) #배열의 형상을 바꿔줌
print(a) #[[-1 3 2 -6]]
b = np.reshape(b, [1, 4]) #1행 4열
b2 = np.transpose(b)
print("\nsol4-1")
print(b2) #[[3][6][1][2]]

result4 = np.matmul(a, b2)
print("\nsol4-2")
print(result4)

#mattrix multiply
# A = [[-1, 3],
#      [2, -6]]
#
# B = [[3, 6],
#      [1, 2]]
#
# A × B = [[-1 × 3 + 3 × 1, -1 × 6 + 3 × 2],
# [2 × 3 - 6 × 1, 2 × 6 - 6 × 2]]
#
# = [[0, 0],
#    [0, 0]]
#
# B × A = [[3 × (-1) + 6 × 2, 3 × 3 + 6 × (-6)],
# [1 × (-1) + 2 × 2, 1 × 3 + 2 × (-6)]]
#
# = [[9, -27],
#    [3, -9]]
