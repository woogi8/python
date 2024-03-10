import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 가상의 데이터 생성
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

# 다항 회귀를 위해 2차항을 적용
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# 다중 회귀 모델 훈련
model = LinearRegression()
model.fit(X_poly, y)

# 예측값 계산
X_fit = np.linspace(0, 5, 100)[:, np.newaxis]
X_fit_poly = poly.transform(X_fit)
y_fit = model.predict(X_fit_poly)

# 그래프 그리기
plt.scatter(X, y, label='Data')
plt.plot(X_fit, y_fit, color='red', label='Polynomial Regression')
plt.xlabel('Product Feature')
plt.ylabel('Yield')
plt.title('Product Yield vs. Feature (Polynomial Regression)')
plt.legend()
plt.show()
