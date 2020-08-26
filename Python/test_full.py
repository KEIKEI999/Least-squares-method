import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.51, 0.76, 1.06, 1.41, 1.75, 1.9, 2.01, 2.15, 2.27, 2.4, 2.49, 2.59, 2.67, 2.76, 2.83, 2.89, 2.95, 3.01, 3.05, 3.11, 3.15, 3.19, 3.23, 3.28, 3.31, 3.34, 3.38, 3.4, 3.43, 3.46, 3.49, 3.51])
y = np.array([10, 11, 12, 13, 14, 14.5, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])


# 第1区間
x1 = x[1:6]
y1 = y[1:6]

coef1 = np.polyfit(x1, y1, 2)	# 最小二乗法で得られた2次関数の各係数
print("第1区間各係数", end=':')
print(coef1)

quad_func1 = np.poly1d(coef1)	# 2次関数の各係数から2次関数を生成
print("第1区間関数:")
print(quad_func1)


# 第2区間
x2 = x[6:13]
y2 = y[6:13]

coef2 = np.polyfit(x2, y2, 2)	# 最小二乗法で得られた2次関数の各係数
print("第2区間各係数", end=':')
print(coef2)

quad_func2 = np.poly1d(coef2)	# 2次関数の各係数から2次関数を生成
print("第2区間関数:")
print(quad_func2)

# 第3区間
x3 = x[13:23]
y3 = y[13:23]

coef3 = np.polyfit(x3, y3, 2)	# 最小二乗法で得られた2次関数の各係数
print("第3区間各係数", end=':')
print(coef3)

quad_func3 = np.poly1d(coef3)	# 2次関数の各係数から2次関数を生成
print("第3区間関数:")
print(quad_func3)


# 第4区間
x4 = x[23:32]
y4 = y[23:32]

coef4 = np.polyfit(x4, y4, 2)	# 最小二乗法で得られた2次関数の各係数
print("第3区間各係数", end=':')
print(coef4)

quad_func4 = np.poly1d(coef4)	# 2次関数の各係数から2次関数を生成
print("第3区間関数:")
print(quad_func4)


xp = np.linspace(0, 4, 400)	# 同定した2次関数のx軸を生成

#plt.plot(x, y, '+', \
#	xp[57:195], quad_func1(xp[57:195]), '-r',   \
#	xp[195:269], quad_func2(xp[195:269]), '-g', \
#	xp[269:325], quad_func3(xp[269:325]), '-b', \
#	xp[325:353], quad_func4(xp[325:353]), '-c'   )

plt.plot(x, y, '+', \
	xp, quad_func1(xp), '-r',   \
	xp, quad_func2(xp), '-g', \
	xp, quad_func3(xp), '-b', \
	xp, quad_func4(xp), '-c'   )

plt.ylim(10,41)
plt.xlim(0,4)
plt.show()

