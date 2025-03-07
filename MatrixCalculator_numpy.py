import numpy as np

# 当 try 块中的代码抛出 ValueError 异常时，程序会跳转到 except 块。
# 在计算时，数组如果不满足条件，numpy 会抛出 ValueError 异常。
# 矩阵加法
def matrix_add(m1, m2):
    try:
        m1 = np.array(m1)
        m2 = np.array(m2)
        return m1 + m2
    except ValueError:
        print("矩阵A列数与矩阵B维度不同,矩阵无法相加！")
        return None

# 矩阵乘法
def matrix_multiply(A, B):
    try:
        A = np.array(A)
        B = np.array(B)
        return np.dot(A, B)
    except ValueError:
        print("矩阵A列数与矩阵B行数不相等,矩阵无法相乘！")
        return None

# 矩阵转置
def matrix_transpose(matrix):
    matrix = np.array(matrix)
    return matrix.T

# 辅助函数：获取用户输入的矩阵
def get_matrix_input(prompt):
    print(prompt)
    rows = int(input("请输入矩阵的行数: "))
    cols = int(input("请输入矩阵的列数: "))
    matrix = []
    for m in range(rows):
        row = input(f"请输入第 {m + 1} 行的元素，用逗号分隔: ").split(",")
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