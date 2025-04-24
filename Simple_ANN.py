import numpy as np
from sklearn.datasets import load_iris

# 1. 极简神经网络框架
# 数据准备（二分类简化版）
X, y = load_iris(return_X_y=True)
X = X[y != 2, :2]  # 只用前两个特征 + 前两个类别
y = y[y != 2].reshape(-1, 1)  # 变成列向量

# 网络参数初始化
def init_weights(input_size, hidden_size, output_size):
    np.random.seed(42)  # 固定随机种子（方便复现）
    W1 = np.random.randn(input_size, hidden_size) * 0.01  # 输入→隐藏层权重
    b1 = np.zeros((1, hidden_size))                       # 隐藏层偏置
    W2 = np.random.randn(hidden_size, output_size) * 0.01  # 隐藏层→输出权重
    b2 = np.zeros((1, output_size))                       # 输出层偏置
    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

params = init_weights(input_size=2, hidden_size=4, output_size=1)  # 2输入→4神经元→1输出

# 2. 前向传播
def forward(X, params):
    # 隐藏层计算
    Z1 = np.dot(X, params["W1"]) + params["b1"]
    A1 = 1 / (1 + np.exp(-Z1))  # Sigmoid激活

    # 输出层计算
    Z2 = np.dot(A1, params["W2"]) + params["b2"]
    A2 = 1 / (1 + np.exp(-Z2))  # 输出概率
    return {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}

# 3. 反向传播
def backward(X, y, params, cache):
    m = X.shape[0]  # 样本数量

    # 输出层梯度
    dZ2 = cache["A2"] - y  # 交叉熵对Z2的导数
    dW2 = np.dot(cache["A1"].T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    # 隐藏层梯度（链式法则）
    dA1 = np.dot(dZ2, params["W2"].T)
    dZ1 = dA1 * cache["A1"] * (1 - cache["A1"])  # Sigmoid导数
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    return {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

# 4. 训练循环（梯度下降）
def train(X, y, epochs=1000, lr=0.1):
    params = init_weights(2, 4, 1)  # 初始化参数

    for i in range(epochs):
        # 前向传播
        cache = forward(X, params)

        # 反向传播计算梯度
        grads = backward(X, y, params, cache)

        # 参数更新（梯度下降）
        params["W1"] -= lr * grads["dW1"]
        params["b1"] -= lr * grads["db1"]
        params["W2"] -= lr * grads["dW2"]
        params["b2"] -= lr * grads["db2"]

        # 每100次打印损失
        if i % 100 == 0:
            loss = -np.mean(y * np.log(cache["A2"]) + (1 - y) * np.log(1 - cache["A2"]))
            print(f"Epoch {i}, Loss: {loss:.4f}")
    return params

trained_params = train(X, y)  # 开训！

# 5. 预测与评估
def predict(X, params):
    cache = forward(X, params)
    return (cache["A2"] > 0.5).astype(int)  # 阈值0.5分类

y_pred = predict(X, trained_params)
accuracy = np.mean(y_pred == y)
print(f"准确率: {accuracy*100:.2f}%")  # 通常能达到95%+