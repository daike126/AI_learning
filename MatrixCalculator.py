#嵌套列表：m1[[1,2],[3,4]]
#矩阵加法
def matrix_add(m1,m2):
    if len(m1) != len(m2) or len(m1) != len(m2):
        print("矩阵A列数与矩阵B维度不同,矩阵无法相加！")
        return None
    else:
        # 嵌套列表推导式:
        return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
#推导过程：
# m1=[[1,2],    m1[0][0]+m2[0][0]
#     [3,4]]    m1[0][1]+m2[0][1]
# m2=[[5,6],    m1[1][0]+m2[1][0]
#     [7,8]]    m1[1][1]+m2[1][1]

#矩阵乘法
def matrix_multiply(A,B):
    if len(A[0]) != len(B):
        print("矩阵A列数与矩阵B行数不相等,矩阵无法相乘！")
        return None
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
#推导过程：
# 假设一个m*n的矩阵A，和一个p*q的矩阵B，先判断n是否等于p。
# 结果为m*q的矩阵C，循环x和y将按顺序遍历结果矩阵C，循环x和z将按顺序遍历矩阵A，循环y和z将按顺序遍历矩阵B。
# 通过矩阵乘法公式推得：Cxy = Axz * Bzy
# result[x][y] 通过 += 完成一系列乘积 A[x][z] * B[z][y] 累加的结果。

#矩阵转置
def matrix_transpose(matrix):
    return [[matrix[m][n]for m in range(len(matrix))]for n in range(len(matrix[0]))]
#推导过程：
# [1,2,3][4,5,6] m*n转置后:
# [1,4][2,5][3,6] n*m

# 辅助函数：获取用户输入的矩阵
def get_matrix_input(prompt):
    print(prompt)
    rows = input("请输入矩阵的行数: ")
    cols = input("请输入矩阵的列数: ")
    rows, cols = int(rows), int(cols)
    matrix = []
    for m in range(rows):
        #split()：用于将字符串按照指定符合分割成多个子字符串，并返回一个包含这些子字符串的列表。
        row = input(f"请输入第 {m + 1} 行的元素，用空格分隔: ").split(",")
        row = [int(num) for num in row]
        if len(row) != cols:
            print("输入的元素数量与列数不匹配，请重新输入。")
            return get_matrix_input(prompt)
        matrix.append(row)
    return matrix

while True:
    print("\n请选择要进行的运算：")
    print("1. 矩阵加法")
    print("2. 矩阵乘法")
    print("3. 矩阵转置")
    print("4. 退出")
    choice = input("请输入选项编号: ")

    if choice == '1':
        m1 = get_matrix_input("请输入第一个矩阵的信息：")
        m2 = get_matrix_input("请输入第二个矩阵的信息：")
        result = matrix_add(m1, m2)
        print("矩阵相加的结果是:", result)
    elif choice == '2':
        A = get_matrix_input("请输入第一个矩阵的信息：")
        B = get_matrix_input("请输入第二个矩阵的信息：")
        result = matrix_multiply(A, B)
        print("矩阵相乘的结果是:", result)
    elif choice == '3':
        matrix = get_matrix_input("请输入要转置的矩阵的信息：")
        result = matrix_transpose(matrix)
        print("矩阵转置的结果是:", result)
    elif choice == '4':
        print("退出程序。")
        break
    else:
        print("无效的选项，请重新输入。")