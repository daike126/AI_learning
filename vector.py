#len() 是 Python 的内置函数，用于返回对象的长度或元素个数。
#range(x),生成一个从 0 开始，到 x-1 结束的整数序列。
#range(x, y),生成一个从 x 开始，到 y-1 结束的整数序列。
#range(x, y, z),生成一个从 x 开始，以 y 为步长，到 z-1 结束的整数序列。
def vector_add(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]+v2[i])
    return v3
#列表推导式:return [v1[i]+v2[i] for i in range(len(v1))]
#它的作用是将循环中每次计算得到的 v1[i]+v2[i] 的结果收集起来，组成一个新的列表。
#语法是在方括号 [] 内包含一个表达式和一个 for 循环
result = vector_add([1,2],[3,4])
print(result)