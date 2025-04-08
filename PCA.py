import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data
y = iris.target

# 创建 PCA 对象，指定降维后的维度为 2
pca = PCA(n_components=2)

# 对数据进行 PCA 降维
X_pca = pca.fit_transform(X)

# 输出降维后的数据形状
print("原始数据形状:", X.shape)
print("降维后数据形状:", X_pca.shape)

# 输出主成分的方差解释比例
explained_variance_ratio = pca.explained_variance_ratio_
print("主成分的方差解释比例:", explained_variance_ratio)
print("累计方差解释比例:", np.sum(explained_variance_ratio))

# 可视化降维后的数据
plt.figure(figsize=(8, 6))
for target, color in zip(np.unique(y), ['r', 'g', 'b']):
    indices = y == target
    plt.scatter(X_pca[indices, 0], X_pca[indices, 1], c=color, label=iris.target_names[target])
plt.xlabel('第一主成分')
plt.ylabel('第二主成分')
plt.title('PCA 降维后的鸢尾花数据集')
plt.legend()
plt.show()
