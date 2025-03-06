#嵌套列表：m1[[1,2],[3,4]]
def matrix_add(m1,m2):
    # 嵌套列表推导式:
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

result = matrix_add([[1,2],[3,4]],[[5,6],[7,8]])
print(result)
#推导过程：
# m1=[[1,2],    m1[0][0]+m2[0][0]
#     [3,4]]    m1[0][1]+m2[0][1]
# m2=[[5,6],    m1[1][0]+m2[1][0]
#     [7,8]]    m1[1][1]+m2[1][1]

def matrix_multiply(A,B):
    if len(A[0]) != len(B):
        print("矩阵A列数与矩阵B行数不相等,矩阵无法相乘！")
    else:
        # 初始化结果矩阵
        result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        # 遍历矩阵A的m
        for x in range(len(A)):
            # 遍历矩阵B的q
            for y in range(len(B[0])):
                # 遍历矩阵A的n（也就是矩阵B的p）
                for z in range(len(A[0])):
                    result[x][y] += A[x][z] * B[z][y]
        return result

result = matrix_multiply([[1,2],[3,4]],[[5,6],[7,8]])
print(result)
#推导过程：
# 假设一个m*n的矩阵A，和一个p*q的矩阵B，先判断n是否等于p。
# 结果为m*q的矩阵C，循环x和y将按顺序遍历结果矩阵C，循环x和z将按顺序遍历矩阵A，循环y和z将按顺序遍历矩阵B。
# 通过矩阵乘法公式推得：Cxy = Axz * Bzy
# result[x][y] 通过 += 完成一系列乘积 A[x][z] * B[z][y] 累加的结果。

def matrix_transpose(matrix):
    return [[matrix[m][n]for m in range(len(matrix))]for n in range(len(matrix[0]))]

result = matrix_transpose([[1,2,3],[4,5,6]])
print(result)
#推导过程：
# [1,2,3][4,5,6] m*n转置后:
# [1,4][2,5][3,6] n*m