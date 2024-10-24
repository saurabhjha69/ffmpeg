import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def import_csv(path):
    data = pd.read_csv(path,header=0)
    print("Data Size ",data.size)
    print("Data Shape ",data.shape)
    return data
imported_data = import_csv("diabetess.csv")

x = imported_data.drop("Outcome",axis=1)
y = imported_data["Outcome"]

train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.4,random_state=42)

LinearModel = LinearRegression().fit(train_x,train_y)

pred_y = LinearModel.predict(test_x)

error = mean_squared_error(test_y,pred_y)
print("Mean Squared error is ",error)

plt.scatter(test_y,pred_y,color="blue")
plt.plot([test_y.min(),test_y.max()],[test_y.min(),test_y.max()],"k--",lw=4)
plt.title("Actual vs Predicted")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
