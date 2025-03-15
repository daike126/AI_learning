import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 数据加载与清洗
# 数据加载
# 从CSV文件读取数据，显示前5行、数据维度、字段类型
df = pd.read_csv('supermarket_sales - Sheet1.csv')
print(df.head(5))
rows, columns = df.shape
print(f"数据维度：{rows} 行 {columns} 列")
print('字段类型：', df.dtypes)

# 检查缺失值数量
# （isnull().sum() 整体的作用就是统计 DataFrame 里每列缺失值的数量）
print(df.isnull().sum())

# 删除缺失率>30%的列（isnull().mean() 计算每列的缺失率）
missing_ratio = df.isnull().mean()
# 找出缺失值比例超过 0.3 的列
columns_to_drop = missing_ratio[missing_ratio > 0.3].index
# 使用 drop 方法删除指定列
df = df.drop(columns=columns_to_drop)

# 数值型字段用中位数填充（如年龄）
# 获取所有数值型字段
numeric_columns = df.select_dtypes(include=[np.number]).columns
# 对数值型字段用中位数填充
for col in numeric_columns:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

# 类别型字段用众数填充（如性别）
# 获取所有类别型字段
categorical_columns = df.select_dtypes(include=['object']).columns
# 对类别型字段用众数填充
for col in categorical_columns:
    mode_value = df[col].mode()[0]
    df[col] = df[col].fillna(mode_value)

# 数据预处理
# 删除重复值
df = df.drop_duplicates()
# 转换日期字段为datetime类型，提取年/月/日信息
df['Date'] = pd.to_datetime(df['Date'])
# 提取年、月、日信息
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
print(df.head())

# 对分类变量（如城市、性别）进行编码
# pd.get_dummies() 采用独热编码的方式分类，如对于 gender 列
# 会创建 gender_男 和 gender_女 两列，根据样本的 gender 值相应列置为 1，另一列置为 0。
# LabelEncoder 采用标签编码的方式分类，标签编码会为分类变量的每个不同取值分配一个唯一的整数。
df = pd.get_dummies(df, columns=['City', 'Gender'])
print("独热编码后的 df:")
print(df.head())

# 探索性分析（EDA）
# 统计指标计算
# 数值型字段：计算均值、中位数、标准差、四分位数
numeric_columns = df.select_dtypes(include=[np.number]).columns
numeric_stats = df[numeric_columns].describe()
# 额外计算中位数
numeric_stats.loc['median'] = df[numeric_columns].median()
print("数值型字段的统计信息：")
print(numeric_stats)

# 类别型字段：统计频次分布（如各城市销售额占比）
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    frequency_distribution = df[col].value_counts()
    percentage_distribution = df[col].value_counts(normalize=True) * 100
    print(f"\n类别型字段 {col} 的频次分布：")
    print(frequency_distribution)
    print(f"\n类别型字段 {col} 的占比分布（%）：")
    print(percentage_distribution)

# 业务问题分析
# 超市销售数据：
# 计算总销售额、平均评分
total_sales = df['Total'].sum()
average_rating = df['Rating'].mean()
print(f"总销售额: {total_sales}")
print(f"平均评分: {average_rating}")

# 分析不同商品类别的销售额分布
product_line_sales = df.groupby('Product line')['Total'].sum()
print("不同商品类别的销售额分布:")
print(product_line_sales)

# 探索会员 vs 非会员用户的平均消费金额差异
member_type_sales = df.groupby('Customer type')['Total'].mean()
print("会员 vs 非会员用户的平均消费金额差异:")
print(member_type_sales)

# 数据可视化
# 基础图表
# 用Matplotlib/Seaborn绘制：
# 柱状图：商品类别的销售额对比
plt.figure(figsize=(10, 6))
product_line_sales.plot(kind='bar')
plt.title('不同商品类别的销售额对比')
plt.xlabel('商品类别')
plt.ylabel('销售额')
plt.show()

# 箱线图：不同客户类型的消费金额分布
plt.figure(figsize=(10, 6))
sns.boxplot(x='Customer type', y='Total', data=df)
plt.title('不同客户类型的消费金额分布')
plt.show()

# 折线图：销售额随时间（月/日）的变化趋势
monthly_sales = df.groupby('month')['Total'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line')
plt.title('销售额随月份的变化趋势')
plt.xlabel('月份')
plt.ylabel('销售额')
plt.show()

# 分面图：分组对比销售额
g = sns.FacetGrid(df, col='Gender_Male', row='Customer type')
g.map(sns.barplot, 'Product line', 'Total')
plt.show()