import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# load_dataset() 用于加载 Seaborn 内置的示例数据集的，比如 "tips"、"iris" 等
# Seaborn 内置的示例数据集储存在Github仓库，需要加速网页
tips = sns.load_dataset("tips")
print(tips.head())

# 主题设置
# 使用 set_theme() 快速为图表设置一个统一的主题风格
sns.set_theme()
# 使用 set_style() 设置特定风格
sns.set_style("whitegrid")

# 基本绘图类型
# lineplot()绘制折线图
sns.lineplot(data=tips, x="total_bill", y="tip")
plt.title("Line Plot of Total Bill vs Tip")
plt.show()

# scatterplot()绘制 total_bill 和 tip 的散点图
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

# barplot()绘制不同性别的平均小费柱状图
sns.barplot(data=tips, x="sex", y="tip")
plt.title("Average Tip by Gender")
plt.show()

# boxplot()绘制 total_bill 的箱线图
# 箱线图用于展示数据的分布情况，包括中位数、四分位数、异常值等。
sns.boxplot(data=tips, x="total_bill")
plt.title("Box Plot of Total Bill")
plt.show()

# histplot()绘制 total_bill 的直方图
# 直方图用于展示数据的分布频率，kde：是否添加核密度估计曲线。
sns.histplot(data=tips, x="total_bill", kde=True)
plt.title("Histogram of Total Bill")
plt.show()

# 高级图表
# 分布图sns.displot()
# 如需要绘制多种类型的分布图形或进行分面绘图，使用 displot()。
sns.displot(data=None, x=None, y=None, hue=None, row=None, col=None, kind='hist')
# hue：用于对数据进行分组的变量名，不同组的数据会用不同的颜色表示。
# row、col：用于创建分面网格的变量名，row 表示按行分面，col 表示按列分面。
# kind：指定绘制的图形类型，可选值有 hist（直方图）、
# kde（核密度估计图）、ecdf（经验累积分布函数图）、
# hist-kde（同时绘制直方图和核密度估计图）等，默认值为 'hist'。

# 如按时间和性别分面绘制 total_bill 的直方图
sns.displot(data=tips, x="total_bill", row="time", col="sex")
plt.show()

# 热力图sns.heatmap()
# 热力图是一种用颜色编码来表示数据矩阵中数值大小的图表，常用于展示数据的相关性或分布情况。
# 生成随机数据矩阵
np.random.seed(0)
data = np.random.rand(10, 10)
df = pd.DataFrame(data)
# 绘制热力图，使用 YlGnBu 颜色映射
sns.heatmap(df, cmap="YlGnBu")
plt.title("Heatmap with YlGnBu Colormap")
plt.show()

# 多图绘制
# FacetGrid 用于根据数据的不同类别创建多个子图。
# 根据日和性别绘制 total_bill 的直方图
g = sns.FacetGrid(tips, row="day", col="sex")
g.map(sns.histplot, "total_bill")
plt.show()

# PairGrid 用于绘制多个变量之间的两两关系图。
g = sns.PairGrid(tips, vars=["tip", "day"])
g.map_diag(sns.histplot)
g.map_offdiag(sns.barplot)
plt.show()
