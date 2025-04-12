import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题


# 读取文件
data = pd.read_csv('house_price_regression_dataset.csv')
# 查看前几行数据
print(data.head())
# 查看数据信息，包括数据类型、缺失值等
print(data.info())
# 处理缺失值
data = data.fillna(data.mean())
# 选择面积和房间数作为特征，目标变量是房价
X = data[['平方英尺', '卧室数量']] # 特征矩阵
y = data['房价'] # 目标变量
# 数据标准化
scaler = StandardScaler()
X = scaler.fit_transform(X)
# 创建线性回归模型
model = LinearRegression()
model.fit(X, y)
# 结果评估
y_pred = model.predict(X)
# 评估指标,常用的评估指标有均方误差（MSE）、决定系数（R²）等。
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"均方误差: {mse}")
print(f"决定系数: {r2}")
# 结果可视化
plt.scatter(y, y_pred)
plt.xlabel('实际房价')
plt.ylabel('预测房价')
plt.title('线性回归预测房价')
# 绘制对角线
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw = 2)
plt.show()