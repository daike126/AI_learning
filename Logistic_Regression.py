import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 只取鸢尾花前两个类别（二分类），特征用花瓣宽度+长度
X, y = load_iris(return_X_y=True)
X = X[y != 2, 2:]  # 只保留类别0和1，特征选最后两列（花瓣）
y = y[y != 2]

# 训练逻辑回归模型
model = LogisticRegression()
model.fit(X, y)

# 获取预测概率
probabilities = model.predict_proba(X)[:, 1]  # 取正类概率

# 这里手动改阈值观察分类结果变化
threshold = 0.3  # 可试试0.3, 0.5, 0.7
custom_pred = (probabilities > threshold).astype(int)

# 打印混淆矩阵
from sklearn.metrics import confusion_matrix, accuracy_score
print("阈值=", threshold, "\n", confusion_matrix(y, custom_pred))

# 阈值 vs 性能可视化
thresholds = np.linspace(0.1, 0.9, 9)
for t in thresholds:
    pred = (probabilities > t).astype(int)
    acc = accuracy_score(y, pred)
    print(f"阈值={t:.1f}, 准确率={acc:.3f}")