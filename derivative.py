import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制函数y = x^2及其导数y' = 2x的曲线
x = np.linspace(-5, 5, 100)
y = x ** 2
y_derivative = 2 * x

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = x^2')
plt.plot(x, y_derivative, label="y' = 2x")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and Its Derivative')
plt.legend()
plt.show()