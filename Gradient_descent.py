import numpy as np

# 生成一些随机数据
# 这个简单的数据集满足 y = 2x 的线性关系，我们的目标是通过梯度下降算法找到拟合这个关系的参数
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# 初始化参数
# b 是线性回归模型中的截距项，k 是斜率项
# 我们将它们初始化为 0，后续会通过梯度下降算法不断更新它们的值
b = 0
k = 0
# 学习率，控制每次参数更新的步长
# 学习率过大可能导致算法无法收敛，过小则会使收敛速度变慢
learning_rate = 0.1
# 迭代次数，即梯度下降算法重复执行的次数
epochs = 100

# 梯度下降算法
# 开始迭代更新参数
for _ in range(epochs):
    # 计算预测值
    # 根据当前的 k 和 b 值，使用线性回归模型 y = kx+b 计算预测值
    y_pred = k * x + b

    # 计算损失函数
    # 这里使用方差（MSE）作为损失函数
    loss = np.mean((y_pred - y) ** 2)

    # 计算梯度
    # 对于均方误差损失函数f(k,b)，求k和b的偏导数
    d_b = np.mean(y_pred - y)
    d_k = np.mean((y_pred - y) * x)

    # 更新参数
    # 根据梯度下降算法的更新规则：k = k - learning_rate * d_k
    # 其中 k 是参数，learning_rate 是学习率，d_k 是参数的梯度
    # 通过减去学习率乘以梯度的方式更新参数，使得损失函数朝着减小的方向移动
    b -= learning_rate * d_b
    k -= learning_rate * d_k

# 输出最终的参数值
print("b:", b)
print("k:", k)