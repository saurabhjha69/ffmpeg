import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from matplotlib import pyplot as plt

def import_data_csv(path):
    data = pd.read_csv(path,header=0)
    print("Data Size ",data.size)
    print("Data Shape ",data.shape)
    return data
imported_data = import_data_csv("weather.csv")
le = LabelEncoder()
for col in ["outlook","temp","humidity","windy","play"]:
    imported_data[col] = le.fit_transform(imported_data[col]) 


x = imported_data.drop("play",axis = 1)
y = imported_data["play"]

treeClass = DecisionTreeClassifier(criterion="entropy",random_state=0).fit(x,y)
tree.plot_tree(treeClass)
plt.show()

print(x,"\n")
print(y)