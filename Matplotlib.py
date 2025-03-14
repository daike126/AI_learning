import matplotlib.pyplot as plt
import numpy as np

# 绘制一条折线图
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# 创建图形和坐标轴
plt.figure()
# 绘制折线图
plt.plot(x, y)
# 设置图表标题和坐标轴标签
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# 显示图表
plt.show()

# 绘制多条折线图
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
# 创建图形和坐标轴
plt.figure()
# 绘制两条折线图，并设置不同的颜色和标签
plt.plot(x, y1, color='blue', label='Line 1')
plt.plot(x, y2, color='red', label='Line 2')
# 设置图表标题和坐标轴标签
plt.title('Multiple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# 显示图例(左上角标志)
plt.legend()
# 显示图表
plt.show()

# 绘制散点图
# 生成随机数据
# 随机生成42个点
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
# 创建图形和坐标轴
plt.figure()
# 绘制散点图
plt.scatter(x, y)
# 设置图表标题和坐标轴标签
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# 显示图表
plt.show()

# 绘制柱状图
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]
# 创建图形和坐标轴
plt.figure()
# 绘制柱状图
plt.bar(categories, values)
# 设置图表标题和坐标轴标签
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
# 显示图表
plt.show()

# 绘制扇形图
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
sizes = [30, 25, 20, 25]
# 创建图形和坐标轴
plt.figure()
# 绘制饼图(autopct 用于显示每个扇形所占的百分比)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# 设置图表标题
plt.title('Pie Chart')
# 显示图表
plt.show()

# 子窗口以及样式设置
# np.linspace会在 0 到 10 这个区间内生成 100 个均匀分布的数字。
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# plt.rcParams 来设置全局的字体属性
plt.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
plt.rcParams['font.size'] = 12  # 设置字体大小

# subplots() 创建一个 2 行 1 列的子图布局(窗口大小(英寸)：figsize=(宽, 高))
# suptitle() 方法为整个图形设置一个总的标题,set_title() 为每个子图设置单独的标题
# axs[0, 0],通过索引访问每个子图对象，并在其上进行绘图操作
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
fig.suptitle('三角函数图像')

# 在第一个子图中绘制正弦曲线
# plot() 绘制图形, color 设置颜色, linewidth 设置线条的粗细
# set_facecolor() 方法来设置坐标轴的背景颜色
# grid(True) 可以添加网格线，使图表看起来更清晰
axs[0].plot(x, y1, color='blue', linewidth=2)
axs[0].set_title('正弦函数')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_facecolor('lightgray')  # 设置子图背景颜色
axs[0].grid(linestyle='--', color='gray')  # 添加网格线

# 在第二个子图中绘制余弦曲线
axs[1].plot(x, y2, color='red', linewidth=2)
axs[1].set_title('余弦函数')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_facecolor('lightgray')
axs[1].grid(linestyle='--', color='gray')

# 设置坐标轴刻度范围和刻度标签
# 如set_xlim(0, 10) 将 x 轴的范围设置为从 0 到 10。
# set_xticklabels() 方法来设置刻度标签的内容
# set_xticklabels([]) 设置对应的刻度标签
axs[0].set_xlim(0, 10)
axs[0].set_xticks([0, 2, 4, 6, 8, 10])
axs[0].set_xticklabels(['0', '2', '4', '6', '8', '10'])
axs[1].set_xlim(0, 10)
axs[1].set_xticks([0, 2, 4, 6, 8, 10])
axs[1].set_xticklabels(['0', '2', '4', '6', '8', '10'])

# 调整子图之间的间距(pad), 高距h_pad, 宽距w_pad
plt.tight_layout(pad=2)

# 显示图形
plt.show()