import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("diabetess.csv")
X = data[['Glucose','BloodPressure']]
Y = data['Outcome']

X =  StandardScaler().fit_transform(X)
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.56,random_state=120)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

asc = accuracy_score(y_test,y_pred)
print("Accuracy Score is ",asc)

h=0.2
x_min,x_max = X[: , 0].min() -1, X[: , 0].max() +1
y_min,y_max = X[: , 1].min() -1, X[: , 1].max() +1
xx, yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

Z = knn.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)

plt.contourf(xx,yy,Z,cmap="coolwarm")
plt.scatter(X[:, 0], X[: , 1], c=Y, edgecolor='k', cmap="coolwarm")
plt.xlabel("Features 1")
plt.ylabel("Features 2")
plt.title("KNN Decision BOundary")
plt.show()