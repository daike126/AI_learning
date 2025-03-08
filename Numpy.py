# 导入 NumPy 库，并使用别名 np，方便后续调用
import numpy as np

# 创建数组部分

# 使用 np.array() 函数将 Python 列表转换为 NumPy 数组
a = np.array([1, 2, 3, 4, 5])
print("使用 np.array() 创建的一维数组 a:", a)

# 使用 np.arange() 函数创建数组，类似于 Python 的 range 函数
# 从 0 开始，以 2 为步长，到 10（不包括 10）
b = np.arange(0, 10, 2)
print("使用 np.arange() 创建的一维数组 b:", b)

# 使用 np.zeros() 函数创建一个 3 行 4 列的全零数组
c = np.zeros((3, 4))
print("使用 np.zeros() 创建的 3 行 4 列全零数组 c:\n", c)

# 使用 np.ones() 函数创建一个 2 行 3 列的全一数组
d = np.ones((2, 3))
print("使用 np.ones() 创建的 2 行 3 列全一数组 d:\n", d)

# 数组的属性部分

# 创建一个二维数组
e = np.array([[1, 2, 3], [4, 5, 6]])
# shape 属性返回数组的形状，即每个维度的大小
print("数组 e 的形状:", e.shape)

# 创建一个包含浮点数的数组
f = np.array([1.0, 2.0, 3.0])
# dtype 属性返回数组中元素的数据类型
print("数组 f 中元素的数据类型:", f.dtype)

# 数组的运算部分

# 创建两个一维数组
g = np.array([1, 2, 3])
h = np.array([4, 5, 6])
# 数组的加法运算，是元素级的操作
i = g + h
# 数组的乘法运算，也是元素级的操作
j = g * h
print("数组 g 和 h 相加的结果:", i)
print("数组 g 和 h 相乘的结果:", j)

# 创建两个二维数组
k = np.array([[1, 2], [3, 4]])
l = np.array([[5, 6], [7, 8]])
# 使用 dot 函数进行矩阵乘法
m = k.dot(l)
# 也可以使用 @ 运算符进行矩阵乘法
n = k @ l
print("使用 dot 函数进行矩阵乘法的结果:\n", m)
print("使用 @ 运算符进行矩阵乘法的结果:\n", n)

# 数组的索引和切片部分

# 创建一个一维数组
o = np.array([10, 20, 30, 40, 50])
# 通过索引访问数组中的元素，索引从 0 开始
print("数组 o 中索引为 2 的元素:", o[2])

# 创建一个二维数组
p = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 对于二维数组，使用两个索引来访问元素
print("数组 p 中第 2 行第 3 列的元素:", p[1, 2])

# 创建一个一维数组
q = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 使用切片操作获取数组的一部分
# 从索引 2 开始，到索引 7（不包括 7），步长为 2
r = q[2:7:2]
print("数组 q 切片后的结果:", r)
