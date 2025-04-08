from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# 加载鸢尾花数据集
iris = load_iris()
# 特征矩阵
X = iris.data
# 目标向量
y = iris.target

# 将数据集划分为训练集和测试集，测试集占比 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树分类器对象
clf = DecisionTreeClassifier()

# 使用训练数据对模型进行训练
clf.fit(X_train, y_train)

# 使用训练好的模型对测试数据进行预测
y_pred = clf.predict(X_test)

# 计算模型的准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy}")

# 创建标准化对象
scaler = StandardScaler()

# 对训练数据进行标准化处理
X_train_scaled = scaler.fit_transform(X_train)

# 使用相同的标准化参数对测试数据进行处理
X_test_scaled = scaler.transform(X_test)

# 创建新的决策树分类器并使用标准化后的数据进行训练和预测
clf_scaled = DecisionTreeClassifier()
clf_scaled.fit(X_train_scaled, y_train)
y_pred_scaled = clf_scaled.predict(X_test_scaled)

# 计算使用标准化数据训练的模型的准确率
accuracy_scaled = accuracy_score(y_test, y_pred_scaled)
print(f"使用标准化数据训练的模型准确率: {accuracy_scaled}")

# 创建决策树分类器对象
clf_cv = DecisionTreeClassifier()

# 进行 5 折交叉验证
scores = cross_val_score(clf_cv, X, y, cv=5)

# 输出每次交叉验证的得分和平均得分
print(f"每次交叉验证的得分: {scores}")
print(f"平均得分: {scores.mean()}")
