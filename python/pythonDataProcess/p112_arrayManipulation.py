import numpy as np

print('\np.repeat function')
su1 = 2
rep_cnt = 5
result = np.repeat(su1, rep_cnt)
print(type(result)) #<class 'numpy.ndarray'>
print(result) #[2 2 2 2 2]

array1 = np.array([1, 2])
array2 = np.array([3, 4])
print('\narray1')
print(array1) #[1 2]
print('\narray2')
print(array2) #[3 4]

print('\nnp.concatenate function')
result = np.concatenate((array1, array2)) #[1 2 3 4]
print(result)

su2 = 3
rep_cnt2 = 4
print('\nfunction repeat')
abcd = np.repeat(su1, rep_cnt)
defg = np.repeat(su2, rep_cnt2)
result = np.concatenate((abcd, defg))
print(result) #[2 2 2 2 2 3 3 3 3 ]

array3 = np.array([1, 2, 3, 4, 5, 6])
print('\nreshape function')

print('2row 3col')
result = np.reshape(array3, [2, 3])
print(result) # [[1 2 3]
            # [4 5 6]]

print('3row 2col')
result = np.reshape(array3, [3, 2])
print(result) #[1 2]
              #[3 4]
              #[5 6]

array4 = np.array([[3, 6, 2], [4, 1, 5]])
print('\narray4')
print(array4) #[[3 6 2]
              #[[4 1 5]

print('\ntransposed array')
result = np.transpose(array4)
print(result) #[3 4]
              #[6 1]
              #[2 5]