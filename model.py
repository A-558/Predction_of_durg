import pandas as pd 

import pickle 
from sklearn.model_selection import train_test_split 

dataset = pd.read_csv("drug200.csv")
dataset["Sex"] = dataset["Sex"].map({"F":0,"M":1})
dataset["BP"] = dataset["BP"].map({"LOW":0,"NORMAL":1,"HIGH":2})
dataset["Cholesterol"]=dataset["Cholesterol"].map({"HIGH":2,"NORMAL":1})
x = dataset.drop(["Drug"], axis = 1)
y = dataset["Drug"]
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.33,random_state = 42)
from sklearn.tree import DecisionTreeClassifier 
gini_value = DecisionTreeClassifier( max_depth = 2 , random_state = 0)
gini_value.fit(X_train,y_train)

pickle.dump(gini_value,open("model.pkl","wb"))
model = pickle.load(open('model.pkl',"rb"))
print(model.predict([[23, 1, 1,1,25]]))