import pandas as pd

file_path = "C:\\Users\\36172\\Desktop\\文档\\a1.csv"

# Series：是一种一维的数据结构，类似于 Python 中的列表或 NumPy 数组，但它还带有索引。
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# DataFrame：是 Pandas 中最常用的数据结构，它类似于电子表格或 SQL 表，是一个二维的表格型数据结构，由行和列组成。
data = {
    'Name': ["张三","李四"],
    'Age': [20,21],
    'Score': [85,92]
}
df = pd.DataFrame(data)
print(df)

# 合并：merge()方法用于根据指定的键将两个 DataFrame 合并。
# on,按照哪行来连接。how,怎样连接。
# (inner内连接,保留两个 DataFrame 中 'key' 列值相同的行。)
# 'left'(左连接，保留左 DataFrame 的所有行),'right'(右连接，保留右 DataFrame 的所有行),'outer'(外连接，保留两个 DataFrame 的所有行)
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})
df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value2': [5, 6, 7, 8]
})
merged_df = df1.merge(df2, on='key', how='inner')
print(merged_df)

# 连接：concat()方法用于沿着指定的轴将多个 DataFrame 连接起来。
# axis = 0,按行方向拼接，也就是把第二个 DataFrame 直接添加到第一个 DataFrame 的下方
# axis = 1,按列方向拼接，会把第二个 DataFrame 添加到第一个 DataFrame 的右边
df3 = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': ['a', 'b', 'c']
})
df4 = pd.DataFrame({
    'col1': [4, 5, 6],
    'col2': ['d', 'e', 'f']
})
concatenated_df = pd.concat([df3, df4], axis=0)
print(concatenated_df)

# 写入数据：可以将数据写入到文件中，如将 DataFrame 写入 CSV 文件：
df.to_csv(file_path, index=False)

# 读取数据：Pandas 可以从多种文件格式中读取数据，如 CSV、Excel、JSON 等。
df = pd.read_csv(file_path)

# 数据查看和基本信息获取
# 查看数据
# head()：# 用于查看数据框的前 n 行，默认是前 5 行。
# tail()：# 用于查看数据框的后 n 行，默认是后 5 行。
# 获取基本信息
# info()：提供数据框的基本信息，包括列的数据类型、非空值的数量等。
# describe()：生成数据框的描述性统计信息，包括计数、均值、标准差、最小值、四分位数、最大值等。
# 数据选择和过滤
# 按列选择：可以通过列名来选择列，例如df['col1']可以选择名为 'col1' 的列。
# 按行选择：可以使用loc和iloc方法按行索引来选择行。loc基于标签索引，iloc基于位置索引。例如df.loc[0]选择第一行（索引为 0），df.iloc[0]也是选择第一行。
# 条件过滤：可以根据条件筛选数据，例如df[df['col1'] > 3]可以筛选出 'col1' 列中值大于 3 的行。
# 数据清洗
# 处理缺失值
# isnull()和notnull()：用于检测数据中的缺失值，返回布尔值。
# dropna()：用于删除包含缺失值的行或列。
# fillna()：用于填充缺失值，可以用指定的值或方法进行填充，如均值、中位数等。
# 去除重复值：drop_duplicates()方法用于去除数据框中的重复行。