# 递归是指在函数的定义中调用函数自身
# 下面是一个计算阶乘的递归函数
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# 记忆式搜索计算斐波那契数列
# 记忆式搜索是一种优化递归的方法, 通过存储已经计算过的结果, 避免重复计算, 从而提升效率
memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result

print(fibonacci(10))

# 汉诺塔游戏
# 目标是将所有盘子从一个柱子移动到另一个柱子, 并且在移动过程中大盘子不能放在小盘子上面
# n 是一个整数参数，表示要移动的圆盘数量。
# source起始柱, auxiliary辅助柱, target终点柱
def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"将圆盘 1 从 {source} 移动到 {target}")
        return
    else:
        hanoi(n - 1, source, target, auxiliary)
        print(f"将圆盘 {n} 从 {source} 移动到 {target}")
        hanoi(n - 1, auxiliary, source, target)

hanoi(3, 'A', 'B', 'C')

