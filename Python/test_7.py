import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.51, 0.76, 1.06, 1.41, 1.75, 1.9, 2.01, 2.15, 2.27, 2.4, 2.49, 2.59, 2.67, 2.76, 2.83, 2.89, 2.95, 3.01, 3.05, 3.11, 3.15, 3.19, 3.23, 3.28, 3.31, 3.34, 3.38, 3.4, 3.43, 3.46, 3.49, 3.51])
y = np.array([10, 11, 12, 13, 14, 14.5, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])


coef = np.polyfit(x, y, 7)	# 最小二乗法で得られた7次関数の各係数
print("各係数", end=':')
print(coef)

quad_func = np.poly1d(coef)	# 2次関数の各係数から2次関数を生成
print("関数:")
print(quad_func)

xp = np.linspace(0, 4, 400)	# 同定した2次関数のx軸を生成

plt.plot(x, y, '+', \
	xp, quad_func(xp), '-' )

plt.ylim(10,41)
plt.xlim(0,4)
plt.show()

